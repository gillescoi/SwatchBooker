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
import sys
import struct
from datetime import *
from math import pi, log, sin, sqrt
from pathlib import Path
from tempfile import mkdtemp
from shutil import rmtree
from io import StringIO
from collections import OrderedDict

from PIL import Image, ImageDraw, ImageCms

import swatchbook.color as color
from swatchbook.icc import *
import swatchbook.codecs as codecs
import swatchbook.websvc as websvc


VERSION = "0.8"


# def decodeFilePath(path):
#     if sys.platform == 'win32':
#                 encoding = 'UTF-8'
#             else:
#                 encoding = sys.getfilesystemencoding()

#             if encoding == 'UTF-8' and isinstance(file, str):
#                 filename = os.path.splitext(os.path.basename(file))[0]
#             else:
#                 filename = os.path.splitext(os.path.basename(file))[0].decode(encoding)


class FileFormatError(Exception):
    pass


class Info():
    # Dublin Core (translatable, longtext)
    dc = {'contributor': (True, True),
          'coverage': (True, False),
          'creator': (True, False),
          'description': (True, True),
          'identifier': (False, False),
          'language': (False, False),
          'publisher': (True, False),
          'relation': (True, False),
          'rights': (True, True),
          'source': (True, False),
          'subject': (True, False),
          'title': (True, False),
          # DCMI Metadata Terms
          'license': (False, False)}

    def __init__(self):
        self.format = 'application/swatchbook'
        self.type = 'http://purl.org/dc/dcmitype/Dataset'
        self.date = False
        for dc in self.dc:
            self.__setattr__(dc, '')
            if self.dc[dc][0]:
                self.__setattr__('%s_l10n' % dc, {})
        self.version = ''


class Book():

    def __init__(self):
        self.display = {'rows': False, 'columns': False}
        self.items = []  # Group, Swatch, Spacer, Break

    def count(self, swatchesonly=False):
        count = len(self.items)
        for e in self.items:
            if isinstance(e, Group):
                count += e.count(swatchesonly)
            if swatchesonly and not isinstance(e, Swatch):
                count -= 1
        return count


class SwatchBook():

    def __init__(self, file: Path = None, codec=None, websvc_name=None, webid=None):
        self.tmpdir = Path(mkdtemp())
        self.info = Info()
        self.profiles = {}
        self.materials = {}
        self.book = Book()
        self.codec = None

        if file:
            self.read(file, codec)
        elif websvc_name:
            self.webread(websvc_name, webid)

    def __del__(self):
        rmtree(self.tmpdir)

    def test(self, file: Path, codec=None):
        # test 1: codec
        test = False
        if codec:
            try:
                test = getattr(codecs, codec).test(file)
            except (IOError, SyntaxError, struct.error):
                codec = None
            if test:
                return codec

        # test 2: extension
        ext = file.suffix.lower()
        if ext in codecs.readexts:
            for codec in codecs.readexts[ext]:
                test = False
                try:
                    test = getattr(codecs, codec).test(file)
                except (IOError, SyntaxError, struct.error):
                    pass
                if test:
                    return codec
            else:
                codec = None

        # test 3: free
        for codec in codecs.reads:
            test = False
            try:
                test = getattr(codecs, codec).test(file)
            except (IOError, SyntaxError, struct.error):
                pass
            if test:
                return codec
        else:
            codec = None
        return codec

    def webread(self, websvc_name, webid):
        svc = getattr(websvc, websvc_name)()
        svc.read(self, webid)

    def read(self, file: Path, codec):
        codec = self.test(file, codec)
        if codec:
            self.codec = codec
            getattr(codecs, codec).read(self, file)
            if not self.info.title:
                self.info.title = file.name.replace('_', ' ')
        else:
            raise FileFormatError()

    def write(self, fmt, output: Path = None):
        if fmt in codecs.writes:
            codec = getattr(codecs, fmt)
            if output is None:
                print(codec.write(self))
            else:
                content = codec.write(self)
                # TODO: check if writable
                with open(output, 'w') as bookfile:
                    bookfile.write(content)
        else:
            raise FileFormatError('unsupported output format')


class Group():
    def __init__(self, title='', parent=None):
        self.info = Info()
        self.info.title = title
        self.items = []

    def count(self, swatchesonly=False):
        count = len(self.items)
        for e in self.items:
            if isinstance(e, Group):
                count += e.count(swatchesonly)
            if swatchesonly and not isinstance(e, Swatch):
                count -= 1
        return count


