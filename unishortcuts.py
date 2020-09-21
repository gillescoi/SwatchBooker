#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#       Copyright (c) Gilles Coissac 2020 <info@gillescoissac.fr>
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
"""unishortcuts

Provides the build_shortcuts class, a subclass of the Command class
in the distutils.command package. Also provides a Shortcut class for
passing metadata to build_shortcuts for shortcuts creation.
"""
import os
import sys
import re
from pathlib import Path
from distutils.core import Command
from distutils.command.build import build


__ALL__ = ['build', 'build_shortcuts', 'Shortcut']


def _get_platform():
    if sys.platform == 'darwin':
        return 'darwin'
    if os.name == 'nt' or sys.platform.startswith('win'):
        return 'win'
    if sys.platform.startswith('linux'):
        return 'linux'


_here = Path(__file__).parent.resolve()

_LINUX_DESKTOP_FORM = """[Desktop Entry]
Version=1.1
Encoding=UTF-8
Name={name:s}
GenericName={gname:s}
Type=Application
Comment={desc:s}
Categories={cat:s}
Keywords={keys:s}
Icon={icon:s}
Exec={script:s} {args:s}
TryExec={script:s}
Terminal={term:s}
"""

_FREE_DESKTOP_CATEGORIES = ['AudioVideo', 'Audio', 'Video', 'Development',
                            'Education', 'Game', 'Graphics', 'Network',
                            'Office', 'Settings', 'System', 'Utility']

# A command line may contain at most one %f, %u, %F or %U field code.
# If the application should not open any file the %f, %u, %F and %U
# field codes must be removed from the command line and ignored.
_LINUX_SPECIAL_ARGS = {'SINGLE_FILE': '%f', 'FILES_LIST': '%F',
                       'SINGLE_URL': '%u', 'URLS_LIST': '%U'}

_ICON_EXT = {'linux': ('ico', 'svg', 'png'), 'win': ('ico',), 'darwin': ('icns',)}


class Shortcut():
    """A representation of a Shortcut parameters and metadata.

    Depending of the OS dependent nature of shortcut to be created,
    not all the arguments will be pertinent, eg: Windows have no category
    classifiers for its shortcuts. This Class is modeled around the more
    complete scheme .desktop file of Linux system defined by the Free
    Desktop Organization.

    Arguments:
    ---------
    script:       script to run, should be identique as one declared
                  in "entry_points['gui_scripts']" arguments of the setup()
                  function.
    name:         name for shortcut ("None" to use name of script file).
                  Defaults to None.
    generic_name: A more descriptive name. Defaults to None.
    description:  Longer string for description. Defaults to None.
    icon:         Icon path relative to the setup script. Defaults to None.
    arguments:    List of arguments for script execution. Could be a list
                  of string or a concatened string of arguments.
                  Defaults to None.
    special_args: For Linux platform, one of string'SINGLE_FILE',
                  'FILES_LIST', 'SINGLE_URL' or 'URLS_LIST'. Defaults to None.
    categories:   A string to classify the app. Should be one
                  of The Free Desktop cateories : ['AudioVideo', 'Audio',
                  'Video', 'Development', 'Education', 'Game', 'Graphics',
                  'Network', 'Office', 'Settings', 'System', 'Utility'].
                  Defaults to None.
    keywords:     A list of strings which may be used in addition to other
                  metadata to describe this entry. Defaults to None.
    mime_type:    The MIME type(s) supported by this application. Defaults to None.
    """

    _instances = set()

    def __new__(cls, script, name=None, generic_name=None, description=None,
                icon=None, arguments=None, special_arg=None, category=None,
                keywords=None, mime_type=None):
        instance = super(Shortcut, cls).__new__(cls)
        cls.__init__(instance, script, name, generic_name, description, icon,
                     arguments, special_arg, category, keywords, mime_type)
        cls._instances.add(instance)
        return instance

    def __init__(self, script, name=None, generic_name=None, description=None,
                 icon=None, arguments=None, special_arg=None, category=None,
                 keywords=None, mime_type=None):
        self.script = script
        self.name = name
        self.generic_name = generic_name
        self.description = description
        self.icon = icon
        self.arguments = arguments
        self.special_arg = special_arg
        self.category = category
        self.keywords = keywords
        self.mime_type = mime_type

    @property
    def script(self):
        return self._script

    @script.setter
    def script(self, s):
        self._script = str(s) if s else ''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, s):
        self._name = str(s) if s else ''

    @property
    def generic_name(self):
        return self._generic_name

    @generic_name.setter
    def generic_name(self, s):
        self._generic_name = str(s) if s else ''

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, s):
        self._description = str(s) if s else ''

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, s):
        if isinstance(s, list):
            self._icon = [Path(i) for i in s]
        else:
            self._icon = [Path(s)] if s else []
        for i in self._icon:
            if i.root != _here:
                raise(AttributeError('icon %s path not inside source directory' % i))

    @property
    def arguments(self):
        return self._arguments

    @arguments.setter
    def arguments(self, s):
        if isinstance(s, list):
            self._arguments = [str(i) for i in s]
        elif isinstance(s, str):
            self._arguments = re.split(r',\s*|\s+', s)
        elif s is None:
            self._arguments = []
        else:
            raise(TypeError())

    @property
    def special_arg(self):
        return self._special_arg

    @special_arg.setter
    def special_arg(self, s):
        if s in _LINUX_SPECIAL_ARGS:
            self._special_arg = s
        elif s is None:
            self._special_arg = ''
        else:
            raise(TypeError('Wrong type for %s' % s))

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, s):
        if s in _FREE_DESKTOP_CATEGORIES:
            self._category = s
        elif s is None:
            self._category = ''
        else:
            raise(TypeError('Arguments should be one of %s' % _FREE_DESKTOP_CATEGORIES))

    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, s):
        if isinstance(s, list):
            self._keywords = [str(i) for i in s]
        elif isinstance(s, str):
            self._keywords = re.split(r',\s*|\s+', s)
        elif s is None:
            self._keywords = []
        else:
            raise(TypeError())

    @property
    def mime_type(self):
        return self._mime_type

    @mime_type.setter
    def mime_type(self, s):
        if isinstance(s, list):
            self._mime_type = [str(i) for i in s]
        elif isinstance(s, str):
            self._mime_type = re.split(r',\s*|\s+', s)
        elif s is None:
            self._mime_type = []
        else:
            raise(TypeError())

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.name == self.name
        return False

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return 'Shortcut %s for script %s' % (self.name, self.script)


