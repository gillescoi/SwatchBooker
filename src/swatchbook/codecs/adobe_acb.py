#!/usr/bin/env python3
# coding: utf-8
#
#       Copyright 2008 Olivier Berten <olivier.berten@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
import sys
from pathlib import Path
import struct

import swatchbook.codecs as codecs
import swatchbook as swbk


class adobe_acb(codecs.SBCodec):
    """Adobe Color Book."""

    @property
    def ext():
        return ('acb',)

    @property
    def isreader():
        return True

    @property
    def iswriter():
        return False

    @staticmethod
    def test(file: Path):
        with open(file, 'rb') as file:
            data = file.read(4)
        if struct.unpack('4s', data)[0] == b'8BCB':
            return True
        else:
            return False

    @staticmethod
    def read(swatchbook, file):
        def decode_str(text_string):
            if text_string[0:4] == '$$$/':
                text_string = text_string.partition('=')[2]
            return text_string.replace('^C', u'©').replace('^R', u'®')

        with open(file, 'rb') as stream:
            # Title
            stream.seek(8, 1)
            length = struct.unpack('>L', stream.read(4))[0]
            if length > 0:
                tmp = struct.unpack('%ss' % (length * 2), stream.read(length * 2))[0]
                swatchbook.info.title = decode_str(tmp.decode(encoding='utf_16_be'))

            # Prefix
            length = struct.unpack('>L', stream.read(4))[0]
            if length > 0:
                tmp = struct.unpack('%ss' % (length * 2), stream.read(length * 2))[0]
                prefix = decode_str(tmp.decode(encoding='utf_16_be'))
            else:
                prefix = ''

            # Suffix
            length = struct.unpack('>L', stream.read(4))[0]
            if length > 0:
                tmp = struct.unpack('%ss' % (length * 2), stream.read(length * 2))[0]
                suffix = decode_str(tmp.decode(encoding='utf_16_be'))
            else:
                suffix = ''

            # Rights
            length = struct.unpack('>L', stream.read(4))[0]
            if length > 0:
                tmp = struct.unpack('%ss' % (length * 2), stream.read(length * 2))[0]
                swatchbook.info.rights = decode_str(tmp.decode(encoding='utf_16_be'))

            # NbColors, Columns, Model
            nbcolors = struct.unpack('>H', stream.read(2))[0]
            swatchbook.book.display['columns'] = struct.unpack('>H', stream.read(2))[0]
            stream.seek(2, 1)
            model = struct.unpack('>H', stream.read(2))[0]

            for i in range(nbcolors):
                item = swbk.Color(swatchbook)
                length = struct.unpack('>L', stream.read(4))[0]
                if length > 0:
                    tmp = struct.unpack('%ss' % (length * 2), stream.read(length * 2))[0]
                    item.info.title = prefix + decode_str(tmp.decode(encoding='utf_16_be')) + suffix

                id = struct.unpack('>6s', stream.read(6))[0].strip().decode(encoding='ASCII')

                if model == 0:
                    R, G, B = struct.unpack('>3B', stream.read(3))
                    item.values[('RGB', False)] = [R / 0xFF, G / 0xFF, B / 0xFF]
                elif model == 2:
                    C, M, Y, K = struct.unpack('>4B', stream.read(4))
                    item.values[('CMYK', False)] = [1 - C / 0xFF, 1 - M / 0xFF, 1 - Y / 0xFF, 1 - K / 0xFF]
                elif model == 7:
                    L, a, b = struct.unpack('>3B', stream.read(3))
                    item.values[('Lab', False)] = [L * 100 / 0xFF, a - 0x80, b - 0x80]
                else:
                    sys.stderr.write('unknown color model [%i]\n' % model)

                if item.info.title == '' and sum(item.values[item.values.keys()[0]]) == 0:
                    swatchbook.book.items.append(swbk.Spacer())
                    continue

                if id in swatchbook.materials:
                    if item.values[item.values.keys()[0]] == swatchbook.materials[id].values[swatchbook.materials[id].values.keys()[0]]:
                        swatchbook.book.items.append(swbk.Swatch(id))
                        continue
                    else:
                        sys.stderr.write('duplicated id: %i\n' % id)
                        id = id + codecs.idfromvals(item.values[item.values.keys()[0]])
                elif len(id) == 0:
                    id = codecs.idfromvals(item.values[item.values.keys()[0]])

                item.info.identifier = id
                swatchbook.materials[id] = item
                swatchbook.book.items.append(swbk.Swatch(id))

            if stream.read(4):
                if struct.unpack('>4s', stream.read(4))[0] == b'spot':
                    for id in swatchbook.materials:
                        if isinstance(swatchbook.materials[id], swbk.Color):
                            swatchbook.materials[id].usage.add('spot')