class Swatch():
    def __init__(self, material, parent=None):
        self.material = material


class Spacer():
    def __init__(self, parent=None):
        pass


class Break():
    def __init__(self, parent=None):
        pass


class Color():
    """
    Output values.

    sRGB,RGB,HSV,HSL,CMY,CMYK,nCLR: 0 -> 1
    YIQ: Y 0 -> 1 : IQ -0.5 -> 0.5
    Lab: L 0 -> 100 : ab -128 -> 127
    LCH: LC 0 -> 100 : H 0 -> 360
    XYZ: 0 -> ~100 (cfr. ref)
    xyZ: xy 0 -> 1 : Y 0 -> 100
    """

    def __init__(self, swatchbook):
        self.info = Info()
        self.values = OrderedDict()
        self.usage = set()
        self.extra = {}
        self.swatchbook = swatchbook

    def toRGB(self, prof_out=False):
        if not prof_out and ('sRGB', False) in self.values:
            return self.values[('sRGB', False)]
        else:
            for key in self.values:
                if key[1]:
                    prof_in = self.swatchbook.profiles[key[1]].uri
                else:
                    prof_in = False
                if color.toRGB(key[0], self.values[key], prof_in, prof_out):
                    return color.toRGB(key[0], self.values[key], prof_in, prof_out)
                    break
            else:
                return False

    def toRGB8(self, prof_out=False):
        RGB = self.toRGB(prof_out)
        if RGB:
            R, G, B = RGB
            return (int(round(R * 0xFF)), int(round(G * 0xFF)), int(round(B * 0xFF)))
        else:
            return False


class Tint():
    def __init__(self):
        self.info = Info()
        self.color = False
        self.amount = False  # 1 = color, 0 = white
        self.usage = []      # for compatibility with colors
        self.extra = {}

    def toRGB(self, prof_out=False):
        R, G, B = self.color.toRGB(prof_out)
        H, S, L = color.RGB2HSL(R, G, B)
        L = L + (1 - L) * (1 - self.amount)
        return color.HSL2RGB(H, S, L)

    def toRGB8(self, prof_out=False):
        RGB = self.toRGB(prof_out)
        if RGB:
            R, G, B = RGB
            return (int(round(R * 0xFF)), int(round(G * 0xFF)), int(round(B * 0xFF)))
        else:
            return False


class Tone():
    def __init__(self):
        self.info = Info()
        self.color = False
        self.amount = False  # 1 = color, 0 = gray
        self.usage = []      # for compatibility with colors
        self.extra = {}

    def toRGB(self, prof_out=False):
        R, G, B = self.color.toRGB(prof_out)
        H, S, L = color.RGB2HSL(R, G, B)
        S = S * self.amount
        L = L * 0.5 * self.amount
        return color.HSL2RGB(H, S, L)

    def toRGB8(self, prof_out=False):
        RGB = self.toRGB(prof_out)
        if RGB:
            R, G, B = RGB
            return (int(round(R * 0xFF)), int(round(G * 0xFF)), int(round(B * 0xFF)))
        else:
            return False


class Shade():
    def __init__(self):
        self.info = Info()
        self.color = False
        self.amount = False  # 1 = color, 0 = black
        self.usage = []      # for compatibility with colors
        self.extra = {}

    def toRGB(self, prof_out=False):
        R, G, B = self.color.toRGB(prof_out)
        H, S, L = color.RGB2HSL(R, G, B)
        L = L * self.amount
        return color.HSL2RGB(H, S, L)

    def toRGB8(self, prof_out=False):
        RGB = self.toRGB(prof_out)
        if RGB:
            R, G, B = RGB
            return (int(round(R * 0xFF)), int(round(G * 0xFF)), int(round(B * 0xFF)))
        else:
            return False


