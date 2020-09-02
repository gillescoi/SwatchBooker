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
import os
import sys
import argparse
from pathlib import Path

import swatchbook as swbk
from swatchbook import _version
import swatchbook.codecs as codecs
import swatchbook.websvc as websvc


__version__ = _version.__version__


def main():
    # Argumentss Parser
    parser = argparse.ArgumentParser(description='Swatch conversion utilities')
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-o', '--output', dest='out_fmt', metavar='FORMAT', required=True, help='output format', choices=codecs.writes)
    group.add_argument('-w', '--websvc', dest='websvc', help='web service', choices=websvc.members.keys())
    group.add_argument('-i', '--input', dest='in_fmt', metavar='FORMAT', help='input format', choices=codecs.reads)
    parser.add_argument('-d', '--dir', dest='directory', metavar='DIRECTORY', default='', help='output directory')
    parser.add_argument('-v', '--version', action='version', version='%s %s' % (sys.argv[0], __version__))
    parser.add_argument('file_in', dest='file_in', metavar='FILE1', help='input file')
    parser.add_argument('file_out', dest='file_out', nargs='?', metavar='FILE2', default=None, help='output file')
    args = parser.parse_args()

    # From file or weebscv ?
    if args.websvc:
        print('Converting palette %s' % args.file_in)
        try:
            sb = swbk.SwatchBook(websvc_name=args.websvc, webid=args.file_in)
        except (IndexError, ValueError):
            sys.stderr.write(': invalid palette id:%s\n' % args.file_in)
    else:
        file_in = Path(args.file_in)
        print('Converting file %s' % os.fspath(file_in))
        try:
            sb = swbk.SwatchBook(file_in, args.in_fmt)
        except swbk.FileFormatError:
            sys.stderr.write('Unknown file format: %s\n' % os.fspath(file_in))

    # Exported file path
    if args.file_out is None:
        file_out = Path(file_in).parent / Path(file_in).stem
    else:
        file_out = Path(args.file_out)

    if not file_out.suffix:
        file_out = file_out.with_suffix(getattr(codecs, args.out_fmt).ext[0])

    # Directory to save exported file
    if args.directory:
        directory = Path(args.directory)
    else:
        directory = file_out.parent
    file_out = file_out.name
    try:
        directory = directory.resolve(strict=True)
    except (FileNotFoundError, RuntimeError):
        parser.error('Directory %s do not exist.' % os.fspath(directory))

    # If file out exists
    skip = False
    while (directory / file_out).exists():
        wtd = input('%s exists. [O]verwrite, [S]kip or [R]ename? ' % file_out)
        if wtd.lower() == 'o':
            break
        if wtd.lower() == 'r':
            file_out = Path(input('New file name: '))
            file_out = file_out.name
        elif wtd.lower() == "s":
            skip = True
            break

    # Export
    if not skip:
        try:
            sb.write(args.out_fmt, directory / file_out)
        except IOError as e:
            parser.error(e)


if __name__ == "__main__":
    main()