class build_shortcuts(Command):
    """Setuptools command build_shortcuts."""

    command_name = 'build_shortcuts'
    description = 'build_shortcuts'
    user_options = [('build-base=', None, 'directory to "build" (copy) to'),
                    ('desktop=', None, 'path to Pylint config file')]

    def initialize_options(self):
        """Set default values for options."""
        self.build_base = None
        self.desktop = None

    def finalize_options(self):
        """Post-process options."""
        if self.desktop:
            pass
        self.set_undefined_options('build', ('build_base', 'build_base'))

    def run(self):
        """Run command."""
        # look for enrty_points
        group = 'console_scripts'
        if hasattr(self.distribution, 'entry_points') and group in self.distribution.entry_points:
            for ep in self.distribution.entry_points[group]:
                shortcut = self._get_metadatas(ep.split('=')[0].strip())

                # _LINUX_DESKTOP_FORM.format(name=name, desc=desc,
        #                            exe=executable, icon=scut.icon,
        #                            script=scut.full_script, args=scut.arguments,
        #                            term='true' if terminal else 'false')
        else:
            self.warn('no entry_points found')
        self.warn(self.distribution.metadata.get_classifiers())

    def _get_metadatas(self, script):
        # If user didn't created a Shortcut object,
        # try to guess obvious metadata from the distribution.
        shortcut = Shortcut(script)
        for s in Shortcut._instances:
            if s.script == script:
                shortcut = s
                break
        # name
        if not shortcut.name:
            shortcut.name = shortcut.script
        # generic_name
        if not shortcut.generic_name:
            shortcut.generic_name = shortcut.name
        # icon
        if not shortcut.icon:
            data = _here / 'data'
            if data.is_dir():
                icons = data.glob('%s.*' % shortcut.name)
                icons = [icon for icon in icons if icon.suffix in _ICON_EXT[_get_platform()]]
                shortcut.icon = icons
            else:
                shortcut.icon = None
        else:
            for ic in shortcut.icon:
                if not ic.exists():
                    shortcut.icon.remove(ic)
        # description
        if not shortcut.description:
            shortcut.description = self.distribution.metadata.get_description()

        # category
        if not shortcut.category:
            for cf in self.distribution.metadata.get_classifiers():
                cf = [c.strip() for c in cf.split('::')]
                if cf[0] == 'Topic':
                    for c in cf:
                        if c in _FREE_DESKTOP_CATEGORIES:
                            shortcut.category = c
                            break

        # keywords
        if not shortcut.keywords:
            shortcut.keywords = self.distribution.metadata.get_keywords()

        return shortcut


# Append our build command to the end of build sub_commands
build.sub_commands.append(('build_shortcuts', None))


# if _get_platform() == 'linux':
#     home = Path.home()
#     ud = home / '.config' / 'user-dirs.dirs'
#     if ud.exists():
#         with open(ud, 'r') as f:
#             for l in f.readlines():
#                 if 'DESKTOP' in l:
#                     desktop = l.split('=')[1].strip('"\'').split('/')[1]
#                     break
# if desktop:
#     desktop = home / desktop
# else:
#     desktop = home / 'Desktop'
# startmenu =