class Pattern():
    def __init__(self, swatchbook):
        self.info = Info()
        self.extra = {}
        self.swatchbook = swatchbook

    def indexed(self):
        if self.image().palette():
            return True
        else:
            return False

    #TODO: SVG support
    def image(self):
        try:
            image = Image.open(self.swatchbook.tmpdir / 'patterns' / self.info.identifier)
            image.load()
            return image
        except (IOError, TypeError):
            return False

    def imageRGB(self, prof_out=False):
        image = self.image()
        alpha_band = False

        if image.mode in ('LA', 'PA', 'RGBA'):
            bands = image.split()
            alpha_band = bands[-1]
            image = Image.merge(image.mode[:-1], bands[:-1])
        sRGB = ImageCms.createProfile('sRGB')

        if 'icc_profile' in image.info:
            inputProfile = ImageCms.ImageCmsProfile(StringIO(image.info['icc_profile']))
        else:
            if image.mode == 'CMYK':
                inputProfile = color.dirpath(__file__) / 'Fogra27L.icm'
            elif image.mode == 'LAB':
                inputProfile = ImageCms.createProfile('LAB')
            else:
                image = image.convert('RGB')
                inputProfile = sRGB

        if prof_out:
            outputProfile = prof_out
        else:
            outputProfile = sRGB
        new_image = ImageCms.profileToProfile(image, inputProfile, outputProfile, outputMode='RGB')

        if not alpha_band:
            alpha_band = Image.new('L', image.size, 255)
        new_image.putalpha(alpha_band)

        return new_image

    # to be called before deleting a pattern from the book
    def deleteFile(self):
        (self.swatchbook.tmpdir / 'patterns' / self.info.identifier).unlink()


