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
from abc import ABC, abstractmethod
import importlib
from swatchbook.color import dirpath


class WebSvc(ABC):
    @property
    @staticmethod
    @abstractmethod
    def about():
        return ''

    @property
    @staticmethod
    @abstractmethod
    def content():
        return []

    @property
    @staticmethod
    @abstractmethod
    def nbLevels():
        return 0

    @property
    @staticmethod
    @abstractmethod
    def url():
        return None

    @abstractmethod
    def level0(self):
        pass

    @abstractmethod
    def read(self, *args):
        pass


for websvc in dirpath(__file__).iterdir():
    if websvc.match('*.py') and websvc.name not in ('__init__', 'template'):
        module = importlib.import_module(websvc.name)
        websvc_cls = (attr for attr in dir(module) if issubclass(attr, WebSvc))
        if websvc_cls:
            globals()[websvc_cls.__name__] = websvc_cls


members = {}

for websvc in WebSvc.__subclasses__():
    members[websvc.__name__] = websvc.__doc__
