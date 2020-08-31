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
from swatchbook.base import FileFormatError, Book, SwatchBook, Group, Swatch
from swatchbook.base import Spacer, Break, Color, Tint, Tone, Pattern, Gradient
from swatchbook.base import ColorStop, OpacityStop
from swatchboook.icc import ICCprofile, BadICCprofile

__ALL__ = ['color', 'icc', 'lcms2']
VERSION = "0.8"