class Gradient():
    def __init__(self, swatchbook):
        self.info = Info()
        self.colorstops = []
        self.opacitystops = []
        self.extra = {}
        self.swatchbook = swatchbook

    @staticmethod
    def linear(position, midpoint):
        if position <= midpoint:
            return 0.5 * position / midpoint
        else:
            position -= midpoint
            midpoint = 1.0 - midpoint
            return 0.5 + 0.5 * position / midpoint

    @staticmethod
    def get_factor(interpolation, position, midpoint):
        if interpolation == 'curved':
            return pow(position, log(0.5) / log(midpoint))
        if interpolation == 'sine':
            return (sin((-pi / 2.0) + pi * Gradient.linear(position, midpoint)) + 1.0) / 2.0
        if interpolation == 'sphere_increasing':
            return sqrt(1.0 - (Gradient.linear(position, midpoint) - 1.0) * (Gradient.linear(position, midpoint) - 1.0))
        if interpolation == 'sphere_decreasing':
            return 1.0 - sqrt(1.0 - Gradient.linear(position, midpoint) * Gradient.linear(position, midpoint))
        return Gradient.linear(position, midpoint)

    @staticmethod
    def interpolate(srgb1, srgb2, factor, model, args):
        r1, g1, b1 = srgb1
        r2, g2, b2 = srgb2
        if model == 'HSV':
            left_hsv = color.RGB2HSV(r1, g1, b1)
            right_hsv = color.RGB2HSV(r2, g2, b2)
            s = left_hsv[1] + (right_hsv[1] - left_hsv[1]) * factor
            v = left_hsv[2] + (right_hsv[2] - left_hsv[2]) * factor

            if 'direction' in args:
                if args['direction'] == 'CW':
                    if right_hsv[0] < left_hsv[0]:
                        h = left_hsv[0] - (left_hsv[0] - right_hsv[0]) * factor
                    else:
                        h = left_hsv[0] - (1.0 - (right_hsv[0] - left_hsv[0])) * factor
                    if h < 0.0:
                        h += 1.0
                elif args['direction'] == 'CCW':
                    if left_hsv[0] < right_hsv[0]:
                        h = left_hsv[0] + (right_hsv[0] - left_hsv[0]) * factor
                    else:
                        h = left_hsv[0] + (1.0 - (left_hsv[0] - right_hsv[0])) * factor
                    if (h > 1.0):
                        h -= 1.0
                else:
                    h = left_hsv[0] + (right_hsv[0] - left_hsv[0]) * factor
            r, g, b = color.HSV2RGB(h, s, v)
        else:
            r = r1 + (r2 - r1) * factor
            g = g1 + (g2 - g1) * factor
            b = b1 + (b2 - b1) * factor

        if 'gamma' in args:
            r = pow(r, args['gamma'])
            g = pow(g, args['gamma'])
            b = pow(b, args['gamma'])

        return (r, g, b)

    def colorAt(self, pos, prof_out=False):
        if len(self.colorstops) == 0:
            return False
        left = 0
        right = len(self.colorstops) - 1
        for i, stop in enumerate(self.colorstops):
            if pos >= stop.position:
                left = i
            else:
                right = i
                break
        if left == right:
            return self.swatchbook.materials[self.colorstops[left].color].toRGB(prof_out)
        seg_pos = (pos - self.colorstops[left].position) / (self.colorstops[right].position - self.colorstops[left].position)

        if 'midpoint' in self.colorstops[left].args:
            midpoint = self.colorstops[left].args['midpoint']
        else:
            midpoint = 0.5

        factor = Gradient.get_factor(self.colorstops[left].interpolation, seg_pos, midpoint)

        srgb1 = self.swatchbook.materials[self.colorstops[left].color].toRGB(prof_out) or (128, 128, 128)
        srgb2 = self.swatchbook.materials[self.colorstops[right].color].toRGB(prof_out) or (128, 128, 128)
        return Gradient.interpolate(srgb1, srgb2, factor, self.colorstops[left].model, self.colorstops[left].args)

    def alphaAt(self, pos):
        if len(self.opacitystops) == 0:
            return 1
        left = 0
        right = len(self.opacitystops) - 1
        for i, stop in enumerate(self.opacitystops):
            if pos >= stop.position:
                left = i
            else:
                right = i
                break

        if left == right:
            return self.opacitystops[left].opacity

        seg_pos = (pos - self.opacitystops[left].position) / (self.opacitystops[right].position - self.opacitystops[left].position)

        if 'midpoint' in self.opacitystops[left].args:
            midpoint = self.opacitystops[left].args['midpoint']
        else:
            midpoint = 0.5

        factor = Gradient.get_factor(self.opacitystops[left].interpolation, seg_pos, midpoint)

        return self.opacitystops[left].opacity + (self.opacitystops[right].opacity - self.opacitystops[left].opacity) * factor

    def imageRGB(self, width, height, prof_out=False):
        if len(self.colorstops) == 0:
            return False
        colors = set()
        for stop in self.colorstops:
            colors.add(stop.color)
        sRGB_colors = {}
        for col in colors:
            if col:
                sRGB_colors[col] = self.swatchbook.materials[col].toRGB(prof_out) or (128, 128, 128)
        # Color
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        for i in range(width):
            pos = i / width
            left = 0
            right = len(self.colorstops) - 1
            for j, stop in enumerate(self.colorstops):
                if pos >= stop.position:
                    left = j
                else:
                    right = j
                    break
            sRGB_left = sRGB_colors[self.colorstops[left].color] if self.colorstops[left].color else (128, 128, 128)
            sRGB_right = sRGB_colors[self.colorstops[right].color] if self.colorstops[right].color else (128, 128, 128)
            if left == right or self.colorstops[left].color == self.colorstops[right].color:
                r, g, b = sRGB_left
            else:
                seg_pos = (pos - self.colorstops[left].position) / (self.colorstops[right].position - self.colorstops[left].position)

                if 'midpoint' in self.colorstops[left].args:
                    midpoint = self.colorstops[left].args['midpoint']
                else:
                    midpoint = 0.5
                factor = Gradient.get_factor(self.colorstops[left].interpolation, seg_pos, midpoint)

                r, g, b = Gradient.interpolate(sRGB_left, sRGB_right, factor, self.colorstops[left].model, self.colorstops[left].args)

            draw.line((i, 0, i, height), fill=(int(round(r * 0xFF)), int(round(g * 0xFF)), int(round(b * 0xFF))))
        del draw

        sRGB = ImageCms.createProfile('sRGB')
        if prof_out:
            new_image = ImageCms.profileToProfile(image, sRGB, prof_out)
        else:
            new_image = image

        # Opacity
        alpha = Image.new('L', (width, height), 255)
        if len(self.opacitystops) > 0:
            draw = ImageDraw.Draw(alpha)
            for i in range(width):
                try:
                    a = self.alphaAt(float(i) / width)
                except TypeError:
                    a = 1
                draw.line((i, 0, i, image.size[1]), fill=int(round(a * 0xFF)))
            del draw
        new_image.putalpha(alpha)
        return new_image


class ColorStop():
    def __init__(self):
        self.position = False
        self.color = False
        self.interpolation = False
        self.model = False
        self.args = {}


class OpacityStop():
    def __init__(self):
        self.position = False
        self.opacity = False
        self.interpolation = False
        self.args = {}
