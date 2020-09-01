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
import os
from pathlib import Path
from abc import ABC, abstractmethod
import importlib
# import xml.etree.cElementTree as etree
# from xml.sax.saxutils import escape as xmlescape
# from xml.sax.saxutils import unescape as xmlunescape
# import zipfile
# import string

# from swatchbook import *
from swatchbook.color import dirpath


def idfromvals(vals):
    id = []
    for val in vals:
        id.append(str(round(val, 3)))
    return "(" + ", ".join(id) + ")"


def hex2(val):
    return hex(int(round(val)))[2:].rjust(2, '0')


# TODO: Follo this -> meant to disappear
# - used in the ASE and Scribus codecs
def unicc(values):
    values = values.copy()
    for val in values:
        if isinstance(val, tuple):
            values[val[0]] = values[val]
            del values[val]
    return values


class SBCodec(ABC):
    @property
    @abstractmethod
    def ext():
        return False

    @property
    @abstractmethod
    def iswriter():
        return False

    @property
    @abstractmethod
    def isreader():
        return False

    @staticmethod
    @abstractmethod
    def test(file: Path):
        pass

    @staticmethod
    @abstractmethod
    def read(swatchbook, file: Path):
        pass

    @staticmethod
    @abstractmethod
    def write(swatchbook):
        pass


for codec in dirpath(__file__).iterdir():
    if codec.match('*.py') and codec.name not in ('__init__', 'template'):
        module = importlib.import_module(codec.name)
        codec_cls = (attr for attr in dir(module) if issubclass(attr, SBCodec))
        if codec_cls:
            globals()[codec_cls.__name__] = codec_cls


writes = []
reads = []
readexts = {}

for codec in SBCodec.__subclasses__():
    cname = codec.__name__
    exts = codec.ext
    if codec.isreader:
        reads.append(cname)
        for ext in exts:
            if ext in readexts.keys():
                readexts[ext].append(cname)
            else:
                readexts[ext] = [cname]
    if codec.iswriter:
        writes.append(cname)
