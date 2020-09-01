#!/usr/bin/env python
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
from collections import OrderedDict
from urllib.request import urlopen

import swatchbook.websvc as websvc
import swatchbook as swbk
from swatchbook.codecs import idfromvals


class pantone(websvc.WebSvc):
    """Pantone."""

    @property
    @staticmethod
    def content():
        return ['swatchbook']

    @property
    @staticmethod
    def about():
        return 'These data come from Pantone\'s <a href="http://www.pantone.com/pages/pantone/color_xref.aspx">X-Ref</a> tool.<br /><br />PANTONE® and other Pantone, Inc. trademarks are the property of Pantone, Inc. © Pantone, Inc. 2010'

    @property
    @staticmethod
    def nbLevels():
        return 1

    @property
    @staticmethod
    def url():
        return 'http://www.pantone.com/images/xref/'

    def __init__(self):
        self._guide = {'1': u'COLOR BRIDGE® Coated',
                       '2': u'COLOR BRIDGE® Uncoated',
                       '3': u'FORMULA GUIDE Solid Coated',
                       '4': u'FORMULA GUIDE Solid Matte',
                       '5': u'FORMULA GUIDE Solid Uncoated',
                       '6': u'GoeGuide™ coated',
                       '7': u'GoeGuide™ uncoated',
                       '8': u'FASHION + HOME cotton',
                       '9': u'FASHION + HOME paper',
                       '10': u'GoeBridge™ coated',
                       '11': u'COLOR BRIDGE® coated',
                       '12': u'COLOR BRIDGE® uncoated',
                       '13': u'FORMULA GUIDE Solid Coated',
                       '14': u'FORMULA GUIDE Solid Uncoated',
                       '15': u'PREMIUM METALLICS Coated',
                       '16': u'PASTELS & NEONS Coated',
                       '17': u'PASTELS & NEONS Uncoated',
                       '18': u'CMYK Coated',
                       '19': u'CMYK Uncoated',
                       '20': u'METALLIC FORMULA GUIDE coated'}

    def level0(self):
        guides = OrderedDict()
        guides[u'PANTONE® MATCHING SYSTEM'] = OrderedDict()
        guides[u'PANTONE® MATCHING SYSTEM']['3'] = self._guide['3']
        guides[u'PANTONE® MATCHING SYSTEM']['5'] = self._guide['5']
        guides[u'PANTONE® MATCHING SYSTEM']['4'] = self._guide['4']
        guides[u'PANTONE® MATCHING SYSTEM']['1'] = self._guide['1']
        guides[u'PANTONE® MATCHING SYSTEM']['2'] = self._guide['2']
        guides[u'PANTONE® MATCHING SYSTEM']['20'] = self._guide['20']
        guides[u'PANTONE® MATCHING SYSTEM']['8'] = self._guide['8']
        guides[u'PANTONE® MATCHING SYSTEM']['9'] = self._guide['9']
        guides[u'PANTONE® Goe™ System'] = OrderedDict()
        guides[u'PANTONE® Goe™ System']['6'] = self._guide['6']
        guides[u'PANTONE® Goe™ System']['7'] = self._guide['7']
        guides[u'PANTONE® Goe™ System']['10'] = self._guide['10']
        guides[u'PANTONE® PLUS SERIES'] = OrderedDict()
        guides[u'PANTONE® PLUS SERIES']['13'] = self._guide['13']
        guides[u'PANTONE® PLUS SERIES']['14'] = self._guide['14']
        guides[u'PANTONE® PLUS SERIES']['11'] = self._guide['11']
        guides[u'PANTONE® PLUS SERIES']['12'] = self._guide['12']
        guides[u'PANTONE® PLUS SERIES']['15'] = self._guide['15']
        guides[u'PANTONE® PLUS SERIES']['16'] = self._guide['16']
        guides[u'PANTONE® PLUS SERIES']['17'] = self._guide['17']
        guides[u'PANTONE® PLUS SERIES']['18'] = self._guide['18']
        guides[u'PANTONE® PLUS SERIES']['19'] = self._guide['19']
        return guides

    def read(self, swatchbook, guide):
        page = urlopen(self.url + 'xref_lib' + guide + '.js').readlines()
        swatchbook.info.title = 'PANTONE® ' + self._guide[guide]
        for line in page[1:]:
            if line.strip() > '':
                line = line.split('"')[1].split(',')
                item = swbk.Color(swatchbook)
                item.usage.add('spot')
                _id = str(line[1])
                item.info.title = 'PANTONE® ' + _id
                item.values[('Lab', False)] = [int(line[2]), int(line[3]), int(line[4])]
                item.values[('sRGB', False)] = [int(line[6]) / 0xFF, int(line[7]) / 0xFF, int(line[8]) / 0xFF]
                if line[13] == '1':
                    item.values[('CMYK', False)] = [int(line[9]) / 100, int(line[10]) / 100, int(line[11]) / 100, int(line[12]) / 100]

                if id in swatchbook.materials:
                    if item.values[item.values.keys()[0]] == swatchbook.materials[_id].values[swatchbook.materials[_id].values.keys()[0]]:
                        swatchbook.book.items.append(swbk.Swatch(_id))
                        continue
                    else:
                        sys.stderr.write('duplicated id: %s \n' % _id)
                        item.info.title = _id
                        _id = _id + idfromvals(item.values[item.values.keys()[0]])
                item.info.identifier = _id
                swatchbook.materials[_id] = item
                swatchbook.book.items.append(swbk.Swatch(id))
