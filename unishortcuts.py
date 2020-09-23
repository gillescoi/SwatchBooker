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

Provides the build_shortcuts and the install_shortcuts class,
two subclass of the Command class in the distutils.command package.
Also provides a Shortcut class for passing metadata to build_shortcuts
for shortcuts creation.
Shortcuts will be built only for gui script declared in 'entry_points'
argument of the setup() function. WARNING: 'entry_points' is an addition
of the Setuptools package, so the latest is required.
"""

import os
import sys
import re
from pathlib import Path
from distutils.core import Command
from distutils.command.build import build
from distutils.command.install import install

__ALL__ = ['build', 'build_shortcuts', 'Shortcut']


def _get_platform():
    if sys.platform == 'darwin':
        return 'darwin'
    if os.name == 'nt' or sys.platform.startswith('win'):
        return 'win'
    if sys.platform.startswith('linux'):
        return 'linux'


_here = Path.cwd()


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
    icons:        Icons path relative to the setup script. Defaults to None.
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
    mime_types:   A list of strings for MIME type(s) supported by
                  this application. Defaults to None.
    """

    _instances = set()

    def __new__(cls, script, name=None, generic_name=None, description=None,
                icons=None, arguments=None, special_arg=None, category=None,
                keywords=None, mime_types=None):
        instance = super(Shortcut, cls).__new__(cls)
        cls.__init__(instance, script, name, generic_name, description, icons,
                     arguments, special_arg, category, keywords, mime_types)
        cls._instances.add(instance)
        return instance

    def __init__(self, script, name=None, generic_name=None, description=None,
                 icons=None, arguments=None, special_arg=None, category=None,
                 keywords=None, mime_types=None):
        self.script = script
        self.name = name
        self.generic_name = generic_name
        self.description = description
        self.icons = icons
        self.arguments = arguments
        self.special_arg = special_arg
        self.category = category
        self.keywords = keywords
        self.mime_types = mime_types

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
    def icons(self):
        return self._icons

    @icons.setter
    def icons(self, s):
        if isinstance(s, list):
            self._icons = [Path(i) for i in s]
        else:
            self._icons = [Path(s)] if s else []
        for i in self._icons:
            if not i.resolve().relative_to(_here):
                raise(AttributeError('icon %s path outside of distribution\'s directory' % i))

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
        for k in self._keywords:
            if k == '':
                self._keywords.remove('')

    @property
    def mime_types(self):
        return self._mime_types

    @mime_types.setter
    def mime_types(self, s):
        if isinstance(s, list):
            self._mime_types = [str(i) for i in s]
        elif isinstance(s, str):
            self._mime_types = re.split(r',\s*|\s+', s)
        elif s is None:
            self._mime_types = []
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
                    ('plat-name=', 'p',
                     'platform name to build for, if supported, (default: %s)'
                     % _get_platform())
                    ]

    def initialize_options(self):
        """Set default values for options."""
        self.build_base = None
        self.build_desktop = None
        self.outfiles = None
        self.plat_name = None

    def finalize_options(self):
        """Post-process options."""
        self.set_undefined_options('build',
                                   ('build_base', 'build_base'),
                                   ('plat_name', 'plat_name')
                                   )
        self.build_desktop = Path(self.build_base) / 'desktop'
        self.outfiles = []
        # is this really a good thing to do
        self.distribution.cmdclass['install_shortcuts'] = install_shortcuts

    def run(self):
        """Run command."""
        # look for enrty_points
        # TODO: change to gui scripts after testing
        group = 'console_scripts'
        if hasattr(self.distribution, 'entry_points') and group in self.distribution.entry_points:
            for ep in self.distribution.entry_points[group]:
                shortcut = self._get_metadatas(ep.split('=')[0].strip())
                self._make_linux_shortcut(shortcut)
        else:
            self.warn('no entry_points found, nothings to do.')

    def get_outputs(self):
        return self.outfiles

    def _make_linux_icons(self, shortcut):
        base_dir_icons = self.build_desktop / 'icons'
        for icon in shortcut.icons:
            pass
        if not self.dry_run:
            # directory.mkdir(mode=0o777, parents=True, exist_ok=True)
            pass

    def _make_linux_shortcut(self, shortcut):
        # TODO: desktop locale
        lines = ['[Desktop Entry]', 'Version=1.1', 'Encoding=UTF-8', 'Type=Application']
        lines.append('Name=%s' % shortcut.name)
        if shortcut.generic_name:
            lines.append('GenericName=%s' % shortcut.generic_name)
        if shortcut.description:
            lines.append('Comment=%s' % shortcut.description)
        if shortcut.category:
            lines.append('Categories=%s' % shortcut.category)
        if shortcut.keywords:
            lines.append('Keywords=%s' % ';'.join(shortcut.keywords))
        if shortcut.icons:
            lines.append('Icon=%s' % Path(shortcut.icons[0]).stem)
        else:
            # TODO: What if none
            pass
        lines.append('Exec=%s %s %s' % (shortcut.script,
                                        ' '.join(shortcut.arguments),
                                        shortcut.special_arg))
        lines.append('TryExec=%s' % shortcut.script)
        lines.append('Terminal=false')
        if shortcut.mime_types:
            lines.append('MimeType=%s' % ';'.join(shortcut.mime_types))

        directory = self.build_desktop / 'applications'
        file = directory / Path(shortcut.name).with_suffix('.desktop')
        if not self.dry_run:
            directory.mkdir(mode=0o777, parents=True, exist_ok=True)
            self.execute(self._write_file, (file, lines, 'UTF-8'),
                         msg='creating %s' % str(file))
        self.outfiles.append(str(file))

    def _write_file(self, file, sequence, encoding=None):
        with file.open('w', encoding=encoding) as f:
            for line in sequence:
                f.write(line + "\n")

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
        # TODO: follow this mechanisme
        # icons
        if not shortcut.icons:
            data = _here / 'data'
            if data.is_dir():
                icons = data.glob('%s.*' % shortcut.name)
                icons = [icon for icon in icons if icon.suffix in _ICON_EXT[_get_platform()]]
                shortcut.icons = icons
            else:
                shortcut.icons = None
        else:
            for ic in shortcut.icons:
                if not ic.exists():
                    shortcut.icons.remove(ic)
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


class install_shortcuts(Command):
    """Setuptools command install_shortcuts."""

    description = "install desktop shortcuts"

    user_options = [
        ('install-dir=', 'd', "directory to install shortcus to"),
        ('build-dir=', 'b', "build directory (where to install from)"),
        ('root=', None, "install everything relative to this alternate root directory"),
        ('force', 'f', "force installation (overwrite existing files)"),
        ('skip-build', None, "skip the build steps"),
    ]

    boolean_options = ['force', 'skip-build']

    def initialize_options(self):
        self.install_dir = None
        self.build_dir = None
        self.root = None
        self.force = 0
        self.skip_build = None
        self.outfiles = None

    def finalize_options(self):
        self.set_undefined_options('build_shortcuts', ('build_desktop', 'build_dir'))
        self.set_undefined_options('install',
                                   ('install_data', 'install_dir'),
                                   ('root', 'root'),
                                   ('force', 'force'),
                                   ('skip_build', 'skip_build'),
                                   )
        self.outfiles = []

    def run(self):
        self.mkpath(self.install_dir)

    def get_inputs(self):
        return self.data_files or []

    def get_outputs(self):
        return self.outfiles


# Append our build command to the end of build sub_commands
install.sub_commands.append(('install_shortcuts', None))
