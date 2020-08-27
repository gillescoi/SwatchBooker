r"""Wrapper for lcms2.h

Generated with:
/usr/local/bin/ctypesgen -llcms2 /usr/include/lcms2.h /usr/include/lcms2_plugin.h --output-language=py32 -o lcms2.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["lcms2"] = load_library("lcms2")

# 1 libraries
# End libraries

# No modules

__off_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 150

__off64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 151

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 49
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE# /usr/include/x86_64-linux-gnu/bits/types/FILE.h: 7

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 36
class struct__IO_marker(Structure):
    pass

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 37
class struct__IO_codecvt(Structure):
    pass

# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 38
class struct__IO_wide_data(Structure):
    pass

_IO_lock_t = None# /usr/include/x86_64-linux-gnu/bits/types/struct_FILE.h: 43

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '_codecvt',
    '_wide_data',
    '_freeres_list',
    '_freeres_buf',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * int(1)),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('_codecvt', POINTER(struct__IO_codecvt)),
    ('_wide_data', POINTER(struct__IO_wide_data)),
    ('_freeres_list', POINTER(struct__IO_FILE)),
    ('_freeres_buf', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * int((((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t)))),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_tm.h: 7
class struct_tm(Structure):
    pass

struct_tm.__slots__ = [
    'tm_sec',
    'tm_min',
    'tm_hour',
    'tm_mday',
    'tm_mon',
    'tm_year',
    'tm_wday',
    'tm_yday',
    'tm_isdst',
    'tm_gmtoff',
    'tm_zone',
]
struct_tm._fields_ = [
    ('tm_sec', c_int),
    ('tm_min', c_int),
    ('tm_hour', c_int),
    ('tm_mday', c_int),
    ('tm_mon', c_int),
    ('tm_year', c_int),
    ('tm_wday', c_int),
    ('tm_yday', c_int),
    ('tm_isdst', c_int),
    ('tm_gmtoff', c_long),
    ('tm_zone', String),
]

cmsUInt8Number = c_ubyte# /usr/include/lcms2.h: 87

cmsInt8Number = c_char# /usr/include/lcms2.h: 88

cmsFloat32Number = c_float# /usr/include/lcms2.h: 95

cmsFloat64Number = c_double# /usr/include/lcms2.h: 96

cmsUInt16Number = c_ushort# /usr/include/lcms2.h: 100

cmsInt16Number = c_short# /usr/include/lcms2.h: 108

cmsUInt32Number = c_uint# /usr/include/lcms2.h: 117

cmsInt32Number = c_int# /usr/include/lcms2.h: 125

cmsUInt64Number = c_ulong# /usr/include/lcms2.h: 135

cmsInt64Number = c_long# /usr/include/lcms2.h: 142

cmsSignature = cmsUInt32Number# /usr/include/lcms2.h: 158

cmsU8Fixed8Number = cmsUInt16Number# /usr/include/lcms2.h: 159

cmsS15Fixed16Number = cmsInt32Number# /usr/include/lcms2.h: 160

cmsU16Fixed16Number = cmsUInt32Number# /usr/include/lcms2.h: 161

cmsBool = c_int# /usr/include/lcms2.h: 164

enum_anon_5 = c_int# /usr/include/lcms2.h: 320

cmsSigChromaticityType = 1667789421# /usr/include/lcms2.h: 320

cmsSigColorantOrderType = 1668051567# /usr/include/lcms2.h: 320

cmsSigColorantTableType = 1668051572# /usr/include/lcms2.h: 320

cmsSigCrdInfoType = 1668441193# /usr/include/lcms2.h: 320

cmsSigCurveType = 1668641398# /usr/include/lcms2.h: 320

cmsSigDataType = 1684108385# /usr/include/lcms2.h: 320

cmsSigDictType = 1684628340# /usr/include/lcms2.h: 320

cmsSigDateTimeType = 1685350765# /usr/include/lcms2.h: 320

cmsSigDeviceSettingsType = 1684371059# /usr/include/lcms2.h: 320

cmsSigLut16Type = 1835430962# /usr/include/lcms2.h: 320

cmsSigLut8Type = 1835430961# /usr/include/lcms2.h: 320

cmsSigLutAtoBType = 1832993312# /usr/include/lcms2.h: 320

cmsSigLutBtoAType = 1833058592# /usr/include/lcms2.h: 320

cmsSigMeasurementType = 1835360627# /usr/include/lcms2.h: 320

cmsSigMultiLocalizedUnicodeType = 1835824483# /usr/include/lcms2.h: 320

cmsSigMultiProcessElementType = 1836082548# /usr/include/lcms2.h: 320

cmsSigNamedColorType = 1852010348# /usr/include/lcms2.h: 320

cmsSigNamedColor2Type = 1852009522# /usr/include/lcms2.h: 320

cmsSigParametricCurveType = 1885434465# /usr/include/lcms2.h: 320

cmsSigProfileSequenceDescType = 1886610801# /usr/include/lcms2.h: 320

cmsSigProfileSequenceIdType = 1886611812# /usr/include/lcms2.h: 320

cmsSigResponseCurveSet16Type = 1919120178# /usr/include/lcms2.h: 320

cmsSigS15Fixed16ArrayType = 1936077618# /usr/include/lcms2.h: 320

cmsSigScreeningType = 1935897198# /usr/include/lcms2.h: 320

cmsSigSignatureType = 1936287520# /usr/include/lcms2.h: 320

cmsSigTextType = 1952807028# /usr/include/lcms2.h: 320

cmsSigTextDescriptionType = 1684370275# /usr/include/lcms2.h: 320

cmsSigU16Fixed16ArrayType = 1969632050# /usr/include/lcms2.h: 320

cmsSigUcrBgType = 1650877472# /usr/include/lcms2.h: 320

cmsSigUInt16ArrayType = 1969828150# /usr/include/lcms2.h: 320

cmsSigUInt32ArrayType = 1969828658# /usr/include/lcms2.h: 320

cmsSigUInt64ArrayType = 1969829428# /usr/include/lcms2.h: 320

cmsSigUInt8ArrayType = 1969827896# /usr/include/lcms2.h: 320

cmsSigVcgtType = 1986226036# /usr/include/lcms2.h: 320

cmsSigViewingConditionsType = 1986618743# /usr/include/lcms2.h: 320

cmsSigXYZType = 1482250784# /usr/include/lcms2.h: 320

cmsTagTypeSignature = enum_anon_5# /usr/include/lcms2.h: 320

enum_anon_6 = c_int# /usr/include/lcms2.h: 396

cmsSigAToB0Tag = 1093812784# /usr/include/lcms2.h: 396

cmsSigAToB1Tag = 1093812785# /usr/include/lcms2.h: 396

cmsSigAToB2Tag = 1093812786# /usr/include/lcms2.h: 396

cmsSigBlueColorantTag = 1649957210# /usr/include/lcms2.h: 396

cmsSigBlueMatrixColumnTag = 1649957210# /usr/include/lcms2.h: 396

cmsSigBlueTRCTag = 1649693251# /usr/include/lcms2.h: 396

cmsSigBToA0Tag = 1110589744# /usr/include/lcms2.h: 396

cmsSigBToA1Tag = 1110589745# /usr/include/lcms2.h: 396

cmsSigBToA2Tag = 1110589746# /usr/include/lcms2.h: 396

cmsSigCalibrationDateTimeTag = 1667329140# /usr/include/lcms2.h: 396

cmsSigCharTargetTag = 1952543335# /usr/include/lcms2.h: 396

cmsSigChromaticAdaptationTag = 1667785060# /usr/include/lcms2.h: 396

cmsSigChromaticityTag = 1667789421# /usr/include/lcms2.h: 396

cmsSigColorantOrderTag = 1668051567# /usr/include/lcms2.h: 396

cmsSigColorantTableTag = 1668051572# /usr/include/lcms2.h: 396

cmsSigColorantTableOutTag = 1668050804# /usr/include/lcms2.h: 396

cmsSigColorimetricIntentImageStateTag = 1667852659# /usr/include/lcms2.h: 396

cmsSigCopyrightTag = 1668313716# /usr/include/lcms2.h: 396

cmsSigCrdInfoTag = 1668441193# /usr/include/lcms2.h: 396

cmsSigDataTag = 1684108385# /usr/include/lcms2.h: 396

cmsSigDateTimeTag = 1685350765# /usr/include/lcms2.h: 396

cmsSigDeviceMfgDescTag = 1684893284# /usr/include/lcms2.h: 396

cmsSigDeviceModelDescTag = 1684890724# /usr/include/lcms2.h: 396

cmsSigDeviceSettingsTag = 1684371059# /usr/include/lcms2.h: 396

cmsSigDToB0Tag = 1144144432# /usr/include/lcms2.h: 396

cmsSigDToB1Tag = 1144144433# /usr/include/lcms2.h: 396

cmsSigDToB2Tag = 1144144434# /usr/include/lcms2.h: 396

cmsSigDToB3Tag = 1144144435# /usr/include/lcms2.h: 396

cmsSigBToD0Tag = 1110590512# /usr/include/lcms2.h: 396

cmsSigBToD1Tag = 1110590513# /usr/include/lcms2.h: 396

cmsSigBToD2Tag = 1110590514# /usr/include/lcms2.h: 396

cmsSigBToD3Tag = 1110590515# /usr/include/lcms2.h: 396

cmsSigGamutTag = 1734438260# /usr/include/lcms2.h: 396

cmsSigGrayTRCTag = 1800688195# /usr/include/lcms2.h: 396

cmsSigGreenColorantTag = 1733843290# /usr/include/lcms2.h: 396

cmsSigGreenMatrixColumnTag = 1733843290# /usr/include/lcms2.h: 396

cmsSigGreenTRCTag = 1733579331# /usr/include/lcms2.h: 396

cmsSigLuminanceTag = 1819635049# /usr/include/lcms2.h: 396

cmsSigMeasurementTag = 1835360627# /usr/include/lcms2.h: 396

cmsSigMediaBlackPointTag = 1651208308# /usr/include/lcms2.h: 396

cmsSigMediaWhitePointTag = 2004119668# /usr/include/lcms2.h: 396

cmsSigNamedColorTag = 1852010348# /usr/include/lcms2.h: 396

cmsSigNamedColor2Tag = 1852009522# /usr/include/lcms2.h: 396

cmsSigOutputResponseTag = 1919251312# /usr/include/lcms2.h: 396

cmsSigPerceptualRenderingIntentGamutTag = 1919510320# /usr/include/lcms2.h: 396

cmsSigPreview0Tag = 1886545200# /usr/include/lcms2.h: 396

cmsSigPreview1Tag = 1886545201# /usr/include/lcms2.h: 396

cmsSigPreview2Tag = 1886545202# /usr/include/lcms2.h: 396

cmsSigProfileDescriptionTag = 1684370275# /usr/include/lcms2.h: 396

cmsSigProfileDescriptionMLTag = 1685283693# /usr/include/lcms2.h: 396

cmsSigProfileSequenceDescTag = 1886610801# /usr/include/lcms2.h: 396

cmsSigProfileSequenceIdTag = 1886611812# /usr/include/lcms2.h: 396

cmsSigPs2CRD0Tag = 1886610480# /usr/include/lcms2.h: 396

cmsSigPs2CRD1Tag = 1886610481# /usr/include/lcms2.h: 396

cmsSigPs2CRD2Tag = 1886610482# /usr/include/lcms2.h: 396

cmsSigPs2CRD3Tag = 1886610483# /usr/include/lcms2.h: 396

cmsSigPs2CSATag = 1886597747# /usr/include/lcms2.h: 396

cmsSigPs2RenderingIntentTag = 1886597737# /usr/include/lcms2.h: 396

cmsSigRedColorantTag = 1918392666# /usr/include/lcms2.h: 396

cmsSigRedMatrixColumnTag = 1918392666# /usr/include/lcms2.h: 396

cmsSigRedTRCTag = 1918128707# /usr/include/lcms2.h: 396

cmsSigSaturationRenderingIntentGamutTag = 1919510322# /usr/include/lcms2.h: 396

cmsSigScreeningDescTag = 1935897188# /usr/include/lcms2.h: 396

cmsSigScreeningTag = 1935897198# /usr/include/lcms2.h: 396

cmsSigTechnologyTag = 1952801640# /usr/include/lcms2.h: 396

cmsSigUcrBgTag = 1650877472# /usr/include/lcms2.h: 396

cmsSigViewingCondDescTag = 1987405156# /usr/include/lcms2.h: 396

cmsSigViewingConditionsTag = 1986618743# /usr/include/lcms2.h: 396

cmsSigVcgtTag = 1986226036# /usr/include/lcms2.h: 396

cmsSigMetaTag = 1835365473# /usr/include/lcms2.h: 396

cmsSigArgyllArtsTag = 1634890867# /usr/include/lcms2.h: 396

cmsTagSignature = enum_anon_6# /usr/include/lcms2.h: 396

enum_anon_7 = c_int# /usr/include/lcms2.h: 428

cmsSigDigitalCamera = 1684234605# /usr/include/lcms2.h: 428

cmsSigFilmScanner = 1718838126# /usr/include/lcms2.h: 428

cmsSigReflectiveScanner = 1920164718# /usr/include/lcms2.h: 428

cmsSigInkJetPrinter = 1768580468# /usr/include/lcms2.h: 428

cmsSigThermalWaxPrinter = 1953980792# /usr/include/lcms2.h: 428

cmsSigElectrophotographicPrinter = 1701865583# /usr/include/lcms2.h: 428

cmsSigElectrostaticPrinter = 1702065249# /usr/include/lcms2.h: 428

cmsSigDyeSublimationPrinter = 1685288290# /usr/include/lcms2.h: 428

cmsSigPhotographicPaperPrinter = 1919969391# /usr/include/lcms2.h: 428

cmsSigFilmWriter = 1718645358# /usr/include/lcms2.h: 428

cmsSigVideoMonitor = 1986618477# /usr/include/lcms2.h: 428

cmsSigVideoCamera = 1986618467# /usr/include/lcms2.h: 428

cmsSigProjectionTelevision = 1886024822# /usr/include/lcms2.h: 428

cmsSigCRTDisplay = 1129468960# /usr/include/lcms2.h: 428

cmsSigPMDisplay = 1347240992# /usr/include/lcms2.h: 428

cmsSigAMDisplay = 1095582752# /usr/include/lcms2.h: 428

cmsSigPhotoCD = 1263551300# /usr/include/lcms2.h: 428

cmsSigPhotoImageSetter = 1768777587# /usr/include/lcms2.h: 428

cmsSigGravure = 1735549302# /usr/include/lcms2.h: 428

cmsSigOffsetLithography = 1868981875# /usr/include/lcms2.h: 428

cmsSigSilkscreen = 1936288875# /usr/include/lcms2.h: 428

cmsSigFlexography = 1718379896# /usr/include/lcms2.h: 428

cmsSigMotionPictureFilmScanner = 1836082803# /usr/include/lcms2.h: 428

cmsSigMotionPictureFilmRecorder = 1836082802# /usr/include/lcms2.h: 428

cmsSigDigitalMotionPictureCamera = 1684893795# /usr/include/lcms2.h: 428

cmsSigDigitalCinemaProjector = 1684236912# /usr/include/lcms2.h: 428

cmsTechnologySignature = enum_anon_7# /usr/include/lcms2.h: 428

enum_anon_8 = c_int# /usr/include/lcms2.h: 477

cmsSigXYZData = 1482250784# /usr/include/lcms2.h: 477

cmsSigLabData = 1281450528# /usr/include/lcms2.h: 477

cmsSigLuvData = 1282766368# /usr/include/lcms2.h: 477

cmsSigYCbCrData = 1497588338# /usr/include/lcms2.h: 477

cmsSigYxyData = 1501067552# /usr/include/lcms2.h: 477

cmsSigRgbData = 1380401696# /usr/include/lcms2.h: 477

cmsSigGrayData = 1196573017# /usr/include/lcms2.h: 477

cmsSigHsvData = 1213421088# /usr/include/lcms2.h: 477

cmsSigHlsData = 1212961568# /usr/include/lcms2.h: 477

cmsSigCmykData = 1129142603# /usr/include/lcms2.h: 477

cmsSigCmyData = 1129142560# /usr/include/lcms2.h: 477

cmsSigMCH1Data = 1296255025# /usr/include/lcms2.h: 477

cmsSigMCH2Data = 1296255026# /usr/include/lcms2.h: 477

cmsSigMCH3Data = 1296255027# /usr/include/lcms2.h: 477

cmsSigMCH4Data = 1296255028# /usr/include/lcms2.h: 477

cmsSigMCH5Data = 1296255029# /usr/include/lcms2.h: 477

cmsSigMCH6Data = 1296255030# /usr/include/lcms2.h: 477

cmsSigMCH7Data = 1296255031# /usr/include/lcms2.h: 477

cmsSigMCH8Data = 1296255032# /usr/include/lcms2.h: 477

cmsSigMCH9Data = 1296255033# /usr/include/lcms2.h: 477

cmsSigMCHAData = 1296255041# /usr/include/lcms2.h: 477

cmsSigMCHBData = 1296255042# /usr/include/lcms2.h: 477

cmsSigMCHCData = 1296255043# /usr/include/lcms2.h: 477

cmsSigMCHDData = 1296255044# /usr/include/lcms2.h: 477

cmsSigMCHEData = 1296255045# /usr/include/lcms2.h: 477

cmsSigMCHFData = 1296255046# /usr/include/lcms2.h: 477

cmsSigNamedData = 1852662636# /usr/include/lcms2.h: 477

cmsSig1colorData = 826494034# /usr/include/lcms2.h: 477

cmsSig2colorData = 843271250# /usr/include/lcms2.h: 477

cmsSig3colorData = 860048466# /usr/include/lcms2.h: 477

cmsSig4colorData = 876825682# /usr/include/lcms2.h: 477

cmsSig5colorData = 893602898# /usr/include/lcms2.h: 477

cmsSig6colorData = 910380114# /usr/include/lcms2.h: 477

cmsSig7colorData = 927157330# /usr/include/lcms2.h: 477

cmsSig8colorData = 943934546# /usr/include/lcms2.h: 477

cmsSig9colorData = 960711762# /usr/include/lcms2.h: 477

cmsSig10colorData = 1094929490# /usr/include/lcms2.h: 477

cmsSig11colorData = 1111706706# /usr/include/lcms2.h: 477

cmsSig12colorData = 1128483922# /usr/include/lcms2.h: 477

cmsSig13colorData = 1145261138# /usr/include/lcms2.h: 477

cmsSig14colorData = 1162038354# /usr/include/lcms2.h: 477

cmsSig15colorData = 1178815570# /usr/include/lcms2.h: 477

cmsSigLuvKData = 1282766411# /usr/include/lcms2.h: 477

cmsColorSpaceSignature = enum_anon_8# /usr/include/lcms2.h: 477

enum_anon_9 = c_int# /usr/include/lcms2.h: 489

cmsSigInputClass = 1935896178# /usr/include/lcms2.h: 489

cmsSigDisplayClass = 1835955314# /usr/include/lcms2.h: 489

cmsSigOutputClass = 1886549106# /usr/include/lcms2.h: 489

cmsSigLinkClass = 1818848875# /usr/include/lcms2.h: 489

cmsSigAbstractClass = 1633842036# /usr/include/lcms2.h: 489

cmsSigColorSpaceClass = 1936744803# /usr/include/lcms2.h: 489

cmsSigNamedColorClass = 1852662636# /usr/include/lcms2.h: 489

cmsProfileClassSignature = enum_anon_9# /usr/include/lcms2.h: 489

enum_anon_10 = c_int# /usr/include/lcms2.h: 500

cmsSigMacintosh = 1095782476# /usr/include/lcms2.h: 500

cmsSigMicrosoft = 1297303124# /usr/include/lcms2.h: 500

cmsSigSolaris = 1398099543# /usr/include/lcms2.h: 500

cmsSigSGI = 1397180704# /usr/include/lcms2.h: 500

cmsSigTaligent = 1413959252# /usr/include/lcms2.h: 500

cmsSigUnices = 711879032# /usr/include/lcms2.h: 500

cmsPlatformSignature = enum_anon_10# /usr/include/lcms2.h: 500

enum_anon_11 = c_int# /usr/include/lcms2.h: 538

cmsSigCurveSetElemType = 1668707188# /usr/include/lcms2.h: 538

cmsSigMatrixElemType = 1835103334# /usr/include/lcms2.h: 538

cmsSigCLutElemType = 1668052340# /usr/include/lcms2.h: 538

cmsSigBAcsElemType = 1648444243# /usr/include/lcms2.h: 538

cmsSigEAcsElemType = 1698775891# /usr/include/lcms2.h: 538

cmsSigXYZ2LabElemType = 1815246880# /usr/include/lcms2.h: 538

cmsSigLab2XYZElemType = 2016570400# /usr/include/lcms2.h: 538

cmsSigNamedColorElemType = 1852009504# /usr/include/lcms2.h: 538

cmsSigLabV2toV4 = 840971296# /usr/include/lcms2.h: 538

cmsSigLabV4toV2 = 874525216# /usr/include/lcms2.h: 538

cmsSigIdentityElemType = 1768189472# /usr/include/lcms2.h: 538

cmsSigLab2FloatPCS = 1681026080# /usr/include/lcms2.h: 538

cmsSigFloatPCS2Lab = 1815241760# /usr/include/lcms2.h: 538

cmsSigXYZ2FloatPCS = 1681029152# /usr/include/lcms2.h: 538

cmsSigFloatPCS2XYZ = 2016568352# /usr/include/lcms2.h: 538

cmsSigClipNegativesElemType = 1668050976# /usr/include/lcms2.h: 538

cmsStageSignature = enum_anon_11# /usr/include/lcms2.h: 538

enum_anon_12 = c_int# /usr/include/lcms2.h: 547

cmsSigFormulaCurveSeg = 1885434470# /usr/include/lcms2.h: 547

cmsSigSampledCurveSeg = 1935764838# /usr/include/lcms2.h: 547

cmsSigSegmentedCurve = 1668641382# /usr/include/lcms2.h: 547

cmsCurveSegSignature = enum_anon_12# /usr/include/lcms2.h: 547

# /usr/include/lcms2.h: 573
class struct_anon_13(Structure):
    pass

struct_anon_13.__slots__ = [
    'len',
    'flag',
    'data',
]
struct_anon_13._fields_ = [
    ('len', cmsUInt32Number),
    ('flag', cmsUInt32Number),
    ('data', cmsUInt8Number * int(1)),
]

cmsICCData = struct_anon_13# /usr/include/lcms2.h: 573

# /usr/include/lcms2.h: 584
class struct_anon_14(Structure):
    pass

struct_anon_14.__slots__ = [
    'year',
    'month',
    'day',
    'hours',
    'minutes',
    'seconds',
]
struct_anon_14._fields_ = [
    ('year', cmsUInt16Number),
    ('month', cmsUInt16Number),
    ('day', cmsUInt16Number),
    ('hours', cmsUInt16Number),
    ('minutes', cmsUInt16Number),
    ('seconds', cmsUInt16Number),
]

cmsDateTimeNumber = struct_anon_14# /usr/include/lcms2.h: 584

# /usr/include/lcms2.h: 592
class struct_anon_15(Structure):
    pass

struct_anon_15.__slots__ = [
    'X',
    'Y',
    'Z',
]
struct_anon_15._fields_ = [
    ('X', cmsS15Fixed16Number),
    ('Y', cmsS15Fixed16Number),
    ('Z', cmsS15Fixed16Number),
]

cmsEncodedXYZNumber = struct_anon_15# /usr/include/lcms2.h: 592

# /usr/include/lcms2.h: 601
class union_anon_16(Union):
    pass

union_anon_16.__slots__ = [
    'ID8',
    'ID16',
    'ID32',
]
union_anon_16._fields_ = [
    ('ID8', cmsUInt8Number * int(16)),
    ('ID16', cmsUInt16Number * int(8)),
    ('ID32', cmsUInt32Number * int(4)),
]

cmsProfileID = union_anon_16# /usr/include/lcms2.h: 601

# /usr/include/lcms2.h: 629
class struct_anon_17(Structure):
    pass

struct_anon_17.__slots__ = [
    'size',
    'cmmId',
    'version',
    'deviceClass',
    'colorSpace',
    'pcs',
    'date',
    'magic',
    'platform',
    'flags',
    'manufacturer',
    'model',
    'attributes',
    'renderingIntent',
    'illuminant',
    'creator',
    'profileID',
    'reserved',
]
struct_anon_17._fields_ = [
    ('size', cmsUInt32Number),
    ('cmmId', cmsSignature),
    ('version', cmsUInt32Number),
    ('deviceClass', cmsProfileClassSignature),
    ('colorSpace', cmsColorSpaceSignature),
    ('pcs', cmsColorSpaceSignature),
    ('date', cmsDateTimeNumber),
    ('magic', cmsSignature),
    ('platform', cmsPlatformSignature),
    ('flags', cmsUInt32Number),
    ('manufacturer', cmsSignature),
    ('model', cmsUInt32Number),
    ('attributes', cmsUInt64Number),
    ('renderingIntent', cmsUInt32Number),
    ('illuminant', cmsEncodedXYZNumber),
    ('creator', cmsSignature),
    ('profileID', cmsProfileID),
    ('reserved', cmsInt8Number * int(28)),
]

cmsICCHeader = struct_anon_17# /usr/include/lcms2.h: 629

# /usr/include/lcms2.h: 636
class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'sig',
    'reserved',
]
struct_anon_18._fields_ = [
    ('sig', cmsTagTypeSignature),
    ('reserved', cmsInt8Number * int(4)),
]

cmsTagBase = struct_anon_18# /usr/include/lcms2.h: 636

# /usr/include/lcms2.h: 644
class struct_anon_19(Structure):
    pass

struct_anon_19.__slots__ = [
    'sig',
    'offset',
    'size',
]
struct_anon_19._fields_ = [
    ('sig', cmsTagSignature),
    ('offset', cmsUInt32Number),
    ('size', cmsUInt32Number),
]

cmsTagEntry = struct_anon_19# /usr/include/lcms2.h: 644

cmsHANDLE = POINTER(None)# /usr/include/lcms2.h: 650

cmsHPROFILE = POINTER(None)# /usr/include/lcms2.h: 651

cmsHTRANSFORM = POINTER(None)# /usr/include/lcms2.h: 652

# /usr/include/lcms2.h: 943
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'X',
    'Y',
    'Z',
]
struct_anon_20._fields_ = [
    ('X', cmsFloat64Number),
    ('Y', cmsFloat64Number),
    ('Z', cmsFloat64Number),
]

cmsCIEXYZ = struct_anon_20# /usr/include/lcms2.h: 943

# /usr/include/lcms2.h: 950
class struct_anon_21(Structure):
    pass

struct_anon_21.__slots__ = [
    'x',
    'y',
    'Y',
]
struct_anon_21._fields_ = [
    ('x', cmsFloat64Number),
    ('y', cmsFloat64Number),
    ('Y', cmsFloat64Number),
]

cmsCIExyY = struct_anon_21# /usr/include/lcms2.h: 950

# /usr/include/lcms2.h: 957
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'L',
    'a',
    'b',
]
struct_anon_22._fields_ = [
    ('L', cmsFloat64Number),
    ('a', cmsFloat64Number),
    ('b', cmsFloat64Number),
]

cmsCIELab = struct_anon_22# /usr/include/lcms2.h: 957

# /usr/include/lcms2.h: 964
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'L',
    'C',
    'h',
]
struct_anon_23._fields_ = [
    ('L', cmsFloat64Number),
    ('C', cmsFloat64Number),
    ('h', cmsFloat64Number),
]

cmsCIELCh = struct_anon_23# /usr/include/lcms2.h: 964

# /usr/include/lcms2.h: 971
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'J',
    'C',
    'h',
]
struct_anon_24._fields_ = [
    ('J', cmsFloat64Number),
    ('C', cmsFloat64Number),
    ('h', cmsFloat64Number),
]

cmsJCh = struct_anon_24# /usr/include/lcms2.h: 971

# /usr/include/lcms2.h: 978
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'Red',
    'Green',
    'Blue',
]
struct_anon_25._fields_ = [
    ('Red', cmsCIEXYZ),
    ('Green', cmsCIEXYZ),
    ('Blue', cmsCIEXYZ),
]

cmsCIEXYZTRIPLE = struct_anon_25# /usr/include/lcms2.h: 978

# /usr/include/lcms2.h: 985
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'Red',
    'Green',
    'Blue',
]
struct_anon_26._fields_ = [
    ('Red', cmsCIExyY),
    ('Green', cmsCIExyY),
    ('Blue', cmsCIExyY),
]

cmsCIExyYTRIPLE = struct_anon_26# /usr/include/lcms2.h: 985

# /usr/include/lcms2.h: 1005
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'Observer',
    'Backing',
    'Geometry',
    'Flare',
    'IlluminantType',
]
struct_anon_27._fields_ = [
    ('Observer', cmsUInt32Number),
    ('Backing', cmsCIEXYZ),
    ('Geometry', cmsUInt32Number),
    ('Flare', cmsFloat64Number),
    ('IlluminantType', cmsUInt32Number),
]

cmsICCMeasurementConditions = struct_anon_27# /usr/include/lcms2.h: 1005

# /usr/include/lcms2.h: 1012
class struct_anon_28(Structure):
    pass

struct_anon_28.__slots__ = [
    'IlluminantXYZ',
    'SurroundXYZ',
    'IlluminantType',
]
struct_anon_28._fields_ = [
    ('IlluminantXYZ', cmsCIEXYZ),
    ('SurroundXYZ', cmsCIEXYZ),
    ('IlluminantType', cmsUInt32Number),
]

cmsICCViewingConditions = struct_anon_28# /usr/include/lcms2.h: 1012

# /usr/include/lcms2.h: 1016
if _libs["lcms2"].has("cmsGetEncodedCMMversion", "cdecl"):
    cmsGetEncodedCMMversion = _libs["lcms2"].get("cmsGetEncodedCMMversion", "cdecl")
    cmsGetEncodedCMMversion.argtypes = []
    cmsGetEncodedCMMversion.restype = c_int

# /usr/include/lcms2.h: 1020
if _libs["lcms2"].has("cmsstrcasecmp", "cdecl"):
    cmsstrcasecmp = _libs["lcms2"].get("cmsstrcasecmp", "cdecl")
    cmsstrcasecmp.argtypes = [String, String]
    cmsstrcasecmp.restype = c_int

# /usr/include/lcms2.h: 1021
if _libs["lcms2"].has("cmsfilelength", "cdecl"):
    cmsfilelength = _libs["lcms2"].get("cmsfilelength", "cdecl")
    cmsfilelength.argtypes = [POINTER(FILE)]
    cmsfilelength.restype = c_long

# /usr/include/lcms2.h: 1029
class struct__cmsContext_struct(Structure):
    pass

cmsContext = POINTER(struct__cmsContext_struct)# /usr/include/lcms2.h: 1029

# /usr/include/lcms2.h: 1031
if _libs["lcms2"].has("cmsCreateContext", "cdecl"):
    cmsCreateContext = _libs["lcms2"].get("cmsCreateContext", "cdecl")
    cmsCreateContext.argtypes = [POINTER(None), POINTER(None)]
    cmsCreateContext.restype = cmsContext

# /usr/include/lcms2.h: 1032
if _libs["lcms2"].has("cmsDeleteContext", "cdecl"):
    cmsDeleteContext = _libs["lcms2"].get("cmsDeleteContext", "cdecl")
    cmsDeleteContext.argtypes = [cmsContext]
    cmsDeleteContext.restype = None

# /usr/include/lcms2.h: 1033
if _libs["lcms2"].has("cmsDupContext", "cdecl"):
    cmsDupContext = _libs["lcms2"].get("cmsDupContext", "cdecl")
    cmsDupContext.argtypes = [cmsContext, POINTER(None)]
    cmsDupContext.restype = cmsContext

# /usr/include/lcms2.h: 1034
if _libs["lcms2"].has("cmsGetContextUserData", "cdecl"):
    cmsGetContextUserData = _libs["lcms2"].get("cmsGetContextUserData", "cdecl")
    cmsGetContextUserData.argtypes = [cmsContext]
    cmsGetContextUserData.restype = POINTER(c_ubyte)
    cmsGetContextUserData.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/lcms2.h: 1038
if _libs["lcms2"].has("cmsPlugin", "cdecl"):
    cmsPlugin = _libs["lcms2"].get("cmsPlugin", "cdecl")
    cmsPlugin.argtypes = [POINTER(None)]
    cmsPlugin.restype = cmsBool

# /usr/include/lcms2.h: 1039
if _libs["lcms2"].has("cmsPluginTHR", "cdecl"):
    cmsPluginTHR = _libs["lcms2"].get("cmsPluginTHR", "cdecl")
    cmsPluginTHR.argtypes = [cmsContext, POINTER(None)]
    cmsPluginTHR.restype = cmsBool

# /usr/include/lcms2.h: 1040
if _libs["lcms2"].has("cmsUnregisterPlugins", "cdecl"):
    cmsUnregisterPlugins = _libs["lcms2"].get("cmsUnregisterPlugins", "cdecl")
    cmsUnregisterPlugins.argtypes = []
    cmsUnregisterPlugins.restype = None

# /usr/include/lcms2.h: 1041
if _libs["lcms2"].has("cmsUnregisterPluginsTHR", "cdecl"):
    cmsUnregisterPluginsTHR = _libs["lcms2"].get("cmsUnregisterPluginsTHR", "cdecl")
    cmsUnregisterPluginsTHR.argtypes = [cmsContext]
    cmsUnregisterPluginsTHR.restype = None

cmsLogErrorHandlerFunction = CFUNCTYPE(UNCHECKED(None), cmsContext, cmsUInt32Number, String)# /usr/include/lcms2.h: 1074

# /usr/include/lcms2.h: 1077
if _libs["lcms2"].has("cmsSetLogErrorHandler", "cdecl"):
    cmsSetLogErrorHandler = _libs["lcms2"].get("cmsSetLogErrorHandler", "cdecl")
    cmsSetLogErrorHandler.argtypes = [cmsLogErrorHandlerFunction]
    cmsSetLogErrorHandler.restype = None

# /usr/include/lcms2.h: 1078
if _libs["lcms2"].has("cmsSetLogErrorHandlerTHR", "cdecl"):
    cmsSetLogErrorHandlerTHR = _libs["lcms2"].get("cmsSetLogErrorHandlerTHR", "cdecl")
    cmsSetLogErrorHandlerTHR.argtypes = [cmsContext, cmsLogErrorHandlerFunction]
    cmsSetLogErrorHandlerTHR.restype = None

# /usr/include/lcms2.h: 1083
if _libs["lcms2"].has("cmsD50_XYZ", "cdecl"):
    cmsD50_XYZ = _libs["lcms2"].get("cmsD50_XYZ", "cdecl")
    cmsD50_XYZ.argtypes = []
    cmsD50_XYZ.restype = POINTER(cmsCIEXYZ)

# /usr/include/lcms2.h: 1084
if _libs["lcms2"].has("cmsD50_xyY", "cdecl"):
    cmsD50_xyY = _libs["lcms2"].get("cmsD50_xyY", "cdecl")
    cmsD50_xyY.argtypes = []
    cmsD50_xyY.restype = POINTER(cmsCIExyY)

# /usr/include/lcms2.h: 1087
if _libs["lcms2"].has("cmsXYZ2xyY", "cdecl"):
    cmsXYZ2xyY = _libs["lcms2"].get("cmsXYZ2xyY", "cdecl")
    cmsXYZ2xyY.argtypes = [POINTER(cmsCIExyY), POINTER(cmsCIEXYZ)]
    cmsXYZ2xyY.restype = None

# /usr/include/lcms2.h: 1088
if _libs["lcms2"].has("cmsxyY2XYZ", "cdecl"):
    cmsxyY2XYZ = _libs["lcms2"].get("cmsxyY2XYZ", "cdecl")
    cmsxyY2XYZ.argtypes = [POINTER(cmsCIEXYZ), POINTER(cmsCIExyY)]
    cmsxyY2XYZ.restype = None

# /usr/include/lcms2.h: 1089
if _libs["lcms2"].has("cmsXYZ2Lab", "cdecl"):
    cmsXYZ2Lab = _libs["lcms2"].get("cmsXYZ2Lab", "cdecl")
    cmsXYZ2Lab.argtypes = [POINTER(cmsCIEXYZ), POINTER(cmsCIELab), POINTER(cmsCIEXYZ)]
    cmsXYZ2Lab.restype = None

# /usr/include/lcms2.h: 1090
if _libs["lcms2"].has("cmsLab2XYZ", "cdecl"):
    cmsLab2XYZ = _libs["lcms2"].get("cmsLab2XYZ", "cdecl")
    cmsLab2XYZ.argtypes = [POINTER(cmsCIEXYZ), POINTER(cmsCIEXYZ), POINTER(cmsCIELab)]
    cmsLab2XYZ.restype = None

# /usr/include/lcms2.h: 1091
if _libs["lcms2"].has("cmsLab2LCh", "cdecl"):
    cmsLab2LCh = _libs["lcms2"].get("cmsLab2LCh", "cdecl")
    cmsLab2LCh.argtypes = [POINTER(cmsCIELCh), POINTER(cmsCIELab)]
    cmsLab2LCh.restype = None

# /usr/include/lcms2.h: 1092
if _libs["lcms2"].has("cmsLCh2Lab", "cdecl"):
    cmsLCh2Lab = _libs["lcms2"].get("cmsLCh2Lab", "cdecl")
    cmsLCh2Lab.argtypes = [POINTER(cmsCIELab), POINTER(cmsCIELCh)]
    cmsLCh2Lab.restype = None

# /usr/include/lcms2.h: 1095
if _libs["lcms2"].has("cmsLabEncoded2Float", "cdecl"):
    cmsLabEncoded2Float = _libs["lcms2"].get("cmsLabEncoded2Float", "cdecl")
    cmsLabEncoded2Float.argtypes = [POINTER(cmsCIELab), cmsUInt16Number * int(3)]
    cmsLabEncoded2Float.restype = None

# /usr/include/lcms2.h: 1096
if _libs["lcms2"].has("cmsLabEncoded2FloatV2", "cdecl"):
    cmsLabEncoded2FloatV2 = _libs["lcms2"].get("cmsLabEncoded2FloatV2", "cdecl")
    cmsLabEncoded2FloatV2.argtypes = [POINTER(cmsCIELab), cmsUInt16Number * int(3)]
    cmsLabEncoded2FloatV2.restype = None

# /usr/include/lcms2.h: 1097
if _libs["lcms2"].has("cmsFloat2LabEncoded", "cdecl"):
    cmsFloat2LabEncoded = _libs["lcms2"].get("cmsFloat2LabEncoded", "cdecl")
    cmsFloat2LabEncoded.argtypes = [cmsUInt16Number * int(3), POINTER(cmsCIELab)]
    cmsFloat2LabEncoded.restype = None

# /usr/include/lcms2.h: 1098
if _libs["lcms2"].has("cmsFloat2LabEncodedV2", "cdecl"):
    cmsFloat2LabEncodedV2 = _libs["lcms2"].get("cmsFloat2LabEncodedV2", "cdecl")
    cmsFloat2LabEncodedV2.argtypes = [cmsUInt16Number * int(3), POINTER(cmsCIELab)]
    cmsFloat2LabEncodedV2.restype = None

# /usr/include/lcms2.h: 1099
if _libs["lcms2"].has("cmsXYZEncoded2Float", "cdecl"):
    cmsXYZEncoded2Float = _libs["lcms2"].get("cmsXYZEncoded2Float", "cdecl")
    cmsXYZEncoded2Float.argtypes = [POINTER(cmsCIEXYZ), cmsUInt16Number * int(3)]
    cmsXYZEncoded2Float.restype = None

# /usr/include/lcms2.h: 1100
if _libs["lcms2"].has("cmsFloat2XYZEncoded", "cdecl"):
    cmsFloat2XYZEncoded = _libs["lcms2"].get("cmsFloat2XYZEncoded", "cdecl")
    cmsFloat2XYZEncoded.argtypes = [cmsUInt16Number * int(3), POINTER(cmsCIEXYZ)]
    cmsFloat2XYZEncoded.restype = None

# /usr/include/lcms2.h: 1103
if _libs["lcms2"].has("cmsDeltaE", "cdecl"):
    cmsDeltaE = _libs["lcms2"].get("cmsDeltaE", "cdecl")
    cmsDeltaE.argtypes = [POINTER(cmsCIELab), POINTER(cmsCIELab)]
    cmsDeltaE.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1104
if _libs["lcms2"].has("cmsCIE94DeltaE", "cdecl"):
    cmsCIE94DeltaE = _libs["lcms2"].get("cmsCIE94DeltaE", "cdecl")
    cmsCIE94DeltaE.argtypes = [POINTER(cmsCIELab), POINTER(cmsCIELab)]
    cmsCIE94DeltaE.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1105
if _libs["lcms2"].has("cmsBFDdeltaE", "cdecl"):
    cmsBFDdeltaE = _libs["lcms2"].get("cmsBFDdeltaE", "cdecl")
    cmsBFDdeltaE.argtypes = [POINTER(cmsCIELab), POINTER(cmsCIELab)]
    cmsBFDdeltaE.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1106
if _libs["lcms2"].has("cmsCMCdeltaE", "cdecl"):
    cmsCMCdeltaE = _libs["lcms2"].get("cmsCMCdeltaE", "cdecl")
    cmsCMCdeltaE.argtypes = [POINTER(cmsCIELab), POINTER(cmsCIELab), cmsFloat64Number, cmsFloat64Number]
    cmsCMCdeltaE.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1107
if _libs["lcms2"].has("cmsCIE2000DeltaE", "cdecl"):
    cmsCIE2000DeltaE = _libs["lcms2"].get("cmsCIE2000DeltaE", "cdecl")
    cmsCIE2000DeltaE.argtypes = [POINTER(cmsCIELab), POINTER(cmsCIELab), cmsFloat64Number, cmsFloat64Number, cmsFloat64Number]
    cmsCIE2000DeltaE.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1110
if _libs["lcms2"].has("cmsWhitePointFromTemp", "cdecl"):
    cmsWhitePointFromTemp = _libs["lcms2"].get("cmsWhitePointFromTemp", "cdecl")
    cmsWhitePointFromTemp.argtypes = [POINTER(cmsCIExyY), cmsFloat64Number]
    cmsWhitePointFromTemp.restype = cmsBool

# /usr/include/lcms2.h: 1111
if _libs["lcms2"].has("cmsTempFromWhitePoint", "cdecl"):
    cmsTempFromWhitePoint = _libs["lcms2"].get("cmsTempFromWhitePoint", "cdecl")
    cmsTempFromWhitePoint.argtypes = [POINTER(cmsFloat64Number), POINTER(cmsCIExyY)]
    cmsTempFromWhitePoint.restype = cmsBool

# /usr/include/lcms2.h: 1114
if _libs["lcms2"].has("cmsAdaptToIlluminant", "cdecl"):
    cmsAdaptToIlluminant = _libs["lcms2"].get("cmsAdaptToIlluminant", "cdecl")
    cmsAdaptToIlluminant.argtypes = [POINTER(cmsCIEXYZ), POINTER(cmsCIEXYZ), POINTER(cmsCIEXYZ), POINTER(cmsCIEXYZ)]
    cmsAdaptToIlluminant.restype = cmsBool

# /usr/include/lcms2.h: 1139
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'whitePoint',
    'Yb',
    'La',
    'surround',
    'D_value',
]
struct_anon_29._fields_ = [
    ('whitePoint', cmsCIEXYZ),
    ('Yb', cmsFloat64Number),
    ('La', cmsFloat64Number),
    ('surround', cmsUInt32Number),
    ('D_value', cmsFloat64Number),
]

cmsViewingConditions = struct_anon_29# /usr/include/lcms2.h: 1139

# /usr/include/lcms2.h: 1141
if _libs["lcms2"].has("cmsCIECAM02Init", "cdecl"):
    cmsCIECAM02Init = _libs["lcms2"].get("cmsCIECAM02Init", "cdecl")
    cmsCIECAM02Init.argtypes = [cmsContext, POINTER(cmsViewingConditions)]
    cmsCIECAM02Init.restype = cmsHANDLE

# /usr/include/lcms2.h: 1142
if _libs["lcms2"].has("cmsCIECAM02Done", "cdecl"):
    cmsCIECAM02Done = _libs["lcms2"].get("cmsCIECAM02Done", "cdecl")
    cmsCIECAM02Done.argtypes = [cmsHANDLE]
    cmsCIECAM02Done.restype = None

# /usr/include/lcms2.h: 1143
if _libs["lcms2"].has("cmsCIECAM02Forward", "cdecl"):
    cmsCIECAM02Forward = _libs["lcms2"].get("cmsCIECAM02Forward", "cdecl")
    cmsCIECAM02Forward.argtypes = [cmsHANDLE, POINTER(cmsCIEXYZ), POINTER(cmsJCh)]
    cmsCIECAM02Forward.restype = None

# /usr/include/lcms2.h: 1144
if _libs["lcms2"].has("cmsCIECAM02Reverse", "cdecl"):
    cmsCIECAM02Reverse = _libs["lcms2"].get("cmsCIECAM02Reverse", "cdecl")
    cmsCIECAM02Reverse.argtypes = [cmsHANDLE, POINTER(cmsJCh), POINTER(cmsCIEXYZ)]
    cmsCIECAM02Reverse.restype = None

# /usr/include/lcms2.h: 1159
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'x0',
    'x1',
    'Type',
    'Params',
    'nGridPoints',
    'SampledPoints',
]
struct_anon_30._fields_ = [
    ('x0', cmsFloat32Number),
    ('x1', cmsFloat32Number),
    ('Type', cmsInt32Number),
    ('Params', cmsFloat64Number * int(10)),
    ('nGridPoints', cmsUInt32Number),
    ('SampledPoints', POINTER(cmsFloat32Number)),
]

cmsCurveSegment = struct_anon_30# /usr/include/lcms2.h: 1159

# /usr/include/lcms2.h: 1162
class struct__cms_curve_struct(Structure):
    pass

cmsToneCurve = struct__cms_curve_struct# /usr/include/lcms2.h: 1162

# /usr/include/lcms2.h: 1164
if _libs["lcms2"].has("cmsBuildSegmentedToneCurve", "cdecl"):
    cmsBuildSegmentedToneCurve = _libs["lcms2"].get("cmsBuildSegmentedToneCurve", "cdecl")
    cmsBuildSegmentedToneCurve.argtypes = [cmsContext, cmsUInt32Number, POINTER(cmsCurveSegment)]
    cmsBuildSegmentedToneCurve.restype = POINTER(cmsToneCurve)

# /usr/include/lcms2.h: 1165
if _libs["lcms2"].has("cmsBuildParametricToneCurve", "cdecl"):
    cmsBuildParametricToneCurve = _libs["lcms2"].get("cmsBuildParametricToneCurve", "cdecl")
    cmsBuildParametricToneCurve.argtypes = [cmsContext, cmsInt32Number, POINTER(cmsFloat64Number)]
    cmsBuildParametricToneCurve.restype = POINTER(cmsToneCurve)

# /usr/include/lcms2.h: 1166
if _libs["lcms2"].has("cmsBuildGamma", "cdecl"):
    cmsBuildGamma = _libs["lcms2"].get("cmsBuildGamma", "cdecl")
    cmsBuildGamma.argtypes = [cmsContext, cmsFloat64Number]
    cmsBuildGamma.restype = POINTER(cmsToneCurve)

# /usr/include/lcms2.h: 1167
if _libs["lcms2"].has("cmsBuildTabulatedToneCurve16", "cdecl"):
    cmsBuildTabulatedToneCurve16 = _libs["lcms2"].get("cmsBuildTabulatedToneCurve16", "cdecl")
    cmsBuildTabulatedToneCurve16.argtypes = [cmsContext, cmsUInt32Number, POINTER(cmsUInt16Number)]
    cmsBuildTabulatedToneCurve16.restype = POINTER(cmsToneCurve)

# /usr/include/lcms2.h: 1168
if _libs["lcms2"].has("cmsBuildTabulatedToneCurveFloat", "cdecl"):
    cmsBuildTabulatedToneCurveFloat = _libs["lcms2"].get("cmsBuildTabulatedToneCurveFloat", "cdecl")
    cmsBuildTabulatedToneCurveFloat.argtypes = [cmsContext, cmsUInt32Number, POINTER(cmsFloat32Number)]
    cmsBuildTabulatedToneCurveFloat.restype = POINTER(cmsToneCurve)

# /usr/include/lcms2.h: 1169
if _libs["lcms2"].has("cmsFreeToneCurve", "cdecl"):
    cmsFreeToneCurve = _libs["lcms2"].get("cmsFreeToneCurve", "cdecl")
    cmsFreeToneCurve.argtypes = [POINTER(cmsToneCurve)]
    cmsFreeToneCurve.restype = None

# /usr/include/lcms2.h: 1170
if _libs["lcms2"].has("cmsFreeToneCurveTriple", "cdecl"):
    cmsFreeToneCurveTriple = _libs["lcms2"].get("cmsFreeToneCurveTriple", "cdecl")
    cmsFreeToneCurveTriple.argtypes = [POINTER(cmsToneCurve) * int(3)]
    cmsFreeToneCurveTriple.restype = None

# /usr/include/lcms2.h: 1171
if _libs["lcms2"].has("cmsDupToneCurve", "cdecl"):
    cmsDupToneCurve = _libs["lcms2"].get("cmsDupToneCurve", "cdecl")
    cmsDupToneCurve.argtypes = [POINTER(cmsToneCurve)]
    cmsDupToneCurve.restype = POINTER(cmsToneCurve)

# /usr/include/lcms2.h: 1172
if _libs["lcms2"].has("cmsReverseToneCurve", "cdecl"):
    cmsReverseToneCurve = _libs["lcms2"].get("cmsReverseToneCurve", "cdecl")
    cmsReverseToneCurve.argtypes = [POINTER(cmsToneCurve)]
    cmsReverseToneCurve.restype = POINTER(cmsToneCurve)

# /usr/include/lcms2.h: 1173
if _libs["lcms2"].has("cmsReverseToneCurveEx", "cdecl"):
    cmsReverseToneCurveEx = _libs["lcms2"].get("cmsReverseToneCurveEx", "cdecl")
    cmsReverseToneCurveEx.argtypes = [cmsUInt32Number, POINTER(cmsToneCurve)]
    cmsReverseToneCurveEx.restype = POINTER(cmsToneCurve)

# /usr/include/lcms2.h: 1174
if _libs["lcms2"].has("cmsJoinToneCurve", "cdecl"):
    cmsJoinToneCurve = _libs["lcms2"].get("cmsJoinToneCurve", "cdecl")
    cmsJoinToneCurve.argtypes = [cmsContext, POINTER(cmsToneCurve), POINTER(cmsToneCurve), cmsUInt32Number]
    cmsJoinToneCurve.restype = POINTER(cmsToneCurve)

# /usr/include/lcms2.h: 1175
if _libs["lcms2"].has("cmsSmoothToneCurve", "cdecl"):
    cmsSmoothToneCurve = _libs["lcms2"].get("cmsSmoothToneCurve", "cdecl")
    cmsSmoothToneCurve.argtypes = [POINTER(cmsToneCurve), cmsFloat64Number]
    cmsSmoothToneCurve.restype = cmsBool

# /usr/include/lcms2.h: 1176
if _libs["lcms2"].has("cmsEvalToneCurveFloat", "cdecl"):
    cmsEvalToneCurveFloat = _libs["lcms2"].get("cmsEvalToneCurveFloat", "cdecl")
    cmsEvalToneCurveFloat.argtypes = [POINTER(cmsToneCurve), cmsFloat32Number]
    cmsEvalToneCurveFloat.restype = cmsFloat32Number

# /usr/include/lcms2.h: 1177
if _libs["lcms2"].has("cmsEvalToneCurve16", "cdecl"):
    cmsEvalToneCurve16 = _libs["lcms2"].get("cmsEvalToneCurve16", "cdecl")
    cmsEvalToneCurve16.argtypes = [POINTER(cmsToneCurve), cmsUInt16Number]
    cmsEvalToneCurve16.restype = cmsUInt16Number

# /usr/include/lcms2.h: 1178
if _libs["lcms2"].has("cmsIsToneCurveMultisegment", "cdecl"):
    cmsIsToneCurveMultisegment = _libs["lcms2"].get("cmsIsToneCurveMultisegment", "cdecl")
    cmsIsToneCurveMultisegment.argtypes = [POINTER(cmsToneCurve)]
    cmsIsToneCurveMultisegment.restype = cmsBool

# /usr/include/lcms2.h: 1179
if _libs["lcms2"].has("cmsIsToneCurveLinear", "cdecl"):
    cmsIsToneCurveLinear = _libs["lcms2"].get("cmsIsToneCurveLinear", "cdecl")
    cmsIsToneCurveLinear.argtypes = [POINTER(cmsToneCurve)]
    cmsIsToneCurveLinear.restype = cmsBool

# /usr/include/lcms2.h: 1180
if _libs["lcms2"].has("cmsIsToneCurveMonotonic", "cdecl"):
    cmsIsToneCurveMonotonic = _libs["lcms2"].get("cmsIsToneCurveMonotonic", "cdecl")
    cmsIsToneCurveMonotonic.argtypes = [POINTER(cmsToneCurve)]
    cmsIsToneCurveMonotonic.restype = cmsBool

# /usr/include/lcms2.h: 1181
if _libs["lcms2"].has("cmsIsToneCurveDescending", "cdecl"):
    cmsIsToneCurveDescending = _libs["lcms2"].get("cmsIsToneCurveDescending", "cdecl")
    cmsIsToneCurveDescending.argtypes = [POINTER(cmsToneCurve)]
    cmsIsToneCurveDescending.restype = cmsBool

# /usr/include/lcms2.h: 1182
if _libs["lcms2"].has("cmsGetToneCurveParametricType", "cdecl"):
    cmsGetToneCurveParametricType = _libs["lcms2"].get("cmsGetToneCurveParametricType", "cdecl")
    cmsGetToneCurveParametricType.argtypes = [POINTER(cmsToneCurve)]
    cmsGetToneCurveParametricType.restype = cmsInt32Number

# /usr/include/lcms2.h: 1183
if _libs["lcms2"].has("cmsEstimateGamma", "cdecl"):
    cmsEstimateGamma = _libs["lcms2"].get("cmsEstimateGamma", "cdecl")
    cmsEstimateGamma.argtypes = [POINTER(cmsToneCurve), cmsFloat64Number]
    cmsEstimateGamma.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1186
if _libs["lcms2"].has("cmsGetToneCurveEstimatedTableEntries", "cdecl"):
    cmsGetToneCurveEstimatedTableEntries = _libs["lcms2"].get("cmsGetToneCurveEstimatedTableEntries", "cdecl")
    cmsGetToneCurveEstimatedTableEntries.argtypes = [POINTER(cmsToneCurve)]
    cmsGetToneCurveEstimatedTableEntries.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1187
if _libs["lcms2"].has("cmsGetToneCurveEstimatedTable", "cdecl"):
    cmsGetToneCurveEstimatedTable = _libs["lcms2"].get("cmsGetToneCurveEstimatedTable", "cdecl")
    cmsGetToneCurveEstimatedTable.argtypes = [POINTER(cmsToneCurve)]
    cmsGetToneCurveEstimatedTable.restype = POINTER(cmsUInt16Number)

# /usr/include/lcms2.h: 1193
class struct__cmsPipeline_struct(Structure):
    pass

cmsPipeline = struct__cmsPipeline_struct# /usr/include/lcms2.h: 1193

# /usr/include/lcms2.h: 1194
class struct__cmsStage_struct(Structure):
    pass

cmsStage = struct__cmsStage_struct# /usr/include/lcms2.h: 1194

# /usr/include/lcms2.h: 1197
if _libs["lcms2"].has("cmsPipelineAlloc", "cdecl"):
    cmsPipelineAlloc = _libs["lcms2"].get("cmsPipelineAlloc", "cdecl")
    cmsPipelineAlloc.argtypes = [cmsContext, cmsUInt32Number, cmsUInt32Number]
    cmsPipelineAlloc.restype = POINTER(cmsPipeline)

# /usr/include/lcms2.h: 1198
if _libs["lcms2"].has("cmsPipelineFree", "cdecl"):
    cmsPipelineFree = _libs["lcms2"].get("cmsPipelineFree", "cdecl")
    cmsPipelineFree.argtypes = [POINTER(cmsPipeline)]
    cmsPipelineFree.restype = None

# /usr/include/lcms2.h: 1199
if _libs["lcms2"].has("cmsPipelineDup", "cdecl"):
    cmsPipelineDup = _libs["lcms2"].get("cmsPipelineDup", "cdecl")
    cmsPipelineDup.argtypes = [POINTER(cmsPipeline)]
    cmsPipelineDup.restype = POINTER(cmsPipeline)

# /usr/include/lcms2.h: 1201
if _libs["lcms2"].has("cmsGetPipelineContextID", "cdecl"):
    cmsGetPipelineContextID = _libs["lcms2"].get("cmsGetPipelineContextID", "cdecl")
    cmsGetPipelineContextID.argtypes = [POINTER(cmsPipeline)]
    cmsGetPipelineContextID.restype = cmsContext

# /usr/include/lcms2.h: 1202
if _libs["lcms2"].has("cmsPipelineInputChannels", "cdecl"):
    cmsPipelineInputChannels = _libs["lcms2"].get("cmsPipelineInputChannels", "cdecl")
    cmsPipelineInputChannels.argtypes = [POINTER(cmsPipeline)]
    cmsPipelineInputChannels.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1203
if _libs["lcms2"].has("cmsPipelineOutputChannels", "cdecl"):
    cmsPipelineOutputChannels = _libs["lcms2"].get("cmsPipelineOutputChannels", "cdecl")
    cmsPipelineOutputChannels.argtypes = [POINTER(cmsPipeline)]
    cmsPipelineOutputChannels.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1205
if _libs["lcms2"].has("cmsPipelineStageCount", "cdecl"):
    cmsPipelineStageCount = _libs["lcms2"].get("cmsPipelineStageCount", "cdecl")
    cmsPipelineStageCount.argtypes = [POINTER(cmsPipeline)]
    cmsPipelineStageCount.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1206
if _libs["lcms2"].has("cmsPipelineGetPtrToFirstStage", "cdecl"):
    cmsPipelineGetPtrToFirstStage = _libs["lcms2"].get("cmsPipelineGetPtrToFirstStage", "cdecl")
    cmsPipelineGetPtrToFirstStage.argtypes = [POINTER(cmsPipeline)]
    cmsPipelineGetPtrToFirstStage.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1207
if _libs["lcms2"].has("cmsPipelineGetPtrToLastStage", "cdecl"):
    cmsPipelineGetPtrToLastStage = _libs["lcms2"].get("cmsPipelineGetPtrToLastStage", "cdecl")
    cmsPipelineGetPtrToLastStage.argtypes = [POINTER(cmsPipeline)]
    cmsPipelineGetPtrToLastStage.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1209
if _libs["lcms2"].has("cmsPipelineEval16", "cdecl"):
    cmsPipelineEval16 = _libs["lcms2"].get("cmsPipelineEval16", "cdecl")
    cmsPipelineEval16.argtypes = [POINTER(cmsUInt16Number), POINTER(cmsUInt16Number), POINTER(cmsPipeline)]
    cmsPipelineEval16.restype = None

# /usr/include/lcms2.h: 1210
if _libs["lcms2"].has("cmsPipelineEvalFloat", "cdecl"):
    cmsPipelineEvalFloat = _libs["lcms2"].get("cmsPipelineEvalFloat", "cdecl")
    cmsPipelineEvalFloat.argtypes = [POINTER(cmsFloat32Number), POINTER(cmsFloat32Number), POINTER(cmsPipeline)]
    cmsPipelineEvalFloat.restype = None

# /usr/include/lcms2.h: 1211
if _libs["lcms2"].has("cmsPipelineEvalReverseFloat", "cdecl"):
    cmsPipelineEvalReverseFloat = _libs["lcms2"].get("cmsPipelineEvalReverseFloat", "cdecl")
    cmsPipelineEvalReverseFloat.argtypes = [POINTER(cmsFloat32Number), POINTER(cmsFloat32Number), POINTER(cmsFloat32Number), POINTER(cmsPipeline)]
    cmsPipelineEvalReverseFloat.restype = cmsBool

# /usr/include/lcms2.h: 1212
if _libs["lcms2"].has("cmsPipelineCat", "cdecl"):
    cmsPipelineCat = _libs["lcms2"].get("cmsPipelineCat", "cdecl")
    cmsPipelineCat.argtypes = [POINTER(cmsPipeline), POINTER(cmsPipeline)]
    cmsPipelineCat.restype = cmsBool

# /usr/include/lcms2.h: 1213
if _libs["lcms2"].has("cmsPipelineSetSaveAs8bitsFlag", "cdecl"):
    cmsPipelineSetSaveAs8bitsFlag = _libs["lcms2"].get("cmsPipelineSetSaveAs8bitsFlag", "cdecl")
    cmsPipelineSetSaveAs8bitsFlag.argtypes = [POINTER(cmsPipeline), cmsBool]
    cmsPipelineSetSaveAs8bitsFlag.restype = cmsBool

enum_anon_31 = c_int# /usr/include/lcms2.h: 1216

cmsAT_BEGIN = 0# /usr/include/lcms2.h: 1216

cmsAT_END = (cmsAT_BEGIN + 1)# /usr/include/lcms2.h: 1216

cmsStageLoc = enum_anon_31# /usr/include/lcms2.h: 1216

# /usr/include/lcms2.h: 1218
if _libs["lcms2"].has("cmsPipelineInsertStage", "cdecl"):
    cmsPipelineInsertStage = _libs["lcms2"].get("cmsPipelineInsertStage", "cdecl")
    cmsPipelineInsertStage.argtypes = [POINTER(cmsPipeline), cmsStageLoc, POINTER(cmsStage)]
    cmsPipelineInsertStage.restype = cmsBool

# /usr/include/lcms2.h: 1219
if _libs["lcms2"].has("cmsPipelineUnlinkStage", "cdecl"):
    cmsPipelineUnlinkStage = _libs["lcms2"].get("cmsPipelineUnlinkStage", "cdecl")
    cmsPipelineUnlinkStage.argtypes = [POINTER(cmsPipeline), cmsStageLoc, POINTER(POINTER(cmsStage))]
    cmsPipelineUnlinkStage.restype = None

# /usr/include/lcms2.h: 1226
if _libs["lcms2"].has("cmsPipelineCheckAndRetreiveStages", "cdecl"):
    _func = _libs["lcms2"].get("cmsPipelineCheckAndRetreiveStages", "cdecl")
    _restype = cmsBool
    _errcheck = None
    _argtypes = [POINTER(cmsPipeline), cmsUInt32Number]
    cmsPipelineCheckAndRetreiveStages = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/lcms2.h: 1230
if _libs["lcms2"].has("cmsStageAllocIdentity", "cdecl"):
    cmsStageAllocIdentity = _libs["lcms2"].get("cmsStageAllocIdentity", "cdecl")
    cmsStageAllocIdentity.argtypes = [cmsContext, cmsUInt32Number]
    cmsStageAllocIdentity.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1231
if _libs["lcms2"].has("cmsStageAllocToneCurves", "cdecl"):
    cmsStageAllocToneCurves = _libs["lcms2"].get("cmsStageAllocToneCurves", "cdecl")
    cmsStageAllocToneCurves.argtypes = [cmsContext, cmsUInt32Number, POINTER(POINTER(cmsToneCurve))]
    cmsStageAllocToneCurves.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1232
if _libs["lcms2"].has("cmsStageAllocMatrix", "cdecl"):
    cmsStageAllocMatrix = _libs["lcms2"].get("cmsStageAllocMatrix", "cdecl")
    cmsStageAllocMatrix.argtypes = [cmsContext, cmsUInt32Number, cmsUInt32Number, POINTER(cmsFloat64Number), POINTER(cmsFloat64Number)]
    cmsStageAllocMatrix.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1234
if _libs["lcms2"].has("cmsStageAllocCLut16bit", "cdecl"):
    cmsStageAllocCLut16bit = _libs["lcms2"].get("cmsStageAllocCLut16bit", "cdecl")
    cmsStageAllocCLut16bit.argtypes = [cmsContext, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number, POINTER(cmsUInt16Number)]
    cmsStageAllocCLut16bit.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1235
if _libs["lcms2"].has("cmsStageAllocCLutFloat", "cdecl"):
    cmsStageAllocCLutFloat = _libs["lcms2"].get("cmsStageAllocCLutFloat", "cdecl")
    cmsStageAllocCLutFloat.argtypes = [cmsContext, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number, POINTER(cmsFloat32Number)]
    cmsStageAllocCLutFloat.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1237
if _libs["lcms2"].has("cmsStageAllocCLut16bitGranular", "cdecl"):
    cmsStageAllocCLut16bitGranular = _libs["lcms2"].get("cmsStageAllocCLut16bitGranular", "cdecl")
    cmsStageAllocCLut16bitGranular.argtypes = [cmsContext, POINTER(cmsUInt32Number), cmsUInt32Number, cmsUInt32Number, POINTER(cmsUInt16Number)]
    cmsStageAllocCLut16bitGranular.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1238
if _libs["lcms2"].has("cmsStageAllocCLutFloatGranular", "cdecl"):
    cmsStageAllocCLutFloatGranular = _libs["lcms2"].get("cmsStageAllocCLutFloatGranular", "cdecl")
    cmsStageAllocCLutFloatGranular.argtypes = [cmsContext, POINTER(cmsUInt32Number), cmsUInt32Number, cmsUInt32Number, POINTER(cmsFloat32Number)]
    cmsStageAllocCLutFloatGranular.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1240
if _libs["lcms2"].has("cmsStageDup", "cdecl"):
    cmsStageDup = _libs["lcms2"].get("cmsStageDup", "cdecl")
    cmsStageDup.argtypes = [POINTER(cmsStage)]
    cmsStageDup.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1241
if _libs["lcms2"].has("cmsStageFree", "cdecl"):
    cmsStageFree = _libs["lcms2"].get("cmsStageFree", "cdecl")
    cmsStageFree.argtypes = [POINTER(cmsStage)]
    cmsStageFree.restype = None

# /usr/include/lcms2.h: 1242
if _libs["lcms2"].has("cmsStageNext", "cdecl"):
    cmsStageNext = _libs["lcms2"].get("cmsStageNext", "cdecl")
    cmsStageNext.argtypes = [POINTER(cmsStage)]
    cmsStageNext.restype = POINTER(cmsStage)

# /usr/include/lcms2.h: 1244
if _libs["lcms2"].has("cmsStageInputChannels", "cdecl"):
    cmsStageInputChannels = _libs["lcms2"].get("cmsStageInputChannels", "cdecl")
    cmsStageInputChannels.argtypes = [POINTER(cmsStage)]
    cmsStageInputChannels.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1245
if _libs["lcms2"].has("cmsStageOutputChannels", "cdecl"):
    cmsStageOutputChannels = _libs["lcms2"].get("cmsStageOutputChannels", "cdecl")
    cmsStageOutputChannels.argtypes = [POINTER(cmsStage)]
    cmsStageOutputChannels.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1246
if _libs["lcms2"].has("cmsStageType", "cdecl"):
    cmsStageType = _libs["lcms2"].get("cmsStageType", "cdecl")
    cmsStageType.argtypes = [POINTER(cmsStage)]
    cmsStageType.restype = cmsStageSignature

# /usr/include/lcms2.h: 1247
if _libs["lcms2"].has("cmsStageData", "cdecl"):
    cmsStageData = _libs["lcms2"].get("cmsStageData", "cdecl")
    cmsStageData.argtypes = [POINTER(cmsStage)]
    cmsStageData.restype = POINTER(c_ubyte)
    cmsStageData.errcheck = lambda v,*a : cast(v, c_void_p)

cmsSAMPLER16 = CFUNCTYPE(UNCHECKED(cmsInt32Number), POINTER(cmsUInt16Number), POINTER(cmsUInt16Number), POINTER(None))# /usr/include/lcms2.h: 1250

cmsSAMPLERFLOAT = CFUNCTYPE(UNCHECKED(cmsInt32Number), POINTER(cmsFloat32Number), POINTER(cmsFloat32Number), POINTER(None))# /usr/include/lcms2.h: 1254

# /usr/include/lcms2.h: 1262
if _libs["lcms2"].has("cmsStageSampleCLut16bit", "cdecl"):
    cmsStageSampleCLut16bit = _libs["lcms2"].get("cmsStageSampleCLut16bit", "cdecl")
    cmsStageSampleCLut16bit.argtypes = [POINTER(cmsStage), cmsSAMPLER16, POINTER(None), cmsUInt32Number]
    cmsStageSampleCLut16bit.restype = cmsBool

# /usr/include/lcms2.h: 1263
if _libs["lcms2"].has("cmsStageSampleCLutFloat", "cdecl"):
    cmsStageSampleCLutFloat = _libs["lcms2"].get("cmsStageSampleCLutFloat", "cdecl")
    cmsStageSampleCLutFloat.argtypes = [POINTER(cmsStage), cmsSAMPLERFLOAT, POINTER(None), cmsUInt32Number]
    cmsStageSampleCLutFloat.restype = cmsBool

# /usr/include/lcms2.h: 1266
if _libs["lcms2"].has("cmsSliceSpace16", "cdecl"):
    cmsSliceSpace16 = _libs["lcms2"].get("cmsSliceSpace16", "cdecl")
    cmsSliceSpace16.argtypes = [cmsUInt32Number, POINTER(cmsUInt32Number), cmsSAMPLER16, POINTER(None)]
    cmsSliceSpace16.restype = cmsBool

# /usr/include/lcms2.h: 1269
if _libs["lcms2"].has("cmsSliceSpaceFloat", "cdecl"):
    cmsSliceSpaceFloat = _libs["lcms2"].get("cmsSliceSpaceFloat", "cdecl")
    cmsSliceSpaceFloat.argtypes = [cmsUInt32Number, POINTER(cmsUInt32Number), cmsSAMPLERFLOAT, POINTER(None)]
    cmsSliceSpaceFloat.restype = cmsBool

# /usr/include/lcms2.h: 1274
class struct__cms_MLU_struct(Structure):
    pass

cmsMLU = struct__cms_MLU_struct# /usr/include/lcms2.h: 1274

# /usr/include/lcms2.h: 1279
if _libs["lcms2"].has("cmsMLUalloc", "cdecl"):
    cmsMLUalloc = _libs["lcms2"].get("cmsMLUalloc", "cdecl")
    cmsMLUalloc.argtypes = [cmsContext, cmsUInt32Number]
    cmsMLUalloc.restype = POINTER(cmsMLU)

# /usr/include/lcms2.h: 1280
if _libs["lcms2"].has("cmsMLUfree", "cdecl"):
    cmsMLUfree = _libs["lcms2"].get("cmsMLUfree", "cdecl")
    cmsMLUfree.argtypes = [POINTER(cmsMLU)]
    cmsMLUfree.restype = None

# /usr/include/lcms2.h: 1281
if _libs["lcms2"].has("cmsMLUdup", "cdecl"):
    cmsMLUdup = _libs["lcms2"].get("cmsMLUdup", "cdecl")
    cmsMLUdup.argtypes = [POINTER(cmsMLU)]
    cmsMLUdup.restype = POINTER(cmsMLU)

# /usr/include/lcms2.h: 1283
if _libs["lcms2"].has("cmsMLUsetASCII", "cdecl"):
    cmsMLUsetASCII = _libs["lcms2"].get("cmsMLUsetASCII", "cdecl")
    cmsMLUsetASCII.argtypes = [POINTER(cmsMLU), c_char * int(3), c_char * int(3), String]
    cmsMLUsetASCII.restype = cmsBool

# /usr/include/lcms2.h: 1286
if _libs["lcms2"].has("cmsMLUsetWide", "cdecl"):
    cmsMLUsetWide = _libs["lcms2"].get("cmsMLUsetWide", "cdecl")
    cmsMLUsetWide.argtypes = [POINTER(cmsMLU), c_char * int(3), c_char * int(3), POINTER(c_wchar)]
    cmsMLUsetWide.restype = cmsBool

# /usr/include/lcms2.h: 1290
if _libs["lcms2"].has("cmsMLUgetASCII", "cdecl"):
    cmsMLUgetASCII = _libs["lcms2"].get("cmsMLUgetASCII", "cdecl")
    cmsMLUgetASCII.argtypes = [POINTER(cmsMLU), c_char * int(3), c_char * int(3), String, cmsUInt32Number]
    cmsMLUgetASCII.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1294
if _libs["lcms2"].has("cmsMLUgetWide", "cdecl"):
    cmsMLUgetWide = _libs["lcms2"].get("cmsMLUgetWide", "cdecl")
    cmsMLUgetWide.argtypes = [POINTER(cmsMLU), c_char * int(3), c_char * int(3), POINTER(c_wchar), cmsUInt32Number]
    cmsMLUgetWide.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1298
if _libs["lcms2"].has("cmsMLUgetTranslation", "cdecl"):
    cmsMLUgetTranslation = _libs["lcms2"].get("cmsMLUgetTranslation", "cdecl")
    cmsMLUgetTranslation.argtypes = [POINTER(cmsMLU), c_char * int(3), c_char * int(3), c_char * int(3), c_char * int(3)]
    cmsMLUgetTranslation.restype = cmsBool

# /usr/include/lcms2.h: 1302
if _libs["lcms2"].has("cmsMLUtranslationsCount", "cdecl"):
    cmsMLUtranslationsCount = _libs["lcms2"].get("cmsMLUtranslationsCount", "cdecl")
    cmsMLUtranslationsCount.argtypes = [POINTER(cmsMLU)]
    cmsMLUtranslationsCount.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1304
if _libs["lcms2"].has("cmsMLUtranslationsCodes", "cdecl"):
    cmsMLUtranslationsCodes = _libs["lcms2"].get("cmsMLUtranslationsCodes", "cdecl")
    cmsMLUtranslationsCodes.argtypes = [POINTER(cmsMLU), cmsUInt32Number, c_char * int(3), c_char * int(3)]
    cmsMLUtranslationsCodes.restype = cmsBool

# /usr/include/lcms2.h: 1316
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'Ucr',
    'Bg',
    'Desc',
]
struct_anon_32._fields_ = [
    ('Ucr', POINTER(cmsToneCurve)),
    ('Bg', POINTER(cmsToneCurve)),
    ('Desc', POINTER(cmsMLU)),
]

cmsUcrBg = struct_anon_32# /usr/include/lcms2.h: 1316

# /usr/include/lcms2.h: 1338
class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'Frequency',
    'ScreenAngle',
    'SpotShape',
]
struct_anon_33._fields_ = [
    ('Frequency', cmsFloat64Number),
    ('ScreenAngle', cmsFloat64Number),
    ('SpotShape', cmsUInt32Number),
]

cmsScreeningChannel = struct_anon_33# /usr/include/lcms2.h: 1338

# /usr/include/lcms2.h: 1345
class struct_anon_34(Structure):
    pass

struct_anon_34.__slots__ = [
    'Flag',
    'nChannels',
    'Channels',
]
struct_anon_34._fields_ = [
    ('Flag', cmsUInt32Number),
    ('nChannels', cmsUInt32Number),
    ('Channels', cmsScreeningChannel * int(16)),
]

cmsScreening = struct_anon_34# /usr/include/lcms2.h: 1345

# /usr/include/lcms2.h: 1350
class struct__cms_NAMEDCOLORLIST_struct(Structure):
    pass

cmsNAMEDCOLORLIST = struct__cms_NAMEDCOLORLIST_struct# /usr/include/lcms2.h: 1350

# /usr/include/lcms2.h: 1352
if _libs["lcms2"].has("cmsAllocNamedColorList", "cdecl"):
    cmsAllocNamedColorList = _libs["lcms2"].get("cmsAllocNamedColorList", "cdecl")
    cmsAllocNamedColorList.argtypes = [cmsContext, cmsUInt32Number, cmsUInt32Number, String, String]
    cmsAllocNamedColorList.restype = POINTER(cmsNAMEDCOLORLIST)

# /usr/include/lcms2.h: 1357
if _libs["lcms2"].has("cmsFreeNamedColorList", "cdecl"):
    cmsFreeNamedColorList = _libs["lcms2"].get("cmsFreeNamedColorList", "cdecl")
    cmsFreeNamedColorList.argtypes = [POINTER(cmsNAMEDCOLORLIST)]
    cmsFreeNamedColorList.restype = None

# /usr/include/lcms2.h: 1358
if _libs["lcms2"].has("cmsDupNamedColorList", "cdecl"):
    cmsDupNamedColorList = _libs["lcms2"].get("cmsDupNamedColorList", "cdecl")
    cmsDupNamedColorList.argtypes = [POINTER(cmsNAMEDCOLORLIST)]
    cmsDupNamedColorList.restype = POINTER(cmsNAMEDCOLORLIST)

# /usr/include/lcms2.h: 1359
if _libs["lcms2"].has("cmsAppendNamedColor", "cdecl"):
    cmsAppendNamedColor = _libs["lcms2"].get("cmsAppendNamedColor", "cdecl")
    cmsAppendNamedColor.argtypes = [POINTER(cmsNAMEDCOLORLIST), String, cmsUInt16Number * int(3), cmsUInt16Number * int(16)]
    cmsAppendNamedColor.restype = cmsBool

# /usr/include/lcms2.h: 1363
if _libs["lcms2"].has("cmsNamedColorCount", "cdecl"):
    cmsNamedColorCount = _libs["lcms2"].get("cmsNamedColorCount", "cdecl")
    cmsNamedColorCount.argtypes = [POINTER(cmsNAMEDCOLORLIST)]
    cmsNamedColorCount.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1364
if _libs["lcms2"].has("cmsNamedColorIndex", "cdecl"):
    cmsNamedColorIndex = _libs["lcms2"].get("cmsNamedColorIndex", "cdecl")
    cmsNamedColorIndex.argtypes = [POINTER(cmsNAMEDCOLORLIST), String]
    cmsNamedColorIndex.restype = cmsInt32Number

# /usr/include/lcms2.h: 1366
if _libs["lcms2"].has("cmsNamedColorInfo", "cdecl"):
    cmsNamedColorInfo = _libs["lcms2"].get("cmsNamedColorInfo", "cdecl")
    cmsNamedColorInfo.argtypes = [POINTER(cmsNAMEDCOLORLIST), cmsUInt32Number, String, String, String, POINTER(cmsUInt16Number), POINTER(cmsUInt16Number)]
    cmsNamedColorInfo.restype = cmsBool

# /usr/include/lcms2.h: 1374
if _libs["lcms2"].has("cmsGetNamedColorList", "cdecl"):
    cmsGetNamedColorList = _libs["lcms2"].get("cmsGetNamedColorList", "cdecl")
    cmsGetNamedColorList.argtypes = [cmsHTRANSFORM]
    cmsGetNamedColorList.restype = POINTER(cmsNAMEDCOLORLIST)

# /usr/include/lcms2.h: 1391
class struct_anon_35(Structure):
    pass

struct_anon_35.__slots__ = [
    'deviceMfg',
    'deviceModel',
    'attributes',
    'technology',
    'ProfileID',
    'Manufacturer',
    'Model',
    'Description',
]
struct_anon_35._fields_ = [
    ('deviceMfg', cmsSignature),
    ('deviceModel', cmsSignature),
    ('attributes', cmsUInt64Number),
    ('technology', cmsTechnologySignature),
    ('ProfileID', cmsProfileID),
    ('Manufacturer', POINTER(cmsMLU)),
    ('Model', POINTER(cmsMLU)),
    ('Description', POINTER(cmsMLU)),
]

cmsPSEQDESC = struct_anon_35# /usr/include/lcms2.h: 1391

# /usr/include/lcms2.h: 1399
class struct_anon_36(Structure):
    pass

struct_anon_36.__slots__ = [
    'n',
    'ContextID',
    'seq',
]
struct_anon_36._fields_ = [
    ('n', cmsUInt32Number),
    ('ContextID', cmsContext),
    ('seq', POINTER(cmsPSEQDESC)),
]

cmsSEQ = struct_anon_36# /usr/include/lcms2.h: 1399

# /usr/include/lcms2.h: 1401
if _libs["lcms2"].has("cmsAllocProfileSequenceDescription", "cdecl"):
    cmsAllocProfileSequenceDescription = _libs["lcms2"].get("cmsAllocProfileSequenceDescription", "cdecl")
    cmsAllocProfileSequenceDescription.argtypes = [cmsContext, cmsUInt32Number]
    cmsAllocProfileSequenceDescription.restype = POINTER(cmsSEQ)

# /usr/include/lcms2.h: 1402
if _libs["lcms2"].has("cmsDupProfileSequenceDescription", "cdecl"):
    cmsDupProfileSequenceDescription = _libs["lcms2"].get("cmsDupProfileSequenceDescription", "cdecl")
    cmsDupProfileSequenceDescription.argtypes = [POINTER(cmsSEQ)]
    cmsDupProfileSequenceDescription.restype = POINTER(cmsSEQ)

# /usr/include/lcms2.h: 1403
if _libs["lcms2"].has("cmsFreeProfileSequenceDescription", "cdecl"):
    cmsFreeProfileSequenceDescription = _libs["lcms2"].get("cmsFreeProfileSequenceDescription", "cdecl")
    cmsFreeProfileSequenceDescription.argtypes = [POINTER(cmsSEQ)]
    cmsFreeProfileSequenceDescription.restype = None

# /usr/include/lcms2.h: 1407
class struct__cmsDICTentry_struct(Structure):
    pass

struct__cmsDICTentry_struct.__slots__ = [
    'Next',
    'DisplayName',
    'DisplayValue',
    'Name',
    'Value',
]
struct__cmsDICTentry_struct._fields_ = [
    ('Next', POINTER(struct__cmsDICTentry_struct)),
    ('DisplayName', POINTER(cmsMLU)),
    ('DisplayValue', POINTER(cmsMLU)),
    ('Name', POINTER(c_wchar)),
    ('Value', POINTER(c_wchar)),
]

cmsDICTentry = struct__cmsDICTentry_struct# /usr/include/lcms2.h: 1416

# /usr/include/lcms2.h: 1418
if _libs["lcms2"].has("cmsDictAlloc", "cdecl"):
    cmsDictAlloc = _libs["lcms2"].get("cmsDictAlloc", "cdecl")
    cmsDictAlloc.argtypes = [cmsContext]
    cmsDictAlloc.restype = cmsHANDLE

# /usr/include/lcms2.h: 1419
if _libs["lcms2"].has("cmsDictFree", "cdecl"):
    cmsDictFree = _libs["lcms2"].get("cmsDictFree", "cdecl")
    cmsDictFree.argtypes = [cmsHANDLE]
    cmsDictFree.restype = None

# /usr/include/lcms2.h: 1420
if _libs["lcms2"].has("cmsDictDup", "cdecl"):
    cmsDictDup = _libs["lcms2"].get("cmsDictDup", "cdecl")
    cmsDictDup.argtypes = [cmsHANDLE]
    cmsDictDup.restype = cmsHANDLE

# /usr/include/lcms2.h: 1422
if _libs["lcms2"].has("cmsDictAddEntry", "cdecl"):
    cmsDictAddEntry = _libs["lcms2"].get("cmsDictAddEntry", "cdecl")
    cmsDictAddEntry.argtypes = [cmsHANDLE, POINTER(c_wchar), POINTER(c_wchar), POINTER(cmsMLU), POINTER(cmsMLU)]
    cmsDictAddEntry.restype = cmsBool

# /usr/include/lcms2.h: 1423
if _libs["lcms2"].has("cmsDictGetEntryList", "cdecl"):
    cmsDictGetEntryList = _libs["lcms2"].get("cmsDictGetEntryList", "cdecl")
    cmsDictGetEntryList.argtypes = [cmsHANDLE]
    cmsDictGetEntryList.restype = POINTER(cmsDICTentry)

# /usr/include/lcms2.h: 1424
if _libs["lcms2"].has("cmsDictNextEntry", "cdecl"):
    cmsDictNextEntry = _libs["lcms2"].get("cmsDictNextEntry", "cdecl")
    cmsDictNextEntry.argtypes = [POINTER(cmsDICTentry)]
    cmsDictNextEntry.restype = POINTER(cmsDICTentry)

# /usr/include/lcms2.h: 1427
if _libs["lcms2"].has("cmsCreateProfilePlaceholder", "cdecl"):
    cmsCreateProfilePlaceholder = _libs["lcms2"].get("cmsCreateProfilePlaceholder", "cdecl")
    cmsCreateProfilePlaceholder.argtypes = [cmsContext]
    cmsCreateProfilePlaceholder.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1429
if _libs["lcms2"].has("cmsGetProfileContextID", "cdecl"):
    cmsGetProfileContextID = _libs["lcms2"].get("cmsGetProfileContextID", "cdecl")
    cmsGetProfileContextID.argtypes = [cmsHPROFILE]
    cmsGetProfileContextID.restype = cmsContext

# /usr/include/lcms2.h: 1430
if _libs["lcms2"].has("cmsGetTagCount", "cdecl"):
    cmsGetTagCount = _libs["lcms2"].get("cmsGetTagCount", "cdecl")
    cmsGetTagCount.argtypes = [cmsHPROFILE]
    cmsGetTagCount.restype = cmsInt32Number

# /usr/include/lcms2.h: 1431
if _libs["lcms2"].has("cmsGetTagSignature", "cdecl"):
    cmsGetTagSignature = _libs["lcms2"].get("cmsGetTagSignature", "cdecl")
    cmsGetTagSignature.argtypes = [cmsHPROFILE, cmsUInt32Number]
    cmsGetTagSignature.restype = cmsTagSignature

# /usr/include/lcms2.h: 1432
if _libs["lcms2"].has("cmsIsTag", "cdecl"):
    cmsIsTag = _libs["lcms2"].get("cmsIsTag", "cdecl")
    cmsIsTag.argtypes = [cmsHPROFILE, cmsTagSignature]
    cmsIsTag.restype = cmsBool

# /usr/include/lcms2.h: 1435
if _libs["lcms2"].has("cmsReadTag", "cdecl"):
    cmsReadTag = _libs["lcms2"].get("cmsReadTag", "cdecl")
    cmsReadTag.argtypes = [cmsHPROFILE, cmsTagSignature]
    cmsReadTag.restype = POINTER(c_ubyte)
    cmsReadTag.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/lcms2.h: 1436
if _libs["lcms2"].has("cmsWriteTag", "cdecl"):
    cmsWriteTag = _libs["lcms2"].get("cmsWriteTag", "cdecl")
    cmsWriteTag.argtypes = [cmsHPROFILE, cmsTagSignature, POINTER(None)]
    cmsWriteTag.restype = cmsBool

# /usr/include/lcms2.h: 1437
if _libs["lcms2"].has("cmsLinkTag", "cdecl"):
    cmsLinkTag = _libs["lcms2"].get("cmsLinkTag", "cdecl")
    cmsLinkTag.argtypes = [cmsHPROFILE, cmsTagSignature, cmsTagSignature]
    cmsLinkTag.restype = cmsBool

# /usr/include/lcms2.h: 1438
if _libs["lcms2"].has("cmsTagLinkedTo", "cdecl"):
    cmsTagLinkedTo = _libs["lcms2"].get("cmsTagLinkedTo", "cdecl")
    cmsTagLinkedTo.argtypes = [cmsHPROFILE, cmsTagSignature]
    cmsTagLinkedTo.restype = cmsTagSignature

# /usr/include/lcms2.h: 1441
if _libs["lcms2"].has("cmsReadRawTag", "cdecl"):
    cmsReadRawTag = _libs["lcms2"].get("cmsReadRawTag", "cdecl")
    cmsReadRawTag.argtypes = [cmsHPROFILE, cmsTagSignature, POINTER(None), cmsUInt32Number]
    cmsReadRawTag.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1442
if _libs["lcms2"].has("cmsWriteRawTag", "cdecl"):
    cmsWriteRawTag = _libs["lcms2"].get("cmsWriteRawTag", "cdecl")
    cmsWriteRawTag.argtypes = [cmsHPROFILE, cmsTagSignature, POINTER(None), cmsUInt32Number]
    cmsWriteRawTag.restype = cmsBool

# /usr/include/lcms2.h: 1450
if _libs["lcms2"].has("cmsGetHeaderFlags", "cdecl"):
    cmsGetHeaderFlags = _libs["lcms2"].get("cmsGetHeaderFlags", "cdecl")
    cmsGetHeaderFlags.argtypes = [cmsHPROFILE]
    cmsGetHeaderFlags.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1451
if _libs["lcms2"].has("cmsGetHeaderAttributes", "cdecl"):
    cmsGetHeaderAttributes = _libs["lcms2"].get("cmsGetHeaderAttributes", "cdecl")
    cmsGetHeaderAttributes.argtypes = [cmsHPROFILE, POINTER(cmsUInt64Number)]
    cmsGetHeaderAttributes.restype = None

# /usr/include/lcms2.h: 1452
if _libs["lcms2"].has("cmsGetHeaderProfileID", "cdecl"):
    cmsGetHeaderProfileID = _libs["lcms2"].get("cmsGetHeaderProfileID", "cdecl")
    cmsGetHeaderProfileID.argtypes = [cmsHPROFILE, POINTER(cmsUInt8Number)]
    cmsGetHeaderProfileID.restype = None

# /usr/include/lcms2.h: 1453
if _libs["lcms2"].has("cmsGetHeaderCreationDateTime", "cdecl"):
    cmsGetHeaderCreationDateTime = _libs["lcms2"].get("cmsGetHeaderCreationDateTime", "cdecl")
    cmsGetHeaderCreationDateTime.argtypes = [cmsHPROFILE, POINTER(struct_tm)]
    cmsGetHeaderCreationDateTime.restype = cmsBool

# /usr/include/lcms2.h: 1454
if _libs["lcms2"].has("cmsGetHeaderRenderingIntent", "cdecl"):
    cmsGetHeaderRenderingIntent = _libs["lcms2"].get("cmsGetHeaderRenderingIntent", "cdecl")
    cmsGetHeaderRenderingIntent.argtypes = [cmsHPROFILE]
    cmsGetHeaderRenderingIntent.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1456
if _libs["lcms2"].has("cmsSetHeaderFlags", "cdecl"):
    cmsSetHeaderFlags = _libs["lcms2"].get("cmsSetHeaderFlags", "cdecl")
    cmsSetHeaderFlags.argtypes = [cmsHPROFILE, cmsUInt32Number]
    cmsSetHeaderFlags.restype = None

# /usr/include/lcms2.h: 1457
if _libs["lcms2"].has("cmsGetHeaderManufacturer", "cdecl"):
    cmsGetHeaderManufacturer = _libs["lcms2"].get("cmsGetHeaderManufacturer", "cdecl")
    cmsGetHeaderManufacturer.argtypes = [cmsHPROFILE]
    cmsGetHeaderManufacturer.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1458
if _libs["lcms2"].has("cmsSetHeaderManufacturer", "cdecl"):
    cmsSetHeaderManufacturer = _libs["lcms2"].get("cmsSetHeaderManufacturer", "cdecl")
    cmsSetHeaderManufacturer.argtypes = [cmsHPROFILE, cmsUInt32Number]
    cmsSetHeaderManufacturer.restype = None

# /usr/include/lcms2.h: 1459
if _libs["lcms2"].has("cmsGetHeaderCreator", "cdecl"):
    cmsGetHeaderCreator = _libs["lcms2"].get("cmsGetHeaderCreator", "cdecl")
    cmsGetHeaderCreator.argtypes = [cmsHPROFILE]
    cmsGetHeaderCreator.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1460
if _libs["lcms2"].has("cmsGetHeaderModel", "cdecl"):
    cmsGetHeaderModel = _libs["lcms2"].get("cmsGetHeaderModel", "cdecl")
    cmsGetHeaderModel.argtypes = [cmsHPROFILE]
    cmsGetHeaderModel.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1461
if _libs["lcms2"].has("cmsSetHeaderModel", "cdecl"):
    cmsSetHeaderModel = _libs["lcms2"].get("cmsSetHeaderModel", "cdecl")
    cmsSetHeaderModel.argtypes = [cmsHPROFILE, cmsUInt32Number]
    cmsSetHeaderModel.restype = None

# /usr/include/lcms2.h: 1462
if _libs["lcms2"].has("cmsSetHeaderAttributes", "cdecl"):
    cmsSetHeaderAttributes = _libs["lcms2"].get("cmsSetHeaderAttributes", "cdecl")
    cmsSetHeaderAttributes.argtypes = [cmsHPROFILE, cmsUInt64Number]
    cmsSetHeaderAttributes.restype = None

# /usr/include/lcms2.h: 1463
if _libs["lcms2"].has("cmsSetHeaderProfileID", "cdecl"):
    cmsSetHeaderProfileID = _libs["lcms2"].get("cmsSetHeaderProfileID", "cdecl")
    cmsSetHeaderProfileID.argtypes = [cmsHPROFILE, POINTER(cmsUInt8Number)]
    cmsSetHeaderProfileID.restype = None

# /usr/include/lcms2.h: 1464
if _libs["lcms2"].has("cmsSetHeaderRenderingIntent", "cdecl"):
    cmsSetHeaderRenderingIntent = _libs["lcms2"].get("cmsSetHeaderRenderingIntent", "cdecl")
    cmsSetHeaderRenderingIntent.argtypes = [cmsHPROFILE, cmsUInt32Number]
    cmsSetHeaderRenderingIntent.restype = None

# /usr/include/lcms2.h: 1467
if _libs["lcms2"].has("cmsGetPCS", "cdecl"):
    cmsGetPCS = _libs["lcms2"].get("cmsGetPCS", "cdecl")
    cmsGetPCS.argtypes = [cmsHPROFILE]
    cmsGetPCS.restype = cmsColorSpaceSignature

# /usr/include/lcms2.h: 1468
if _libs["lcms2"].has("cmsSetPCS", "cdecl"):
    cmsSetPCS = _libs["lcms2"].get("cmsSetPCS", "cdecl")
    cmsSetPCS.argtypes = [cmsHPROFILE, cmsColorSpaceSignature]
    cmsSetPCS.restype = None

# /usr/include/lcms2.h: 1470
if _libs["lcms2"].has("cmsGetColorSpace", "cdecl"):
    cmsGetColorSpace = _libs["lcms2"].get("cmsGetColorSpace", "cdecl")
    cmsGetColorSpace.argtypes = [cmsHPROFILE]
    cmsGetColorSpace.restype = cmsColorSpaceSignature

# /usr/include/lcms2.h: 1471
if _libs["lcms2"].has("cmsSetColorSpace", "cdecl"):
    cmsSetColorSpace = _libs["lcms2"].get("cmsSetColorSpace", "cdecl")
    cmsSetColorSpace.argtypes = [cmsHPROFILE, cmsColorSpaceSignature]
    cmsSetColorSpace.restype = None

# /usr/include/lcms2.h: 1473
if _libs["lcms2"].has("cmsGetDeviceClass", "cdecl"):
    cmsGetDeviceClass = _libs["lcms2"].get("cmsGetDeviceClass", "cdecl")
    cmsGetDeviceClass.argtypes = [cmsHPROFILE]
    cmsGetDeviceClass.restype = cmsProfileClassSignature

# /usr/include/lcms2.h: 1474
if _libs["lcms2"].has("cmsSetDeviceClass", "cdecl"):
    cmsSetDeviceClass = _libs["lcms2"].get("cmsSetDeviceClass", "cdecl")
    cmsSetDeviceClass.argtypes = [cmsHPROFILE, cmsProfileClassSignature]
    cmsSetDeviceClass.restype = None

# /usr/include/lcms2.h: 1475
if _libs["lcms2"].has("cmsSetProfileVersion", "cdecl"):
    cmsSetProfileVersion = _libs["lcms2"].get("cmsSetProfileVersion", "cdecl")
    cmsSetProfileVersion.argtypes = [cmsHPROFILE, cmsFloat64Number]
    cmsSetProfileVersion.restype = None

# /usr/include/lcms2.h: 1476
if _libs["lcms2"].has("cmsGetProfileVersion", "cdecl"):
    cmsGetProfileVersion = _libs["lcms2"].get("cmsGetProfileVersion", "cdecl")
    cmsGetProfileVersion.argtypes = [cmsHPROFILE]
    cmsGetProfileVersion.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1478
if _libs["lcms2"].has("cmsGetEncodedICCversion", "cdecl"):
    cmsGetEncodedICCversion = _libs["lcms2"].get("cmsGetEncodedICCversion", "cdecl")
    cmsGetEncodedICCversion.argtypes = [cmsHPROFILE]
    cmsGetEncodedICCversion.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1479
if _libs["lcms2"].has("cmsSetEncodedICCversion", "cdecl"):
    cmsSetEncodedICCversion = _libs["lcms2"].get("cmsSetEncodedICCversion", "cdecl")
    cmsSetEncodedICCversion.argtypes = [cmsHPROFILE, cmsUInt32Number]
    cmsSetEncodedICCversion.restype = None

# /usr/include/lcms2.h: 1486
if _libs["lcms2"].has("cmsIsIntentSupported", "cdecl"):
    cmsIsIntentSupported = _libs["lcms2"].get("cmsIsIntentSupported", "cdecl")
    cmsIsIntentSupported.argtypes = [cmsHPROFILE, cmsUInt32Number, cmsUInt32Number]
    cmsIsIntentSupported.restype = cmsBool

# /usr/include/lcms2.h: 1487
if _libs["lcms2"].has("cmsIsMatrixShaper", "cdecl"):
    cmsIsMatrixShaper = _libs["lcms2"].get("cmsIsMatrixShaper", "cdecl")
    cmsIsMatrixShaper.argtypes = [cmsHPROFILE]
    cmsIsMatrixShaper.restype = cmsBool

# /usr/include/lcms2.h: 1488
if _libs["lcms2"].has("cmsIsCLUT", "cdecl"):
    cmsIsCLUT = _libs["lcms2"].get("cmsIsCLUT", "cdecl")
    cmsIsCLUT.argtypes = [cmsHPROFILE, cmsUInt32Number, cmsUInt32Number]
    cmsIsCLUT.restype = cmsBool

# /usr/include/lcms2.h: 1491
if _libs["lcms2"].has("_cmsICCcolorSpace", "cdecl"):
    _cmsICCcolorSpace = _libs["lcms2"].get("_cmsICCcolorSpace", "cdecl")
    _cmsICCcolorSpace.argtypes = [c_int]
    _cmsICCcolorSpace.restype = cmsColorSpaceSignature

# /usr/include/lcms2.h: 1492
if _libs["lcms2"].has("_cmsLCMScolorSpace", "cdecl"):
    _cmsLCMScolorSpace = _libs["lcms2"].get("_cmsLCMScolorSpace", "cdecl")
    _cmsLCMScolorSpace.argtypes = [cmsColorSpaceSignature]
    _cmsLCMScolorSpace.restype = c_int

# /usr/include/lcms2.h: 1494
if _libs["lcms2"].has("cmsChannelsOf", "cdecl"):
    cmsChannelsOf = _libs["lcms2"].get("cmsChannelsOf", "cdecl")
    cmsChannelsOf.argtypes = [cmsColorSpaceSignature]
    cmsChannelsOf.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1497
if _libs["lcms2"].has("cmsFormatterForColorspaceOfProfile", "cdecl"):
    cmsFormatterForColorspaceOfProfile = _libs["lcms2"].get("cmsFormatterForColorspaceOfProfile", "cdecl")
    cmsFormatterForColorspaceOfProfile.argtypes = [cmsHPROFILE, cmsUInt32Number, cmsBool]
    cmsFormatterForColorspaceOfProfile.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1498
if _libs["lcms2"].has("cmsFormatterForPCSOfProfile", "cdecl"):
    cmsFormatterForPCSOfProfile = _libs["lcms2"].get("cmsFormatterForPCSOfProfile", "cdecl")
    cmsFormatterForPCSOfProfile.argtypes = [cmsHPROFILE, cmsUInt32Number, cmsBool]
    cmsFormatterForPCSOfProfile.restype = cmsUInt32Number

enum_anon_37 = c_int# /usr/include/lcms2.h: 1507

cmsInfoDescription = 0# /usr/include/lcms2.h: 1507

cmsInfoManufacturer = 1# /usr/include/lcms2.h: 1507

cmsInfoModel = 2# /usr/include/lcms2.h: 1507

cmsInfoCopyright = 3# /usr/include/lcms2.h: 1507

cmsInfoType = enum_anon_37# /usr/include/lcms2.h: 1507

# /usr/include/lcms2.h: 1509
if _libs["lcms2"].has("cmsGetProfileInfo", "cdecl"):
    cmsGetProfileInfo = _libs["lcms2"].get("cmsGetProfileInfo", "cdecl")
    cmsGetProfileInfo.argtypes = [cmsHPROFILE, cmsInfoType, c_char * int(3), c_char * int(3), POINTER(c_wchar), cmsUInt32Number]
    cmsGetProfileInfo.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1513
if _libs["lcms2"].has("cmsGetProfileInfoASCII", "cdecl"):
    cmsGetProfileInfoASCII = _libs["lcms2"].get("cmsGetProfileInfoASCII", "cdecl")
    cmsGetProfileInfoASCII.argtypes = [cmsHPROFILE, cmsInfoType, c_char * int(3), c_char * int(3), String, cmsUInt32Number]
    cmsGetProfileInfoASCII.restype = cmsUInt32Number

# /usr/include/lcms2_plugin.h: 112
class struct__cms_io_handler(Structure):
    pass

cmsIOHANDLER = struct__cms_io_handler# /usr/include/lcms2.h: 1519

# /usr/include/lcms2.h: 1521
if _libs["lcms2"].has("cmsOpenIOhandlerFromFile", "cdecl"):
    cmsOpenIOhandlerFromFile = _libs["lcms2"].get("cmsOpenIOhandlerFromFile", "cdecl")
    cmsOpenIOhandlerFromFile.argtypes = [cmsContext, String, String]
    cmsOpenIOhandlerFromFile.restype = POINTER(cmsIOHANDLER)

# /usr/include/lcms2.h: 1522
if _libs["lcms2"].has("cmsOpenIOhandlerFromStream", "cdecl"):
    cmsOpenIOhandlerFromStream = _libs["lcms2"].get("cmsOpenIOhandlerFromStream", "cdecl")
    cmsOpenIOhandlerFromStream.argtypes = [cmsContext, POINTER(FILE)]
    cmsOpenIOhandlerFromStream.restype = POINTER(cmsIOHANDLER)

# /usr/include/lcms2.h: 1523
if _libs["lcms2"].has("cmsOpenIOhandlerFromMem", "cdecl"):
    cmsOpenIOhandlerFromMem = _libs["lcms2"].get("cmsOpenIOhandlerFromMem", "cdecl")
    cmsOpenIOhandlerFromMem.argtypes = [cmsContext, POINTER(None), cmsUInt32Number, String]
    cmsOpenIOhandlerFromMem.restype = POINTER(cmsIOHANDLER)

# /usr/include/lcms2.h: 1524
if _libs["lcms2"].has("cmsOpenIOhandlerFromNULL", "cdecl"):
    cmsOpenIOhandlerFromNULL = _libs["lcms2"].get("cmsOpenIOhandlerFromNULL", "cdecl")
    cmsOpenIOhandlerFromNULL.argtypes = [cmsContext]
    cmsOpenIOhandlerFromNULL.restype = POINTER(cmsIOHANDLER)

# /usr/include/lcms2.h: 1525
if _libs["lcms2"].has("cmsGetProfileIOhandler", "cdecl"):
    cmsGetProfileIOhandler = _libs["lcms2"].get("cmsGetProfileIOhandler", "cdecl")
    cmsGetProfileIOhandler.argtypes = [cmsHPROFILE]
    cmsGetProfileIOhandler.restype = POINTER(cmsIOHANDLER)

# /usr/include/lcms2.h: 1526
if _libs["lcms2"].has("cmsCloseIOhandler", "cdecl"):
    cmsCloseIOhandler = _libs["lcms2"].get("cmsCloseIOhandler", "cdecl")
    cmsCloseIOhandler.argtypes = [POINTER(cmsIOHANDLER)]
    cmsCloseIOhandler.restype = cmsBool

# /usr/include/lcms2.h: 1530
if _libs["lcms2"].has("cmsMD5computeID", "cdecl"):
    cmsMD5computeID = _libs["lcms2"].get("cmsMD5computeID", "cdecl")
    cmsMD5computeID.argtypes = [cmsHPROFILE]
    cmsMD5computeID.restype = cmsBool

# /usr/include/lcms2.h: 1534
if _libs["lcms2"].has("cmsOpenProfileFromFile", "cdecl"):
    cmsOpenProfileFromFile = _libs["lcms2"].get("cmsOpenProfileFromFile", "cdecl")
    cmsOpenProfileFromFile.argtypes = [String, String]
    cmsOpenProfileFromFile.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1535
if _libs["lcms2"].has("cmsOpenProfileFromFileTHR", "cdecl"):
    cmsOpenProfileFromFileTHR = _libs["lcms2"].get("cmsOpenProfileFromFileTHR", "cdecl")
    cmsOpenProfileFromFileTHR.argtypes = [cmsContext, String, String]
    cmsOpenProfileFromFileTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1536
if _libs["lcms2"].has("cmsOpenProfileFromStream", "cdecl"):
    cmsOpenProfileFromStream = _libs["lcms2"].get("cmsOpenProfileFromStream", "cdecl")
    cmsOpenProfileFromStream.argtypes = [POINTER(FILE), String]
    cmsOpenProfileFromStream.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1537
if _libs["lcms2"].has("cmsOpenProfileFromStreamTHR", "cdecl"):
    cmsOpenProfileFromStreamTHR = _libs["lcms2"].get("cmsOpenProfileFromStreamTHR", "cdecl")
    cmsOpenProfileFromStreamTHR.argtypes = [cmsContext, POINTER(FILE), String]
    cmsOpenProfileFromStreamTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1538
if _libs["lcms2"].has("cmsOpenProfileFromMem", "cdecl"):
    cmsOpenProfileFromMem = _libs["lcms2"].get("cmsOpenProfileFromMem", "cdecl")
    cmsOpenProfileFromMem.argtypes = [POINTER(None), cmsUInt32Number]
    cmsOpenProfileFromMem.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1539
if _libs["lcms2"].has("cmsOpenProfileFromMemTHR", "cdecl"):
    cmsOpenProfileFromMemTHR = _libs["lcms2"].get("cmsOpenProfileFromMemTHR", "cdecl")
    cmsOpenProfileFromMemTHR.argtypes = [cmsContext, POINTER(None), cmsUInt32Number]
    cmsOpenProfileFromMemTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1540
if _libs["lcms2"].has("cmsOpenProfileFromIOhandlerTHR", "cdecl"):
    cmsOpenProfileFromIOhandlerTHR = _libs["lcms2"].get("cmsOpenProfileFromIOhandlerTHR", "cdecl")
    cmsOpenProfileFromIOhandlerTHR.argtypes = [cmsContext, POINTER(cmsIOHANDLER)]
    cmsOpenProfileFromIOhandlerTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1541
if _libs["lcms2"].has("cmsOpenProfileFromIOhandler2THR", "cdecl"):
    cmsOpenProfileFromIOhandler2THR = _libs["lcms2"].get("cmsOpenProfileFromIOhandler2THR", "cdecl")
    cmsOpenProfileFromIOhandler2THR.argtypes = [cmsContext, POINTER(cmsIOHANDLER), cmsBool]
    cmsOpenProfileFromIOhandler2THR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1542
if _libs["lcms2"].has("cmsCloseProfile", "cdecl"):
    cmsCloseProfile = _libs["lcms2"].get("cmsCloseProfile", "cdecl")
    cmsCloseProfile.argtypes = [cmsHPROFILE]
    cmsCloseProfile.restype = cmsBool

# /usr/include/lcms2.h: 1544
if _libs["lcms2"].has("cmsSaveProfileToFile", "cdecl"):
    cmsSaveProfileToFile = _libs["lcms2"].get("cmsSaveProfileToFile", "cdecl")
    cmsSaveProfileToFile.argtypes = [cmsHPROFILE, String]
    cmsSaveProfileToFile.restype = cmsBool

# /usr/include/lcms2.h: 1545
if _libs["lcms2"].has("cmsSaveProfileToStream", "cdecl"):
    cmsSaveProfileToStream = _libs["lcms2"].get("cmsSaveProfileToStream", "cdecl")
    cmsSaveProfileToStream.argtypes = [cmsHPROFILE, POINTER(FILE)]
    cmsSaveProfileToStream.restype = cmsBool

# /usr/include/lcms2.h: 1546
if _libs["lcms2"].has("cmsSaveProfileToMem", "cdecl"):
    cmsSaveProfileToMem = _libs["lcms2"].get("cmsSaveProfileToMem", "cdecl")
    cmsSaveProfileToMem.argtypes = [cmsHPROFILE, POINTER(None), POINTER(cmsUInt32Number)]
    cmsSaveProfileToMem.restype = cmsBool

# /usr/include/lcms2.h: 1547
if _libs["lcms2"].has("cmsSaveProfileToIOhandler", "cdecl"):
    cmsSaveProfileToIOhandler = _libs["lcms2"].get("cmsSaveProfileToIOhandler", "cdecl")
    cmsSaveProfileToIOhandler.argtypes = [cmsHPROFILE, POINTER(cmsIOHANDLER)]
    cmsSaveProfileToIOhandler.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1551
if _libs["lcms2"].has("cmsCreateRGBProfileTHR", "cdecl"):
    cmsCreateRGBProfileTHR = _libs["lcms2"].get("cmsCreateRGBProfileTHR", "cdecl")
    cmsCreateRGBProfileTHR.argtypes = [cmsContext, POINTER(cmsCIExyY), POINTER(cmsCIExyYTRIPLE), POINTER(cmsToneCurve) * int(3)]
    cmsCreateRGBProfileTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1556
if _libs["lcms2"].has("cmsCreateRGBProfile", "cdecl"):
    cmsCreateRGBProfile = _libs["lcms2"].get("cmsCreateRGBProfile", "cdecl")
    cmsCreateRGBProfile.argtypes = [POINTER(cmsCIExyY), POINTER(cmsCIExyYTRIPLE), POINTER(cmsToneCurve) * int(3)]
    cmsCreateRGBProfile.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1560
if _libs["lcms2"].has("cmsCreateGrayProfileTHR", "cdecl"):
    cmsCreateGrayProfileTHR = _libs["lcms2"].get("cmsCreateGrayProfileTHR", "cdecl")
    cmsCreateGrayProfileTHR.argtypes = [cmsContext, POINTER(cmsCIExyY), POINTER(cmsToneCurve)]
    cmsCreateGrayProfileTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1564
if _libs["lcms2"].has("cmsCreateGrayProfile", "cdecl"):
    cmsCreateGrayProfile = _libs["lcms2"].get("cmsCreateGrayProfile", "cdecl")
    cmsCreateGrayProfile.argtypes = [POINTER(cmsCIExyY), POINTER(cmsToneCurve)]
    cmsCreateGrayProfile.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1567
if _libs["lcms2"].has("cmsCreateLinearizationDeviceLinkTHR", "cdecl"):
    cmsCreateLinearizationDeviceLinkTHR = _libs["lcms2"].get("cmsCreateLinearizationDeviceLinkTHR", "cdecl")
    cmsCreateLinearizationDeviceLinkTHR.argtypes = [cmsContext, cmsColorSpaceSignature, POINTER(POINTER(cmsToneCurve))]
    cmsCreateLinearizationDeviceLinkTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1571
if _libs["lcms2"].has("cmsCreateLinearizationDeviceLink", "cdecl"):
    cmsCreateLinearizationDeviceLink = _libs["lcms2"].get("cmsCreateLinearizationDeviceLink", "cdecl")
    cmsCreateLinearizationDeviceLink.argtypes = [cmsColorSpaceSignature, POINTER(POINTER(cmsToneCurve))]
    cmsCreateLinearizationDeviceLink.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1574
if _libs["lcms2"].has("cmsCreateInkLimitingDeviceLinkTHR", "cdecl"):
    cmsCreateInkLimitingDeviceLinkTHR = _libs["lcms2"].get("cmsCreateInkLimitingDeviceLinkTHR", "cdecl")
    cmsCreateInkLimitingDeviceLinkTHR.argtypes = [cmsContext, cmsColorSpaceSignature, cmsFloat64Number]
    cmsCreateInkLimitingDeviceLinkTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1577
if _libs["lcms2"].has("cmsCreateInkLimitingDeviceLink", "cdecl"):
    cmsCreateInkLimitingDeviceLink = _libs["lcms2"].get("cmsCreateInkLimitingDeviceLink", "cdecl")
    cmsCreateInkLimitingDeviceLink.argtypes = [cmsColorSpaceSignature, cmsFloat64Number]
    cmsCreateInkLimitingDeviceLink.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1580
if _libs["lcms2"].has("cmsCreateLab2ProfileTHR", "cdecl"):
    cmsCreateLab2ProfileTHR = _libs["lcms2"].get("cmsCreateLab2ProfileTHR", "cdecl")
    cmsCreateLab2ProfileTHR.argtypes = [cmsContext, POINTER(cmsCIExyY)]
    cmsCreateLab2ProfileTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1581
if _libs["lcms2"].has("cmsCreateLab2Profile", "cdecl"):
    cmsCreateLab2Profile = _libs["lcms2"].get("cmsCreateLab2Profile", "cdecl")
    cmsCreateLab2Profile.argtypes = [POINTER(cmsCIExyY)]
    cmsCreateLab2Profile.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1582
if _libs["lcms2"].has("cmsCreateLab4ProfileTHR", "cdecl"):
    cmsCreateLab4ProfileTHR = _libs["lcms2"].get("cmsCreateLab4ProfileTHR", "cdecl")
    cmsCreateLab4ProfileTHR.argtypes = [cmsContext, POINTER(cmsCIExyY)]
    cmsCreateLab4ProfileTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1583
if _libs["lcms2"].has("cmsCreateLab4Profile", "cdecl"):
    cmsCreateLab4Profile = _libs["lcms2"].get("cmsCreateLab4Profile", "cdecl")
    cmsCreateLab4Profile.argtypes = [POINTER(cmsCIExyY)]
    cmsCreateLab4Profile.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1585
if _libs["lcms2"].has("cmsCreateXYZProfileTHR", "cdecl"):
    cmsCreateXYZProfileTHR = _libs["lcms2"].get("cmsCreateXYZProfileTHR", "cdecl")
    cmsCreateXYZProfileTHR.argtypes = [cmsContext]
    cmsCreateXYZProfileTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1586
if _libs["lcms2"].has("cmsCreateXYZProfile", "cdecl"):
    cmsCreateXYZProfile = _libs["lcms2"].get("cmsCreateXYZProfile", "cdecl")
    cmsCreateXYZProfile.argtypes = []
    cmsCreateXYZProfile.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1588
if _libs["lcms2"].has("cmsCreate_sRGBProfileTHR", "cdecl"):
    cmsCreate_sRGBProfileTHR = _libs["lcms2"].get("cmsCreate_sRGBProfileTHR", "cdecl")
    cmsCreate_sRGBProfileTHR.argtypes = [cmsContext]
    cmsCreate_sRGBProfileTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1589
if _libs["lcms2"].has("cmsCreate_sRGBProfile", "cdecl"):
    cmsCreate_sRGBProfile = _libs["lcms2"].get("cmsCreate_sRGBProfile", "cdecl")
    cmsCreate_sRGBProfile.argtypes = []
    cmsCreate_sRGBProfile.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1591
if _libs["lcms2"].has("cmsCreateBCHSWabstractProfileTHR", "cdecl"):
    cmsCreateBCHSWabstractProfileTHR = _libs["lcms2"].get("cmsCreateBCHSWabstractProfileTHR", "cdecl")
    cmsCreateBCHSWabstractProfileTHR.argtypes = [cmsContext, cmsUInt32Number, cmsFloat64Number, cmsFloat64Number, cmsFloat64Number, cmsFloat64Number, cmsUInt32Number, cmsUInt32Number]
    cmsCreateBCHSWabstractProfileTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1600
if _libs["lcms2"].has("cmsCreateBCHSWabstractProfile", "cdecl"):
    cmsCreateBCHSWabstractProfile = _libs["lcms2"].get("cmsCreateBCHSWabstractProfile", "cdecl")
    cmsCreateBCHSWabstractProfile.argtypes = [cmsUInt32Number, cmsFloat64Number, cmsFloat64Number, cmsFloat64Number, cmsFloat64Number, cmsUInt32Number, cmsUInt32Number]
    cmsCreateBCHSWabstractProfile.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1608
if _libs["lcms2"].has("cmsCreateNULLProfileTHR", "cdecl"):
    cmsCreateNULLProfileTHR = _libs["lcms2"].get("cmsCreateNULLProfileTHR", "cdecl")
    cmsCreateNULLProfileTHR.argtypes = [cmsContext]
    cmsCreateNULLProfileTHR.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1609
if _libs["lcms2"].has("cmsCreateNULLProfile", "cdecl"):
    cmsCreateNULLProfile = _libs["lcms2"].get("cmsCreateNULLProfile", "cdecl")
    cmsCreateNULLProfile.argtypes = []
    cmsCreateNULLProfile.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1612
if _libs["lcms2"].has("cmsTransform2DeviceLink", "cdecl"):
    cmsTransform2DeviceLink = _libs["lcms2"].get("cmsTransform2DeviceLink", "cdecl")
    cmsTransform2DeviceLink.argtypes = [cmsHTRANSFORM, cmsFloat64Number, cmsUInt32Number]
    cmsTransform2DeviceLink.restype = cmsHPROFILE

# /usr/include/lcms2.h: 1631
if _libs["lcms2"].has("cmsGetSupportedIntents", "cdecl"):
    cmsGetSupportedIntents = _libs["lcms2"].get("cmsGetSupportedIntents", "cdecl")
    cmsGetSupportedIntents.argtypes = [cmsUInt32Number, POINTER(cmsUInt32Number), POINTER(POINTER(c_char))]
    cmsGetSupportedIntents.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1632
if _libs["lcms2"].has("cmsGetSupportedIntentsTHR", "cdecl"):
    cmsGetSupportedIntentsTHR = _libs["lcms2"].get("cmsGetSupportedIntentsTHR", "cdecl")
    cmsGetSupportedIntentsTHR.argtypes = [cmsContext, cmsUInt32Number, POINTER(cmsUInt32Number), POINTER(POINTER(c_char))]
    cmsGetSupportedIntentsTHR.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1674
if _libs["lcms2"].has("cmsCreateTransformTHR", "cdecl"):
    cmsCreateTransformTHR = _libs["lcms2"].get("cmsCreateTransformTHR", "cdecl")
    cmsCreateTransformTHR.argtypes = [cmsContext, cmsHPROFILE, cmsUInt32Number, cmsHPROFILE, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number]
    cmsCreateTransformTHR.restype = cmsHTRANSFORM

# /usr/include/lcms2.h: 1682
if _libs["lcms2"].has("cmsCreateTransform", "cdecl"):
    cmsCreateTransform = _libs["lcms2"].get("cmsCreateTransform", "cdecl")
    cmsCreateTransform.argtypes = [cmsHPROFILE, cmsUInt32Number, cmsHPROFILE, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number]
    cmsCreateTransform.restype = cmsHTRANSFORM

# /usr/include/lcms2.h: 1689
if _libs["lcms2"].has("cmsCreateProofingTransformTHR", "cdecl"):
    cmsCreateProofingTransformTHR = _libs["lcms2"].get("cmsCreateProofingTransformTHR", "cdecl")
    cmsCreateProofingTransformTHR.argtypes = [cmsContext, cmsHPROFILE, cmsUInt32Number, cmsHPROFILE, cmsUInt32Number, cmsHPROFILE, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number]
    cmsCreateProofingTransformTHR.restype = cmsHTRANSFORM

# /usr/include/lcms2.h: 1699
if _libs["lcms2"].has("cmsCreateProofingTransform", "cdecl"):
    cmsCreateProofingTransform = _libs["lcms2"].get("cmsCreateProofingTransform", "cdecl")
    cmsCreateProofingTransform.argtypes = [cmsHPROFILE, cmsUInt32Number, cmsHPROFILE, cmsUInt32Number, cmsHPROFILE, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number]
    cmsCreateProofingTransform.restype = cmsHTRANSFORM

# /usr/include/lcms2.h: 1708
if _libs["lcms2"].has("cmsCreateMultiprofileTransformTHR", "cdecl"):
    cmsCreateMultiprofileTransformTHR = _libs["lcms2"].get("cmsCreateMultiprofileTransformTHR", "cdecl")
    cmsCreateMultiprofileTransformTHR.argtypes = [cmsContext, POINTER(cmsHPROFILE), cmsUInt32Number, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number]
    cmsCreateMultiprofileTransformTHR.restype = cmsHTRANSFORM

# /usr/include/lcms2.h: 1717
if _libs["lcms2"].has("cmsCreateMultiprofileTransform", "cdecl"):
    cmsCreateMultiprofileTransform = _libs["lcms2"].get("cmsCreateMultiprofileTransform", "cdecl")
    cmsCreateMultiprofileTransform.argtypes = [POINTER(cmsHPROFILE), cmsUInt32Number, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number]
    cmsCreateMultiprofileTransform.restype = cmsHTRANSFORM

# /usr/include/lcms2.h: 1725
if _libs["lcms2"].has("cmsCreateExtendedTransform", "cdecl"):
    cmsCreateExtendedTransform = _libs["lcms2"].get("cmsCreateExtendedTransform", "cdecl")
    cmsCreateExtendedTransform.argtypes = [cmsContext, cmsUInt32Number, POINTER(cmsHPROFILE), POINTER(cmsBool), POINTER(cmsUInt32Number), POINTER(cmsFloat64Number), cmsHPROFILE, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number]
    cmsCreateExtendedTransform.restype = cmsHTRANSFORM

# /usr/include/lcms2.h: 1736
if _libs["lcms2"].has("cmsDeleteTransform", "cdecl"):
    cmsDeleteTransform = _libs["lcms2"].get("cmsDeleteTransform", "cdecl")
    cmsDeleteTransform.argtypes = [cmsHTRANSFORM]
    cmsDeleteTransform.restype = None

# /usr/include/lcms2.h: 1738
if _libs["lcms2"].has("cmsDoTransform", "cdecl"):
    cmsDoTransform = _libs["lcms2"].get("cmsDoTransform", "cdecl")
    cmsDoTransform.argtypes = [cmsHTRANSFORM, POINTER(None), POINTER(None), cmsUInt32Number]
    cmsDoTransform.restype = None

# /usr/include/lcms2.h: 1743
if _libs["lcms2"].has("cmsDoTransformStride", "cdecl"):
    cmsDoTransformStride = _libs["lcms2"].get("cmsDoTransformStride", "cdecl")
    cmsDoTransformStride.argtypes = [cmsHTRANSFORM, POINTER(None), POINTER(None), cmsUInt32Number, cmsUInt32Number]
    cmsDoTransformStride.restype = None

# /usr/include/lcms2.h: 1749
if _libs["lcms2"].has("cmsDoTransformLineStride", "cdecl"):
    cmsDoTransformLineStride = _libs["lcms2"].get("cmsDoTransformLineStride", "cdecl")
    cmsDoTransformLineStride.argtypes = [cmsHTRANSFORM, POINTER(None), POINTER(None), cmsUInt32Number, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number, cmsUInt32Number]
    cmsDoTransformLineStride.restype = None

# /usr/include/lcms2.h: 1760
if _libs["lcms2"].has("cmsSetAlarmCodes", "cdecl"):
    cmsSetAlarmCodes = _libs["lcms2"].get("cmsSetAlarmCodes", "cdecl")
    cmsSetAlarmCodes.argtypes = [cmsUInt16Number * int(16)]
    cmsSetAlarmCodes.restype = None

# /usr/include/lcms2.h: 1761
if _libs["lcms2"].has("cmsGetAlarmCodes", "cdecl"):
    cmsGetAlarmCodes = _libs["lcms2"].get("cmsGetAlarmCodes", "cdecl")
    cmsGetAlarmCodes.argtypes = [cmsUInt16Number * int(16)]
    cmsGetAlarmCodes.restype = None

# /usr/include/lcms2.h: 1764
if _libs["lcms2"].has("cmsSetAlarmCodesTHR", "cdecl"):
    cmsSetAlarmCodesTHR = _libs["lcms2"].get("cmsSetAlarmCodesTHR", "cdecl")
    cmsSetAlarmCodesTHR.argtypes = [cmsContext, cmsUInt16Number * int(16)]
    cmsSetAlarmCodesTHR.restype = None

# /usr/include/lcms2.h: 1766
if _libs["lcms2"].has("cmsGetAlarmCodesTHR", "cdecl"):
    cmsGetAlarmCodesTHR = _libs["lcms2"].get("cmsGetAlarmCodesTHR", "cdecl")
    cmsGetAlarmCodesTHR.argtypes = [cmsContext, cmsUInt16Number * int(16)]
    cmsGetAlarmCodesTHR.restype = None

# /usr/include/lcms2.h: 1772
if _libs["lcms2"].has("cmsSetAdaptationState", "cdecl"):
    cmsSetAdaptationState = _libs["lcms2"].get("cmsSetAdaptationState", "cdecl")
    cmsSetAdaptationState.argtypes = [cmsFloat64Number]
    cmsSetAdaptationState.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1773
if _libs["lcms2"].has("cmsSetAdaptationStateTHR", "cdecl"):
    cmsSetAdaptationStateTHR = _libs["lcms2"].get("cmsSetAdaptationStateTHR", "cdecl")
    cmsSetAdaptationStateTHR.argtypes = [cmsContext, cmsFloat64Number]
    cmsSetAdaptationStateTHR.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1778
if _libs["lcms2"].has("cmsGetTransformContextID", "cdecl"):
    cmsGetTransformContextID = _libs["lcms2"].get("cmsGetTransformContextID", "cdecl")
    cmsGetTransformContextID.argtypes = [cmsHTRANSFORM]
    cmsGetTransformContextID.restype = cmsContext

# /usr/include/lcms2.h: 1781
if _libs["lcms2"].has("cmsGetTransformInputFormat", "cdecl"):
    cmsGetTransformInputFormat = _libs["lcms2"].get("cmsGetTransformInputFormat", "cdecl")
    cmsGetTransformInputFormat.argtypes = [cmsHTRANSFORM]
    cmsGetTransformInputFormat.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1782
if _libs["lcms2"].has("cmsGetTransformOutputFormat", "cdecl"):
    cmsGetTransformOutputFormat = _libs["lcms2"].get("cmsGetTransformOutputFormat", "cdecl")
    cmsGetTransformOutputFormat.argtypes = [cmsHTRANSFORM]
    cmsGetTransformOutputFormat.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1785
if _libs["lcms2"].has("cmsChangeBuffersFormat", "cdecl"):
    cmsChangeBuffersFormat = _libs["lcms2"].get("cmsChangeBuffersFormat", "cdecl")
    cmsChangeBuffersFormat.argtypes = [cmsHTRANSFORM, cmsUInt32Number, cmsUInt32Number]
    cmsChangeBuffersFormat.restype = cmsBool

enum_anon_38 = c_int# /usr/include/lcms2.h: 1793

cmsPS_RESOURCE_CSA = 0# /usr/include/lcms2.h: 1793

cmsPS_RESOURCE_CRD = (cmsPS_RESOURCE_CSA + 1)# /usr/include/lcms2.h: 1793

cmsPSResourceType = enum_anon_38# /usr/include/lcms2.h: 1793

# /usr/include/lcms2.h: 1796
if _libs["lcms2"].has("cmsGetPostScriptColorResource", "cdecl"):
    cmsGetPostScriptColorResource = _libs["lcms2"].get("cmsGetPostScriptColorResource", "cdecl")
    cmsGetPostScriptColorResource.argtypes = [cmsContext, cmsPSResourceType, cmsHPROFILE, cmsUInt32Number, cmsUInt32Number, POINTER(cmsIOHANDLER)]
    cmsGetPostScriptColorResource.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1803
if _libs["lcms2"].has("cmsGetPostScriptCSA", "cdecl"):
    cmsGetPostScriptCSA = _libs["lcms2"].get("cmsGetPostScriptCSA", "cdecl")
    cmsGetPostScriptCSA.argtypes = [cmsContext, cmsHPROFILE, cmsUInt32Number, cmsUInt32Number, POINTER(None), cmsUInt32Number]
    cmsGetPostScriptCSA.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1804
if _libs["lcms2"].has("cmsGetPostScriptCRD", "cdecl"):
    cmsGetPostScriptCRD = _libs["lcms2"].get("cmsGetPostScriptCRD", "cdecl")
    cmsGetPostScriptCRD.argtypes = [cmsContext, cmsHPROFILE, cmsUInt32Number, cmsUInt32Number, POINTER(None), cmsUInt32Number]
    cmsGetPostScriptCRD.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1809
if _libs["lcms2"].has("cmsIT8Alloc", "cdecl"):
    cmsIT8Alloc = _libs["lcms2"].get("cmsIT8Alloc", "cdecl")
    cmsIT8Alloc.argtypes = [cmsContext]
    cmsIT8Alloc.restype = cmsHANDLE

# /usr/include/lcms2.h: 1810
if _libs["lcms2"].has("cmsIT8Free", "cdecl"):
    cmsIT8Free = _libs["lcms2"].get("cmsIT8Free", "cdecl")
    cmsIT8Free.argtypes = [cmsHANDLE]
    cmsIT8Free.restype = None

# /usr/include/lcms2.h: 1813
if _libs["lcms2"].has("cmsIT8TableCount", "cdecl"):
    cmsIT8TableCount = _libs["lcms2"].get("cmsIT8TableCount", "cdecl")
    cmsIT8TableCount.argtypes = [cmsHANDLE]
    cmsIT8TableCount.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1814
if _libs["lcms2"].has("cmsIT8SetTable", "cdecl"):
    cmsIT8SetTable = _libs["lcms2"].get("cmsIT8SetTable", "cdecl")
    cmsIT8SetTable.argtypes = [cmsHANDLE, cmsUInt32Number]
    cmsIT8SetTable.restype = cmsInt32Number

# /usr/include/lcms2.h: 1817
if _libs["lcms2"].has("cmsIT8LoadFromFile", "cdecl"):
    cmsIT8LoadFromFile = _libs["lcms2"].get("cmsIT8LoadFromFile", "cdecl")
    cmsIT8LoadFromFile.argtypes = [cmsContext, String]
    cmsIT8LoadFromFile.restype = cmsHANDLE

# /usr/include/lcms2.h: 1818
if _libs["lcms2"].has("cmsIT8LoadFromMem", "cdecl"):
    cmsIT8LoadFromMem = _libs["lcms2"].get("cmsIT8LoadFromMem", "cdecl")
    cmsIT8LoadFromMem.argtypes = [cmsContext, POINTER(None), cmsUInt32Number]
    cmsIT8LoadFromMem.restype = cmsHANDLE

# /usr/include/lcms2.h: 1821
if _libs["lcms2"].has("cmsIT8SaveToFile", "cdecl"):
    cmsIT8SaveToFile = _libs["lcms2"].get("cmsIT8SaveToFile", "cdecl")
    cmsIT8SaveToFile.argtypes = [cmsHANDLE, String]
    cmsIT8SaveToFile.restype = cmsBool

# /usr/include/lcms2.h: 1822
if _libs["lcms2"].has("cmsIT8SaveToMem", "cdecl"):
    cmsIT8SaveToMem = _libs["lcms2"].get("cmsIT8SaveToMem", "cdecl")
    cmsIT8SaveToMem.argtypes = [cmsHANDLE, POINTER(None), POINTER(cmsUInt32Number)]
    cmsIT8SaveToMem.restype = cmsBool

# /usr/include/lcms2.h: 1825
if _libs["lcms2"].has("cmsIT8GetSheetType", "cdecl"):
    cmsIT8GetSheetType = _libs["lcms2"].get("cmsIT8GetSheetType", "cdecl")
    cmsIT8GetSheetType.argtypes = [cmsHANDLE]
    cmsIT8GetSheetType.restype = c_char_p

# /usr/include/lcms2.h: 1826
if _libs["lcms2"].has("cmsIT8SetSheetType", "cdecl"):
    cmsIT8SetSheetType = _libs["lcms2"].get("cmsIT8SetSheetType", "cdecl")
    cmsIT8SetSheetType.argtypes = [cmsHANDLE, String]
    cmsIT8SetSheetType.restype = cmsBool

# /usr/include/lcms2.h: 1828
if _libs["lcms2"].has("cmsIT8SetComment", "cdecl"):
    cmsIT8SetComment = _libs["lcms2"].get("cmsIT8SetComment", "cdecl")
    cmsIT8SetComment.argtypes = [cmsHANDLE, String]
    cmsIT8SetComment.restype = cmsBool

# /usr/include/lcms2.h: 1830
if _libs["lcms2"].has("cmsIT8SetPropertyStr", "cdecl"):
    cmsIT8SetPropertyStr = _libs["lcms2"].get("cmsIT8SetPropertyStr", "cdecl")
    cmsIT8SetPropertyStr.argtypes = [cmsHANDLE, String, String]
    cmsIT8SetPropertyStr.restype = cmsBool

# /usr/include/lcms2.h: 1831
if _libs["lcms2"].has("cmsIT8SetPropertyDbl", "cdecl"):
    cmsIT8SetPropertyDbl = _libs["lcms2"].get("cmsIT8SetPropertyDbl", "cdecl")
    cmsIT8SetPropertyDbl.argtypes = [cmsHANDLE, String, cmsFloat64Number]
    cmsIT8SetPropertyDbl.restype = cmsBool

# /usr/include/lcms2.h: 1832
if _libs["lcms2"].has("cmsIT8SetPropertyHex", "cdecl"):
    cmsIT8SetPropertyHex = _libs["lcms2"].get("cmsIT8SetPropertyHex", "cdecl")
    cmsIT8SetPropertyHex.argtypes = [cmsHANDLE, String, cmsUInt32Number]
    cmsIT8SetPropertyHex.restype = cmsBool

# /usr/include/lcms2.h: 1833
if _libs["lcms2"].has("cmsIT8SetPropertyMulti", "cdecl"):
    cmsIT8SetPropertyMulti = _libs["lcms2"].get("cmsIT8SetPropertyMulti", "cdecl")
    cmsIT8SetPropertyMulti.argtypes = [cmsHANDLE, String, String, String]
    cmsIT8SetPropertyMulti.restype = cmsBool

# /usr/include/lcms2.h: 1834
if _libs["lcms2"].has("cmsIT8SetPropertyUncooked", "cdecl"):
    cmsIT8SetPropertyUncooked = _libs["lcms2"].get("cmsIT8SetPropertyUncooked", "cdecl")
    cmsIT8SetPropertyUncooked.argtypes = [cmsHANDLE, String, String]
    cmsIT8SetPropertyUncooked.restype = cmsBool

# /usr/include/lcms2.h: 1837
if _libs["lcms2"].has("cmsIT8GetProperty", "cdecl"):
    cmsIT8GetProperty = _libs["lcms2"].get("cmsIT8GetProperty", "cdecl")
    cmsIT8GetProperty.argtypes = [cmsHANDLE, String]
    cmsIT8GetProperty.restype = c_char_p

# /usr/include/lcms2.h: 1838
if _libs["lcms2"].has("cmsIT8GetPropertyDbl", "cdecl"):
    cmsIT8GetPropertyDbl = _libs["lcms2"].get("cmsIT8GetPropertyDbl", "cdecl")
    cmsIT8GetPropertyDbl.argtypes = [cmsHANDLE, String]
    cmsIT8GetPropertyDbl.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1839
if _libs["lcms2"].has("cmsIT8GetPropertyMulti", "cdecl"):
    cmsIT8GetPropertyMulti = _libs["lcms2"].get("cmsIT8GetPropertyMulti", "cdecl")
    cmsIT8GetPropertyMulti.argtypes = [cmsHANDLE, String, String]
    cmsIT8GetPropertyMulti.restype = c_char_p

# /usr/include/lcms2.h: 1840
if _libs["lcms2"].has("cmsIT8EnumProperties", "cdecl"):
    cmsIT8EnumProperties = _libs["lcms2"].get("cmsIT8EnumProperties", "cdecl")
    cmsIT8EnumProperties.argtypes = [cmsHANDLE, POINTER(POINTER(POINTER(c_char)))]
    cmsIT8EnumProperties.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1841
if _libs["lcms2"].has("cmsIT8EnumPropertyMulti", "cdecl"):
    cmsIT8EnumPropertyMulti = _libs["lcms2"].get("cmsIT8EnumPropertyMulti", "cdecl")
    cmsIT8EnumPropertyMulti.argtypes = [cmsHANDLE, String, POINTER(POINTER(POINTER(c_char)))]
    cmsIT8EnumPropertyMulti.restype = cmsUInt32Number

# /usr/include/lcms2.h: 1844
if _libs["lcms2"].has("cmsIT8GetDataRowCol", "cdecl"):
    cmsIT8GetDataRowCol = _libs["lcms2"].get("cmsIT8GetDataRowCol", "cdecl")
    cmsIT8GetDataRowCol.argtypes = [cmsHANDLE, c_int, c_int]
    cmsIT8GetDataRowCol.restype = c_char_p

# /usr/include/lcms2.h: 1845
if _libs["lcms2"].has("cmsIT8GetDataRowColDbl", "cdecl"):
    cmsIT8GetDataRowColDbl = _libs["lcms2"].get("cmsIT8GetDataRowColDbl", "cdecl")
    cmsIT8GetDataRowColDbl.argtypes = [cmsHANDLE, c_int, c_int]
    cmsIT8GetDataRowColDbl.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1847
if _libs["lcms2"].has("cmsIT8SetDataRowCol", "cdecl"):
    cmsIT8SetDataRowCol = _libs["lcms2"].get("cmsIT8SetDataRowCol", "cdecl")
    cmsIT8SetDataRowCol.argtypes = [cmsHANDLE, c_int, c_int, String]
    cmsIT8SetDataRowCol.restype = cmsBool

# /usr/include/lcms2.h: 1850
if _libs["lcms2"].has("cmsIT8SetDataRowColDbl", "cdecl"):
    cmsIT8SetDataRowColDbl = _libs["lcms2"].get("cmsIT8SetDataRowColDbl", "cdecl")
    cmsIT8SetDataRowColDbl.argtypes = [cmsHANDLE, c_int, c_int, cmsFloat64Number]
    cmsIT8SetDataRowColDbl.restype = cmsBool

# /usr/include/lcms2.h: 1853
if _libs["lcms2"].has("cmsIT8GetData", "cdecl"):
    cmsIT8GetData = _libs["lcms2"].get("cmsIT8GetData", "cdecl")
    cmsIT8GetData.argtypes = [cmsHANDLE, String, String]
    cmsIT8GetData.restype = c_char_p

# /usr/include/lcms2.h: 1856
if _libs["lcms2"].has("cmsIT8GetDataDbl", "cdecl"):
    cmsIT8GetDataDbl = _libs["lcms2"].get("cmsIT8GetDataDbl", "cdecl")
    cmsIT8GetDataDbl.argtypes = [cmsHANDLE, String, String]
    cmsIT8GetDataDbl.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1858
if _libs["lcms2"].has("cmsIT8SetData", "cdecl"):
    cmsIT8SetData = _libs["lcms2"].get("cmsIT8SetData", "cdecl")
    cmsIT8SetData.argtypes = [cmsHANDLE, String, String, String]
    cmsIT8SetData.restype = cmsBool

# /usr/include/lcms2.h: 1862
if _libs["lcms2"].has("cmsIT8SetDataDbl", "cdecl"):
    cmsIT8SetDataDbl = _libs["lcms2"].get("cmsIT8SetDataDbl", "cdecl")
    cmsIT8SetDataDbl.argtypes = [cmsHANDLE, String, String, cmsFloat64Number]
    cmsIT8SetDataDbl.restype = cmsBool

# /usr/include/lcms2.h: 1866
if _libs["lcms2"].has("cmsIT8FindDataFormat", "cdecl"):
    cmsIT8FindDataFormat = _libs["lcms2"].get("cmsIT8FindDataFormat", "cdecl")
    cmsIT8FindDataFormat.argtypes = [cmsHANDLE, String]
    cmsIT8FindDataFormat.restype = c_int

# /usr/include/lcms2.h: 1867
if _libs["lcms2"].has("cmsIT8SetDataFormat", "cdecl"):
    cmsIT8SetDataFormat = _libs["lcms2"].get("cmsIT8SetDataFormat", "cdecl")
    cmsIT8SetDataFormat.argtypes = [cmsHANDLE, c_int, String]
    cmsIT8SetDataFormat.restype = cmsBool

# /usr/include/lcms2.h: 1868
if _libs["lcms2"].has("cmsIT8EnumDataFormat", "cdecl"):
    cmsIT8EnumDataFormat = _libs["lcms2"].get("cmsIT8EnumDataFormat", "cdecl")
    cmsIT8EnumDataFormat.argtypes = [cmsHANDLE, POINTER(POINTER(POINTER(c_char)))]
    cmsIT8EnumDataFormat.restype = c_int

# /usr/include/lcms2.h: 1870
if _libs["lcms2"].has("cmsIT8GetPatchName", "cdecl"):
    cmsIT8GetPatchName = _libs["lcms2"].get("cmsIT8GetPatchName", "cdecl")
    cmsIT8GetPatchName.argtypes = [cmsHANDLE, c_int, String]
    cmsIT8GetPatchName.restype = c_char_p

# /usr/include/lcms2.h: 1871
if _libs["lcms2"].has("cmsIT8GetPatchByName", "cdecl"):
    cmsIT8GetPatchByName = _libs["lcms2"].get("cmsIT8GetPatchByName", "cdecl")
    cmsIT8GetPatchByName.argtypes = [cmsHANDLE, String]
    cmsIT8GetPatchByName.restype = c_int

# /usr/include/lcms2.h: 1874
if _libs["lcms2"].has("cmsIT8SetTableByLabel", "cdecl"):
    cmsIT8SetTableByLabel = _libs["lcms2"].get("cmsIT8SetTableByLabel", "cdecl")
    cmsIT8SetTableByLabel.argtypes = [cmsHANDLE, String, String, String]
    cmsIT8SetTableByLabel.restype = c_int

# /usr/include/lcms2.h: 1876
if _libs["lcms2"].has("cmsIT8SetIndexColumn", "cdecl"):
    cmsIT8SetIndexColumn = _libs["lcms2"].get("cmsIT8SetIndexColumn", "cdecl")
    cmsIT8SetIndexColumn.argtypes = [cmsHANDLE, String]
    cmsIT8SetIndexColumn.restype = cmsBool

# /usr/include/lcms2.h: 1879
if _libs["lcms2"].has("cmsIT8DefineDblFormat", "cdecl"):
    cmsIT8DefineDblFormat = _libs["lcms2"].get("cmsIT8DefineDblFormat", "cdecl")
    cmsIT8DefineDblFormat.argtypes = [cmsHANDLE, String]
    cmsIT8DefineDblFormat.restype = None

# /usr/include/lcms2.h: 1883
if _libs["lcms2"].has("cmsGBDAlloc", "cdecl"):
    cmsGBDAlloc = _libs["lcms2"].get("cmsGBDAlloc", "cdecl")
    cmsGBDAlloc.argtypes = [cmsContext]
    cmsGBDAlloc.restype = cmsHANDLE

# /usr/include/lcms2.h: 1884
if _libs["lcms2"].has("cmsGBDFree", "cdecl"):
    cmsGBDFree = _libs["lcms2"].get("cmsGBDFree", "cdecl")
    cmsGBDFree.argtypes = [cmsHANDLE]
    cmsGBDFree.restype = None

# /usr/include/lcms2.h: 1885
if _libs["lcms2"].has("cmsGDBAddPoint", "cdecl"):
    cmsGDBAddPoint = _libs["lcms2"].get("cmsGDBAddPoint", "cdecl")
    cmsGDBAddPoint.argtypes = [cmsHANDLE, POINTER(cmsCIELab)]
    cmsGDBAddPoint.restype = cmsBool

# /usr/include/lcms2.h: 1886
if _libs["lcms2"].has("cmsGDBCompute", "cdecl"):
    cmsGDBCompute = _libs["lcms2"].get("cmsGDBCompute", "cdecl")
    cmsGDBCompute.argtypes = [cmsHANDLE, cmsUInt32Number]
    cmsGDBCompute.restype = cmsBool

# /usr/include/lcms2.h: 1887
if _libs["lcms2"].has("cmsGDBCheckPoint", "cdecl"):
    cmsGDBCheckPoint = _libs["lcms2"].get("cmsGDBCheckPoint", "cdecl")
    cmsGDBCheckPoint.argtypes = [cmsHANDLE, POINTER(cmsCIELab)]
    cmsGDBCheckPoint.restype = cmsBool

# /usr/include/lcms2.h: 1892
if _libs["lcms2"].has("cmsDetectBlackPoint", "cdecl"):
    cmsDetectBlackPoint = _libs["lcms2"].get("cmsDetectBlackPoint", "cdecl")
    cmsDetectBlackPoint.argtypes = [POINTER(cmsCIEXYZ), cmsHPROFILE, cmsUInt32Number, cmsUInt32Number]
    cmsDetectBlackPoint.restype = cmsBool

# /usr/include/lcms2.h: 1893
if _libs["lcms2"].has("cmsDetectDestinationBlackPoint", "cdecl"):
    cmsDetectDestinationBlackPoint = _libs["lcms2"].get("cmsDetectDestinationBlackPoint", "cdecl")
    cmsDetectDestinationBlackPoint.argtypes = [POINTER(cmsCIEXYZ), cmsHPROFILE, cmsUInt32Number, cmsUInt32Number]
    cmsDetectDestinationBlackPoint.restype = cmsBool

# /usr/include/lcms2.h: 1896
if _libs["lcms2"].has("cmsDetectTAC", "cdecl"):
    cmsDetectTAC = _libs["lcms2"].get("cmsDetectTAC", "cdecl")
    cmsDetectTAC.argtypes = [cmsHPROFILE]
    cmsDetectTAC.restype = cmsFloat64Number

# /usr/include/lcms2.h: 1900
if _libs["lcms2"].has("cmsDesaturateLab", "cdecl"):
    cmsDesaturateLab = _libs["lcms2"].get("cmsDesaturateLab", "cdecl")
    cmsDesaturateLab.argtypes = [POINTER(cmsCIELab), c_double, c_double, c_double, c_double]
    cmsDesaturateLab.restype = cmsBool

# /usr/include/lcms2_plugin.h: 74
class struct_anon_58(Structure):
    pass

struct_anon_58.__slots__ = [
    'n',
]
struct_anon_58._fields_ = [
    ('n', cmsFloat64Number * int(3)),
]

cmsVEC3 = struct_anon_58# /usr/include/lcms2_plugin.h: 74

# /usr/include/lcms2_plugin.h: 80
class struct_anon_59(Structure):
    pass

struct_anon_59.__slots__ = [
    'v',
]
struct_anon_59._fields_ = [
    ('v', cmsVEC3 * int(3)),
]

cmsMAT3 = struct_anon_59# /usr/include/lcms2_plugin.h: 80

# /usr/include/lcms2_plugin.h: 82
if _libs["lcms2"].has("_cmsVEC3init", "cdecl"):
    _cmsVEC3init = _libs["lcms2"].get("_cmsVEC3init", "cdecl")
    _cmsVEC3init.argtypes = [POINTER(cmsVEC3), cmsFloat64Number, cmsFloat64Number, cmsFloat64Number]
    _cmsVEC3init.restype = None

# /usr/include/lcms2_plugin.h: 83
if _libs["lcms2"].has("_cmsVEC3minus", "cdecl"):
    _cmsVEC3minus = _libs["lcms2"].get("_cmsVEC3minus", "cdecl")
    _cmsVEC3minus.argtypes = [POINTER(cmsVEC3), POINTER(cmsVEC3), POINTER(cmsVEC3)]
    _cmsVEC3minus.restype = None

# /usr/include/lcms2_plugin.h: 84
if _libs["lcms2"].has("_cmsVEC3cross", "cdecl"):
    _cmsVEC3cross = _libs["lcms2"].get("_cmsVEC3cross", "cdecl")
    _cmsVEC3cross.argtypes = [POINTER(cmsVEC3), POINTER(cmsVEC3), POINTER(cmsVEC3)]
    _cmsVEC3cross.restype = None

# /usr/include/lcms2_plugin.h: 85
if _libs["lcms2"].has("_cmsVEC3dot", "cdecl"):
    _cmsVEC3dot = _libs["lcms2"].get("_cmsVEC3dot", "cdecl")
    _cmsVEC3dot.argtypes = [POINTER(cmsVEC3), POINTER(cmsVEC3)]
    _cmsVEC3dot.restype = cmsFloat64Number

# /usr/include/lcms2_plugin.h: 86
if _libs["lcms2"].has("_cmsVEC3length", "cdecl"):
    _cmsVEC3length = _libs["lcms2"].get("_cmsVEC3length", "cdecl")
    _cmsVEC3length.argtypes = [POINTER(cmsVEC3)]
    _cmsVEC3length.restype = cmsFloat64Number

# /usr/include/lcms2_plugin.h: 87
if _libs["lcms2"].has("_cmsVEC3distance", "cdecl"):
    _cmsVEC3distance = _libs["lcms2"].get("_cmsVEC3distance", "cdecl")
    _cmsVEC3distance.argtypes = [POINTER(cmsVEC3), POINTER(cmsVEC3)]
    _cmsVEC3distance.restype = cmsFloat64Number

# /usr/include/lcms2_plugin.h: 89
if _libs["lcms2"].has("_cmsMAT3identity", "cdecl"):
    _cmsMAT3identity = _libs["lcms2"].get("_cmsMAT3identity", "cdecl")
    _cmsMAT3identity.argtypes = [POINTER(cmsMAT3)]
    _cmsMAT3identity.restype = None

# /usr/include/lcms2_plugin.h: 90
if _libs["lcms2"].has("_cmsMAT3isIdentity", "cdecl"):
    _cmsMAT3isIdentity = _libs["lcms2"].get("_cmsMAT3isIdentity", "cdecl")
    _cmsMAT3isIdentity.argtypes = [POINTER(cmsMAT3)]
    _cmsMAT3isIdentity.restype = cmsBool

# /usr/include/lcms2_plugin.h: 91
if _libs["lcms2"].has("_cmsMAT3per", "cdecl"):
    _cmsMAT3per = _libs["lcms2"].get("_cmsMAT3per", "cdecl")
    _cmsMAT3per.argtypes = [POINTER(cmsMAT3), POINTER(cmsMAT3), POINTER(cmsMAT3)]
    _cmsMAT3per.restype = None

# /usr/include/lcms2_plugin.h: 92
if _libs["lcms2"].has("_cmsMAT3inverse", "cdecl"):
    _cmsMAT3inverse = _libs["lcms2"].get("_cmsMAT3inverse", "cdecl")
    _cmsMAT3inverse.argtypes = [POINTER(cmsMAT3), POINTER(cmsMAT3)]
    _cmsMAT3inverse.restype = cmsBool

# /usr/include/lcms2_plugin.h: 93
if _libs["lcms2"].has("_cmsMAT3solve", "cdecl"):
    _cmsMAT3solve = _libs["lcms2"].get("_cmsMAT3solve", "cdecl")
    _cmsMAT3solve.argtypes = [POINTER(cmsVEC3), POINTER(cmsMAT3), POINTER(cmsVEC3)]
    _cmsMAT3solve.restype = cmsBool

# /usr/include/lcms2_plugin.h: 94
if _libs["lcms2"].has("_cmsMAT3eval", "cdecl"):
    _cmsMAT3eval = _libs["lcms2"].get("_cmsMAT3eval", "cdecl")
    _cmsMAT3eval.argtypes = [POINTER(cmsVEC3), POINTER(cmsMAT3), POINTER(cmsVEC3)]
    _cmsMAT3eval.restype = None

# /usr/include/lcms2_plugin.h: 99
if _libs["lcms2"].has("cmsSignalError", "cdecl"):
    _func = _libs["lcms2"].get("cmsSignalError", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [cmsContext, cmsUInt32Number, String]
    cmsSignalError = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/lcms2_plugin.h: 103
if _libs["lcms2"].has("_cmsMalloc", "cdecl"):
    _cmsMalloc = _libs["lcms2"].get("_cmsMalloc", "cdecl")
    _cmsMalloc.argtypes = [cmsContext, cmsUInt32Number]
    _cmsMalloc.restype = POINTER(c_ubyte)
    _cmsMalloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/lcms2_plugin.h: 104
if _libs["lcms2"].has("_cmsMallocZero", "cdecl"):
    _cmsMallocZero = _libs["lcms2"].get("_cmsMallocZero", "cdecl")
    _cmsMallocZero.argtypes = [cmsContext, cmsUInt32Number]
    _cmsMallocZero.restype = POINTER(c_ubyte)
    _cmsMallocZero.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/lcms2_plugin.h: 105
if _libs["lcms2"].has("_cmsCalloc", "cdecl"):
    _cmsCalloc = _libs["lcms2"].get("_cmsCalloc", "cdecl")
    _cmsCalloc.argtypes = [cmsContext, cmsUInt32Number, cmsUInt32Number]
    _cmsCalloc.restype = POINTER(c_ubyte)
    _cmsCalloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/lcms2_plugin.h: 106
if _libs["lcms2"].has("_cmsRealloc", "cdecl"):
    _cmsRealloc = _libs["lcms2"].get("_cmsRealloc", "cdecl")
    _cmsRealloc.argtypes = [cmsContext, POINTER(None), cmsUInt32Number]
    _cmsRealloc.restype = POINTER(c_ubyte)
    _cmsRealloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/lcms2_plugin.h: 107
if _libs["lcms2"].has("_cmsFree", "cdecl"):
    _cmsFree = _libs["lcms2"].get("_cmsFree", "cdecl")
    _cmsFree.argtypes = [cmsContext, POINTER(None)]
    _cmsFree.restype = None

# /usr/include/lcms2_plugin.h: 108
if _libs["lcms2"].has("_cmsDupMem", "cdecl"):
    _cmsDupMem = _libs["lcms2"].get("_cmsDupMem", "cdecl")
    _cmsDupMem.argtypes = [cmsContext, POINTER(None), cmsUInt32Number]
    _cmsDupMem.restype = POINTER(c_ubyte)
    _cmsDupMem.errcheck = lambda v,*a : cast(v, c_void_p)

struct__cms_io_handler.__slots__ = [
    'stream',
    'ContextID',
    'UsedSpace',
    'ReportedSize',
    'PhysicalFile',
    'Read',
    'Seek',
    'Close',
    'Tell',
    'Write',
]
struct__cms_io_handler._fields_ = [
    ('stream', POINTER(None)),
    ('ContextID', cmsContext),
    ('UsedSpace', cmsUInt32Number),
    ('ReportedSize', cmsUInt32Number),
    ('PhysicalFile', c_char * int(256)),
    ('Read', CFUNCTYPE(UNCHECKED(cmsUInt32Number), POINTER(struct__cms_io_handler), POINTER(None), cmsUInt32Number, cmsUInt32Number)),
    ('Seek', CFUNCTYPE(UNCHECKED(cmsBool), POINTER(struct__cms_io_handler), cmsUInt32Number)),
    ('Close', CFUNCTYPE(UNCHECKED(cmsBool), POINTER(struct__cms_io_handler))),
    ('Tell', CFUNCTYPE(UNCHECKED(cmsUInt32Number), POINTER(struct__cms_io_handler))),
    ('Write', CFUNCTYPE(UNCHECKED(cmsBool), POINTER(struct__cms_io_handler), cmsUInt32Number, POINTER(None))),
]

# /usr/include/lcms2_plugin.h: 132
if _libs["lcms2"].has("_cmsAdjustEndianess16", "cdecl"):
    _cmsAdjustEndianess16 = _libs["lcms2"].get("_cmsAdjustEndianess16", "cdecl")
    _cmsAdjustEndianess16.argtypes = [cmsUInt16Number]
    _cmsAdjustEndianess16.restype = cmsUInt16Number

# /usr/include/lcms2_plugin.h: 133
if _libs["lcms2"].has("_cmsAdjustEndianess32", "cdecl"):
    _cmsAdjustEndianess32 = _libs["lcms2"].get("_cmsAdjustEndianess32", "cdecl")
    _cmsAdjustEndianess32.argtypes = [cmsUInt32Number]
    _cmsAdjustEndianess32.restype = cmsUInt32Number

# /usr/include/lcms2_plugin.h: 134
if _libs["lcms2"].has("_cmsAdjustEndianess64", "cdecl"):
    _cmsAdjustEndianess64 = _libs["lcms2"].get("_cmsAdjustEndianess64", "cdecl")
    _cmsAdjustEndianess64.argtypes = [POINTER(cmsUInt64Number), POINTER(cmsUInt64Number)]
    _cmsAdjustEndianess64.restype = None

# /usr/include/lcms2_plugin.h: 137
if _libs["lcms2"].has("_cmsReadUInt8Number", "cdecl"):
    _cmsReadUInt8Number = _libs["lcms2"].get("_cmsReadUInt8Number", "cdecl")
    _cmsReadUInt8Number.argtypes = [POINTER(cmsIOHANDLER), POINTER(cmsUInt8Number)]
    _cmsReadUInt8Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 138
if _libs["lcms2"].has("_cmsReadUInt16Number", "cdecl"):
    _cmsReadUInt16Number = _libs["lcms2"].get("_cmsReadUInt16Number", "cdecl")
    _cmsReadUInt16Number.argtypes = [POINTER(cmsIOHANDLER), POINTER(cmsUInt16Number)]
    _cmsReadUInt16Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 139
if _libs["lcms2"].has("_cmsReadUInt32Number", "cdecl"):
    _cmsReadUInt32Number = _libs["lcms2"].get("_cmsReadUInt32Number", "cdecl")
    _cmsReadUInt32Number.argtypes = [POINTER(cmsIOHANDLER), POINTER(cmsUInt32Number)]
    _cmsReadUInt32Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 140
if _libs["lcms2"].has("_cmsReadFloat32Number", "cdecl"):
    _cmsReadFloat32Number = _libs["lcms2"].get("_cmsReadFloat32Number", "cdecl")
    _cmsReadFloat32Number.argtypes = [POINTER(cmsIOHANDLER), POINTER(cmsFloat32Number)]
    _cmsReadFloat32Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 141
if _libs["lcms2"].has("_cmsReadUInt64Number", "cdecl"):
    _cmsReadUInt64Number = _libs["lcms2"].get("_cmsReadUInt64Number", "cdecl")
    _cmsReadUInt64Number.argtypes = [POINTER(cmsIOHANDLER), POINTER(cmsUInt64Number)]
    _cmsReadUInt64Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 142
if _libs["lcms2"].has("_cmsRead15Fixed16Number", "cdecl"):
    _cmsRead15Fixed16Number = _libs["lcms2"].get("_cmsRead15Fixed16Number", "cdecl")
    _cmsRead15Fixed16Number.argtypes = [POINTER(cmsIOHANDLER), POINTER(cmsFloat64Number)]
    _cmsRead15Fixed16Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 143
if _libs["lcms2"].has("_cmsReadXYZNumber", "cdecl"):
    _cmsReadXYZNumber = _libs["lcms2"].get("_cmsReadXYZNumber", "cdecl")
    _cmsReadXYZNumber.argtypes = [POINTER(cmsIOHANDLER), POINTER(cmsCIEXYZ)]
    _cmsReadXYZNumber.restype = cmsBool

# /usr/include/lcms2_plugin.h: 144
if _libs["lcms2"].has("_cmsReadUInt16Array", "cdecl"):
    _cmsReadUInt16Array = _libs["lcms2"].get("_cmsReadUInt16Array", "cdecl")
    _cmsReadUInt16Array.argtypes = [POINTER(cmsIOHANDLER), cmsUInt32Number, POINTER(cmsUInt16Number)]
    _cmsReadUInt16Array.restype = cmsBool

# /usr/include/lcms2_plugin.h: 146
if _libs["lcms2"].has("_cmsWriteUInt8Number", "cdecl"):
    _cmsWriteUInt8Number = _libs["lcms2"].get("_cmsWriteUInt8Number", "cdecl")
    _cmsWriteUInt8Number.argtypes = [POINTER(cmsIOHANDLER), cmsUInt8Number]
    _cmsWriteUInt8Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 147
if _libs["lcms2"].has("_cmsWriteUInt16Number", "cdecl"):
    _cmsWriteUInt16Number = _libs["lcms2"].get("_cmsWriteUInt16Number", "cdecl")
    _cmsWriteUInt16Number.argtypes = [POINTER(cmsIOHANDLER), cmsUInt16Number]
    _cmsWriteUInt16Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 148
if _libs["lcms2"].has("_cmsWriteUInt32Number", "cdecl"):
    _cmsWriteUInt32Number = _libs["lcms2"].get("_cmsWriteUInt32Number", "cdecl")
    _cmsWriteUInt32Number.argtypes = [POINTER(cmsIOHANDLER), cmsUInt32Number]
    _cmsWriteUInt32Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 149
if _libs["lcms2"].has("_cmsWriteFloat32Number", "cdecl"):
    _cmsWriteFloat32Number = _libs["lcms2"].get("_cmsWriteFloat32Number", "cdecl")
    _cmsWriteFloat32Number.argtypes = [POINTER(cmsIOHANDLER), cmsFloat32Number]
    _cmsWriteFloat32Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 150
if _libs["lcms2"].has("_cmsWriteUInt64Number", "cdecl"):
    _cmsWriteUInt64Number = _libs["lcms2"].get("_cmsWriteUInt64Number", "cdecl")
    _cmsWriteUInt64Number.argtypes = [POINTER(cmsIOHANDLER), POINTER(cmsUInt64Number)]
    _cmsWriteUInt64Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 151
if _libs["lcms2"].has("_cmsWrite15Fixed16Number", "cdecl"):
    _cmsWrite15Fixed16Number = _libs["lcms2"].get("_cmsWrite15Fixed16Number", "cdecl")
    _cmsWrite15Fixed16Number.argtypes = [POINTER(cmsIOHANDLER), cmsFloat64Number]
    _cmsWrite15Fixed16Number.restype = cmsBool

# /usr/include/lcms2_plugin.h: 152
if _libs["lcms2"].has("_cmsWriteXYZNumber", "cdecl"):
    _cmsWriteXYZNumber = _libs["lcms2"].get("_cmsWriteXYZNumber", "cdecl")
    _cmsWriteXYZNumber.argtypes = [POINTER(cmsIOHANDLER), POINTER(cmsCIEXYZ)]
    _cmsWriteXYZNumber.restype = cmsBool

# /usr/include/lcms2_plugin.h: 153
if _libs["lcms2"].has("_cmsWriteUInt16Array", "cdecl"):
    _cmsWriteUInt16Array = _libs["lcms2"].get("_cmsWriteUInt16Array", "cdecl")
    _cmsWriteUInt16Array.argtypes = [POINTER(cmsIOHANDLER), cmsUInt32Number, POINTER(cmsUInt16Number)]
    _cmsWriteUInt16Array.restype = cmsBool

# /usr/include/lcms2_plugin.h: 160
class struct_anon_60(Structure):
    pass

struct_anon_60.__slots__ = [
    'sig',
    'reserved',
]
struct_anon_60._fields_ = [
    ('sig', cmsTagTypeSignature),
    ('reserved', cmsInt8Number * int(4)),
]

_cmsTagBase = struct_anon_60# /usr/include/lcms2_plugin.h: 160

# /usr/include/lcms2_plugin.h: 163
if _libs["lcms2"].has("_cmsReadTypeBase", "cdecl"):
    _cmsReadTypeBase = _libs["lcms2"].get("_cmsReadTypeBase", "cdecl")
    _cmsReadTypeBase.argtypes = [POINTER(cmsIOHANDLER)]
    _cmsReadTypeBase.restype = cmsTagTypeSignature

# /usr/include/lcms2_plugin.h: 164
if _libs["lcms2"].has("_cmsWriteTypeBase", "cdecl"):
    _cmsWriteTypeBase = _libs["lcms2"].get("_cmsWriteTypeBase", "cdecl")
    _cmsWriteTypeBase.argtypes = [POINTER(cmsIOHANDLER), cmsTagTypeSignature]
    _cmsWriteTypeBase.restype = cmsBool

# /usr/include/lcms2_plugin.h: 167
if _libs["lcms2"].has("_cmsReadAlignment", "cdecl"):
    _cmsReadAlignment = _libs["lcms2"].get("_cmsReadAlignment", "cdecl")
    _cmsReadAlignment.argtypes = [POINTER(cmsIOHANDLER)]
    _cmsReadAlignment.restype = cmsBool

# /usr/include/lcms2_plugin.h: 168
if _libs["lcms2"].has("_cmsWriteAlignment", "cdecl"):
    _cmsWriteAlignment = _libs["lcms2"].get("_cmsWriteAlignment", "cdecl")
    _cmsWriteAlignment.argtypes = [POINTER(cmsIOHANDLER)]
    _cmsWriteAlignment.restype = cmsBool

# /usr/include/lcms2_plugin.h: 171
if _libs["lcms2"].has("_cmsIOPrintf", "cdecl"):
    _func = _libs["lcms2"].get("_cmsIOPrintf", "cdecl")
    _restype = cmsBool
    _errcheck = None
    _argtypes = [POINTER(cmsIOHANDLER), String]
    _cmsIOPrintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/lcms2_plugin.h: 174
if _libs["lcms2"].has("_cms8Fixed8toDouble", "cdecl"):
    _cms8Fixed8toDouble = _libs["lcms2"].get("_cms8Fixed8toDouble", "cdecl")
    _cms8Fixed8toDouble.argtypes = [cmsUInt16Number]
    _cms8Fixed8toDouble.restype = cmsFloat64Number

# /usr/include/lcms2_plugin.h: 175
if _libs["lcms2"].has("_cmsDoubleTo8Fixed8", "cdecl"):
    _cmsDoubleTo8Fixed8 = _libs["lcms2"].get("_cmsDoubleTo8Fixed8", "cdecl")
    _cmsDoubleTo8Fixed8.argtypes = [cmsFloat64Number]
    _cmsDoubleTo8Fixed8.restype = cmsUInt16Number

# /usr/include/lcms2_plugin.h: 177
if _libs["lcms2"].has("_cms15Fixed16toDouble", "cdecl"):
    _cms15Fixed16toDouble = _libs["lcms2"].get("_cms15Fixed16toDouble", "cdecl")
    _cms15Fixed16toDouble.argtypes = [cmsS15Fixed16Number]
    _cms15Fixed16toDouble.restype = cmsFloat64Number

# /usr/include/lcms2_plugin.h: 178
if _libs["lcms2"].has("_cmsDoubleTo15Fixed16", "cdecl"):
    _cmsDoubleTo15Fixed16 = _libs["lcms2"].get("_cmsDoubleTo15Fixed16", "cdecl")
    _cmsDoubleTo15Fixed16.argtypes = [cmsFloat64Number]
    _cmsDoubleTo15Fixed16.restype = cmsS15Fixed16Number

# /usr/include/lcms2_plugin.h: 181
if _libs["lcms2"].has("_cmsEncodeDateTimeNumber", "cdecl"):
    _cmsEncodeDateTimeNumber = _libs["lcms2"].get("_cmsEncodeDateTimeNumber", "cdecl")
    _cmsEncodeDateTimeNumber.argtypes = [POINTER(cmsDateTimeNumber), POINTER(struct_tm)]
    _cmsEncodeDateTimeNumber.restype = None

# /usr/include/lcms2_plugin.h: 182
if _libs["lcms2"].has("_cmsDecodeDateTimeNumber", "cdecl"):
    _cmsDecodeDateTimeNumber = _libs["lcms2"].get("_cmsDecodeDateTimeNumber", "cdecl")
    _cmsDecodeDateTimeNumber.argtypes = [POINTER(cmsDateTimeNumber), POINTER(struct_tm)]
    _cmsDecodeDateTimeNumber.restype = None

_cmsFreeUserDataFn = CFUNCTYPE(UNCHECKED(None), cmsContext, POINTER(None))# /usr/include/lcms2_plugin.h: 187

_cmsDupUserDataFn = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), cmsContext, POINTER(None))# /usr/include/lcms2_plugin.h: 188

# /usr/include/lcms2_plugin.h: 207
class struct__cmsPluginBaseStruct(Structure):
    pass

struct__cmsPluginBaseStruct.__slots__ = [
    'Magic',
    'ExpectedVersion',
    'Type',
    'Next',
]
struct__cmsPluginBaseStruct._fields_ = [
    ('Magic', cmsUInt32Number),
    ('ExpectedVersion', cmsUInt32Number),
    ('Type', cmsUInt32Number),
    ('Next', POINTER(struct__cmsPluginBaseStruct)),
]

cmsPluginBase = struct__cmsPluginBaseStruct# /usr/include/lcms2_plugin.h: 214

_cmsMallocFnPtrType = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), cmsContext, cmsUInt32Number)# /usr/include/lcms2_plugin.h: 223

_cmsFreeFnPtrType = CFUNCTYPE(UNCHECKED(None), cmsContext, POINTER(None))# /usr/include/lcms2_plugin.h: 224

_cmsReallocFnPtrType = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), cmsContext, POINTER(None), cmsUInt32Number)# /usr/include/lcms2_plugin.h: 225

_cmsMalloZerocFnPtrType = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), cmsContext, cmsUInt32Number)# /usr/include/lcms2_plugin.h: 227

_cmsCallocFnPtrType = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), cmsContext, cmsUInt32Number, cmsUInt32Number)# /usr/include/lcms2_plugin.h: 228

_cmsDupFnPtrType = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), cmsContext, POINTER(None), cmsUInt32Number)# /usr/include/lcms2_plugin.h: 229

# /usr/include/lcms2_plugin.h: 245
class struct_anon_61(Structure):
    pass

struct_anon_61.__slots__ = [
    'base',
    'MallocPtr',
    'FreePtr',
    'ReallocPtr',
    'MallocZeroPtr',
    'CallocPtr',
    'DupPtr',
]
struct_anon_61._fields_ = [
    ('base', cmsPluginBase),
    ('MallocPtr', _cmsMallocFnPtrType),
    ('FreePtr', _cmsFreeFnPtrType),
    ('ReallocPtr', _cmsReallocFnPtrType),
    ('MallocZeroPtr', _cmsMalloZerocFnPtrType),
    ('CallocPtr', _cmsCallocFnPtrType),
    ('DupPtr', _cmsDupFnPtrType),
]

cmsPluginMemHandler = struct_anon_61# /usr/include/lcms2_plugin.h: 245

# /usr/include/lcms2_plugin.h: 285
class struct__cms_interp_struc(Structure):
    pass

_cmsInterpFn16 = CFUNCTYPE(UNCHECKED(None), POINTER(cmsUInt16Number), POINTER(cmsUInt16Number), POINTER(struct__cms_interp_struc))# /usr/include/lcms2_plugin.h: 258

_cmsInterpFnFloat = CFUNCTYPE(UNCHECKED(None), POINTER(cmsFloat32Number), POINTER(cmsFloat32Number), POINTER(struct__cms_interp_struc))# /usr/include/lcms2_plugin.h: 265

# /usr/include/lcms2_plugin.h: 275
class union_anon_62(Union):
    pass

union_anon_62.__slots__ = [
    'Lerp16',
    'LerpFloat',
]
union_anon_62._fields_ = [
    ('Lerp16', _cmsInterpFn16),
    ('LerpFloat', _cmsInterpFnFloat),
]

cmsInterpFunction = union_anon_62# /usr/include/lcms2_plugin.h: 275

struct__cms_interp_struc.__slots__ = [
    'ContextID',
    'dwFlags',
    'nInputs',
    'nOutputs',
    'nSamples',
    'Domain',
    'opta',
    'Table',
    'Interpolation',
]
struct__cms_interp_struc._fields_ = [
    ('ContextID', cmsContext),
    ('dwFlags', cmsUInt32Number),
    ('nInputs', cmsUInt32Number),
    ('nOutputs', cmsUInt32Number),
    ('nSamples', cmsUInt32Number * int(8)),
    ('Domain', cmsUInt32Number * int(8)),
    ('opta', cmsUInt32Number * int(8)),
    ('Table', POINTER(None)),
    ('Interpolation', cmsInterpFunction),
]

cmsInterpParams = struct__cms_interp_struc# /usr/include/lcms2_plugin.h: 303

cmsInterpFnFactory = CFUNCTYPE(UNCHECKED(cmsInterpFunction), cmsUInt32Number, cmsUInt32Number, cmsUInt32Number)# /usr/include/lcms2_plugin.h: 306

# /usr/include/lcms2_plugin.h: 315
class struct_anon_63(Structure):
    pass

struct_anon_63.__slots__ = [
    'base',
    'InterpolatorsFactory',
]
struct_anon_63._fields_ = [
    ('base', cmsPluginBase),
    ('InterpolatorsFactory', cmsInterpFnFactory),
]

cmsPluginInterpolation = struct_anon_63# /usr/include/lcms2_plugin.h: 315

cmsParametricCurveEvaluator = CFUNCTYPE(UNCHECKED(cmsFloat64Number), cmsInt32Number, cmsFloat64Number * int(10), cmsFloat64Number)# /usr/include/lcms2_plugin.h: 322

# /usr/include/lcms2_plugin.h: 334
class struct_anon_64(Structure):
    pass

struct_anon_64.__slots__ = [
    'base',
    'nFunctions',
    'FunctionTypes',
    'ParameterCount',
    'Evaluator',
]
struct_anon_64._fields_ = [
    ('base', cmsPluginBase),
    ('nFunctions', cmsUInt32Number),
    ('FunctionTypes', cmsUInt32Number * int(20)),
    ('ParameterCount', cmsUInt32Number * int(20)),
    ('Evaluator', cmsParametricCurveEvaluator),
]

cmsPluginParametricCurves = struct_anon_64# /usr/include/lcms2_plugin.h: 334

# /usr/include/lcms2_plugin.h: 341
class struct__cmstransform_struct(Structure):
    pass

cmsFormatter16 = CFUNCTYPE(UNCHECKED(POINTER(cmsUInt8Number)), POINTER(struct__cmstransform_struct), POINTER(cmsUInt16Number), POINTER(cmsUInt8Number), cmsUInt32Number)# /usr/include/lcms2_plugin.h: 343

cmsFormatterFloat = CFUNCTYPE(UNCHECKED(POINTER(cmsUInt8Number)), POINTER(struct__cmstransform_struct), POINTER(cmsFloat32Number), POINTER(cmsUInt8Number), cmsUInt32Number)# /usr/include/lcms2_plugin.h: 348

# /usr/include/lcms2_plugin.h: 358
class union_anon_65(Union):
    pass

union_anon_65.__slots__ = [
    'Fmt16',
    'FmtFloat',
]
union_anon_65._fields_ = [
    ('Fmt16', cmsFormatter16),
    ('FmtFloat', cmsFormatterFloat),
]

cmsFormatter = union_anon_65# /usr/include/lcms2_plugin.h: 358

enum_anon_66 = c_int# /usr/include/lcms2_plugin.h: 363

cmsFormatterInput = 0# /usr/include/lcms2_plugin.h: 363

cmsFormatterOutput = 1# /usr/include/lcms2_plugin.h: 363

cmsFormatterDirection = enum_anon_66# /usr/include/lcms2_plugin.h: 363

cmsFormatterFactory = CFUNCTYPE(UNCHECKED(cmsFormatter), cmsUInt32Number, cmsFormatterDirection, cmsUInt32Number)# /usr/include/lcms2_plugin.h: 365

# /usr/include/lcms2_plugin.h: 374
class struct_anon_67(Structure):
    pass

struct_anon_67.__slots__ = [
    'base',
    'FormattersFactory',
]
struct_anon_67._fields_ = [
    ('base', cmsPluginBase),
    ('FormattersFactory', cmsFormatterFactory),
]

cmsPluginFormatters = struct_anon_67# /usr/include/lcms2_plugin.h: 374

# /usr/include/lcms2_plugin.h: 380
class struct__cms_typehandler_struct(Structure):
    pass

struct__cms_typehandler_struct.__slots__ = [
    'Signature',
    'ReadPtr',
    'WritePtr',
    'DupPtr',
    'FreePtr',
    'ContextID',
    'ICCVersion',
]
struct__cms_typehandler_struct._fields_ = [
    ('Signature', cmsTagTypeSignature),
    ('ReadPtr', CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(struct__cms_typehandler_struct), POINTER(cmsIOHANDLER), POINTER(cmsUInt32Number), cmsUInt32Number)),
    ('WritePtr', CFUNCTYPE(UNCHECKED(cmsBool), POINTER(struct__cms_typehandler_struct), POINTER(cmsIOHANDLER), POINTER(None), cmsUInt32Number)),
    ('DupPtr', CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(struct__cms_typehandler_struct), POINTER(None), cmsUInt32Number)),
    ('FreePtr', CFUNCTYPE(UNCHECKED(None), POINTER(struct__cms_typehandler_struct), POINTER(None))),
    ('ContextID', cmsContext),
    ('ICCVersion', cmsUInt32Number),
]

cmsTagTypeHandler = struct__cms_typehandler_struct# /usr/include/lcms2_plugin.h: 409

# /usr/include/lcms2_plugin.h: 416
class struct_anon_68(Structure):
    pass

struct_anon_68.__slots__ = [
    'base',
    'Handler',
]
struct_anon_68._fields_ = [
    ('base', cmsPluginBase),
    ('Handler', cmsTagTypeHandler),
]

cmsPluginTagType = struct_anon_68# /usr/include/lcms2_plugin.h: 416

# /usr/include/lcms2_plugin.h: 434
class struct_anon_69(Structure):
    pass

struct_anon_69.__slots__ = [
    'ElemCount',
    'nSupportedTypes',
    'SupportedTypes',
    'DecideType',
]
struct_anon_69._fields_ = [
    ('ElemCount', cmsUInt32Number),
    ('nSupportedTypes', cmsUInt32Number),
    ('SupportedTypes', cmsTagTypeSignature * int(20)),
    ('DecideType', CFUNCTYPE(UNCHECKED(cmsTagTypeSignature), cmsFloat64Number, POINTER(None))),
]

cmsTagDescriptor = struct_anon_69# /usr/include/lcms2_plugin.h: 434

# /usr/include/lcms2_plugin.h: 443
class struct_anon_70(Structure):
    pass

struct_anon_70.__slots__ = [
    'base',
    'Signature',
    'Descriptor',
]
struct_anon_70._fields_ = [
    ('base', cmsPluginBase),
    ('Signature', cmsTagSignature),
    ('Descriptor', cmsTagDescriptor),
]

cmsPluginTag = struct_anon_70# /usr/include/lcms2_plugin.h: 443

cmsIntentFn = CFUNCTYPE(UNCHECKED(POINTER(cmsPipeline)), cmsContext, cmsUInt32Number, POINTER(cmsUInt32Number), POINTER(cmsHPROFILE), POINTER(cmsBool), POINTER(cmsFloat64Number), cmsUInt32Number)# /usr/include/lcms2_plugin.h: 452

# /usr/include/lcms2_plugin.h: 468
class struct_anon_71(Structure):
    pass

struct_anon_71.__slots__ = [
    'base',
    'Intent',
    'Link',
    'Description',
]
struct_anon_71._fields_ = [
    ('base', cmsPluginBase),
    ('Intent', cmsUInt32Number),
    ('Link', cmsIntentFn),
    ('Description', c_char * int(256)),
]

cmsPluginRenderingIntent = struct_anon_71# /usr/include/lcms2_plugin.h: 468

# /usr/include/lcms2_plugin.h: 472
if _libs["lcms2"].has("_cmsDefaultICCintents", "cdecl"):
    _cmsDefaultICCintents = _libs["lcms2"].get("_cmsDefaultICCintents", "cdecl")
    _cmsDefaultICCintents.argtypes = [cmsContext, cmsUInt32Number, POINTER(cmsUInt32Number), POINTER(cmsHPROFILE), POINTER(cmsBool), POINTER(cmsFloat64Number), cmsUInt32Number]
    _cmsDefaultICCintents.restype = POINTER(cmsPipeline)

_cmsStageEvalFn = CFUNCTYPE(UNCHECKED(None), POINTER(cmsFloat32Number), POINTER(cmsFloat32Number), POINTER(cmsStage))# /usr/include/lcms2_plugin.h: 485

_cmsStageDupElemFn = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(cmsStage))# /usr/include/lcms2_plugin.h: 486

_cmsStageFreeElemFn = CFUNCTYPE(UNCHECKED(None), POINTER(cmsStage))# /usr/include/lcms2_plugin.h: 487

# /usr/include/lcms2_plugin.h: 491
if _libs["lcms2"].has("_cmsStageAllocPlaceholder", "cdecl"):
    _cmsStageAllocPlaceholder = _libs["lcms2"].get("_cmsStageAllocPlaceholder", "cdecl")
    _cmsStageAllocPlaceholder.argtypes = [cmsContext, cmsStageSignature, cmsUInt32Number, cmsUInt32Number, _cmsStageEvalFn, _cmsStageDupElemFn, _cmsStageFreeElemFn, POINTER(None)]
    _cmsStageAllocPlaceholder.restype = POINTER(cmsStage)

# /usr/include/lcms2_plugin.h: 503
class struct_anon_72(Structure):
    pass

struct_anon_72.__slots__ = [
    'base',
    'Handler',
]
struct_anon_72._fields_ = [
    ('base', cmsPluginBase),
    ('Handler', cmsTagTypeHandler),
]

cmsPluginMultiProcessElement = struct_anon_72# /usr/include/lcms2_plugin.h: 503

# /usr/include/lcms2_plugin.h: 513
class struct_anon_73(Structure):
    pass

struct_anon_73.__slots__ = [
    'nCurves',
    'TheCurves',
]
struct_anon_73._fields_ = [
    ('nCurves', cmsUInt32Number),
    ('TheCurves', POINTER(POINTER(cmsToneCurve))),
]

_cmsStageToneCurvesData = struct_anon_73# /usr/include/lcms2_plugin.h: 513

# /usr/include/lcms2_plugin.h: 520
class struct_anon_74(Structure):
    pass

struct_anon_74.__slots__ = [
    'Double',
    'Offset',
]
struct_anon_74._fields_ = [
    ('Double', POINTER(cmsFloat64Number)),
    ('Offset', POINTER(cmsFloat64Number)),
]

_cmsStageMatrixData = struct_anon_74# /usr/include/lcms2_plugin.h: 520

# /usr/include/lcms2_plugin.h: 525
class union_anon_75(Union):
    pass

union_anon_75.__slots__ = [
    'T',
    'TFloat',
]
union_anon_75._fields_ = [
    ('T', POINTER(cmsUInt16Number)),
    ('TFloat', POINTER(cmsFloat32Number)),
]

# /usr/include/lcms2_plugin.h: 535
class struct_anon_76(Structure):
    pass

struct_anon_76.__slots__ = [
    'Tab',
    'Params',
    'nEntries',
    'HasFloatValues',
]
struct_anon_76._fields_ = [
    ('Tab', union_anon_75),
    ('Params', POINTER(cmsInterpParams)),
    ('nEntries', cmsUInt32Number),
    ('HasFloatValues', cmsBool),
]

_cmsStageCLutData = struct_anon_76# /usr/include/lcms2_plugin.h: 535

_cmsOPTeval16Fn = CFUNCTYPE(UNCHECKED(None), POINTER(cmsUInt16Number), POINTER(cmsUInt16Number), POINTER(None))# /usr/include/lcms2_plugin.h: 544

_cmsOPToptimizeFn = CFUNCTYPE(UNCHECKED(cmsBool), POINTER(POINTER(cmsPipeline)), cmsUInt32Number, POINTER(cmsUInt32Number), POINTER(cmsUInt32Number), POINTER(cmsUInt32Number))# /usr/include/lcms2_plugin.h: 549

# /usr/include/lcms2_plugin.h: 558
if _libs["lcms2"].has("_cmsPipelineSetOptimizationParameters", "cdecl"):
    _cmsPipelineSetOptimizationParameters = _libs["lcms2"].get("_cmsPipelineSetOptimizationParameters", "cdecl")
    _cmsPipelineSetOptimizationParameters.argtypes = [POINTER(cmsPipeline), _cmsOPTeval16Fn, POINTER(None), _cmsFreeUserDataFn, _cmsDupUserDataFn]
    _cmsPipelineSetOptimizationParameters.restype = None

# /usr/include/lcms2_plugin.h: 570
class struct_anon_77(Structure):
    pass

struct_anon_77.__slots__ = [
    'base',
    'OptimizePtr',
]
struct_anon_77._fields_ = [
    ('base', cmsPluginBase),
    ('OptimizePtr', _cmsOPToptimizeFn),
]

cmsPluginOptimization = struct_anon_77# /usr/include/lcms2_plugin.h: 570

# /usr/include/lcms2_plugin.h: 581
class struct_anon_78(Structure):
    pass

struct_anon_78.__slots__ = [
    'BytesPerLineIn',
    'BytesPerLineOut',
    'BytesPerPlaneIn',
    'BytesPerPlaneOut',
]
struct_anon_78._fields_ = [
    ('BytesPerLineIn', cmsUInt32Number),
    ('BytesPerLineOut', cmsUInt32Number),
    ('BytesPerPlaneIn', cmsUInt32Number),
    ('BytesPerPlaneOut', cmsUInt32Number),
]

cmsStride = struct_anon_78# /usr/include/lcms2_plugin.h: 581

_cmsTransformFn = CFUNCTYPE(UNCHECKED(None), POINTER(struct__cmstransform_struct), POINTER(None), POINTER(None), cmsUInt32Number, cmsUInt32Number)# /usr/include/lcms2_plugin.h: 583

_cmsTransform2Fn = CFUNCTYPE(UNCHECKED(None), POINTER(struct__cmstransform_struct), POINTER(None), POINTER(None), cmsUInt32Number, cmsUInt32Number, POINTER(cmsStride))# /usr/include/lcms2_plugin.h: 590

_cmsTransformFactory = CFUNCTYPE(UNCHECKED(cmsBool), POINTER(_cmsTransformFn), POINTER(POINTER(None)), POINTER(_cmsFreeUserDataFn), POINTER(POINTER(cmsPipeline)), POINTER(cmsUInt32Number), POINTER(cmsUInt32Number), POINTER(cmsUInt32Number))# /usr/include/lcms2_plugin.h: 597

_cmsTransform2Factory = CFUNCTYPE(UNCHECKED(cmsBool), POINTER(_cmsTransform2Fn), POINTER(POINTER(None)), POINTER(_cmsFreeUserDataFn), POINTER(POINTER(cmsPipeline)), POINTER(cmsUInt32Number), POINTER(cmsUInt32Number), POINTER(cmsUInt32Number))# /usr/include/lcms2_plugin.h: 605

# /usr/include/lcms2_plugin.h: 615
if _libs["lcms2"].has("_cmsSetTransformUserData", "cdecl"):
    _cmsSetTransformUserData = _libs["lcms2"].get("_cmsSetTransformUserData", "cdecl")
    _cmsSetTransformUserData.argtypes = [POINTER(struct__cmstransform_struct), POINTER(None), _cmsFreeUserDataFn]
    _cmsSetTransformUserData.restype = None

# /usr/include/lcms2_plugin.h: 616
if _libs["lcms2"].has("_cmsGetTransformUserData", "cdecl"):
    _cmsGetTransformUserData = _libs["lcms2"].get("_cmsGetTransformUserData", "cdecl")
    _cmsGetTransformUserData.argtypes = [POINTER(struct__cmstransform_struct)]
    _cmsGetTransformUserData.restype = POINTER(c_ubyte)
    _cmsGetTransformUserData.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/lcms2_plugin.h: 620
if _libs["lcms2"].has("_cmsGetTransformFormatters16", "cdecl"):
    _cmsGetTransformFormatters16 = _libs["lcms2"].get("_cmsGetTransformFormatters16", "cdecl")
    _cmsGetTransformFormatters16.argtypes = [POINTER(struct__cmstransform_struct), POINTER(cmsFormatter16), POINTER(cmsFormatter16)]
    _cmsGetTransformFormatters16.restype = None

# /usr/include/lcms2_plugin.h: 621
if _libs["lcms2"].has("_cmsGetTransformFormattersFloat", "cdecl"):
    _cmsGetTransformFormattersFloat = _libs["lcms2"].get("_cmsGetTransformFormattersFloat", "cdecl")
    _cmsGetTransformFormattersFloat.argtypes = [POINTER(struct__cmstransform_struct), POINTER(cmsFormatterFloat), POINTER(cmsFormatterFloat)]
    _cmsGetTransformFormattersFloat.restype = None

# /usr/include/lcms2_plugin.h: 627
class union_anon_79(Union):
    pass

union_anon_79.__slots__ = [
    'legacy_xform',
    'xform',
]
union_anon_79._fields_ = [
    ('legacy_xform', _cmsTransformFactory),
    ('xform', _cmsTransform2Factory),
]

# /usr/include/lcms2_plugin.h: 632
class struct_anon_80(Structure):
    pass

struct_anon_80.__slots__ = [
    'base',
    'factories',
]
struct_anon_80._fields_ = [
    ('base', cmsPluginBase),
    ('factories', union_anon_79),
]

cmsPluginTransform = struct_anon_80# /usr/include/lcms2_plugin.h: 632

_cmsCreateMutexFnPtrType = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), cmsContext)# /usr/include/lcms2_plugin.h: 637

_cmsDestroyMutexFnPtrType = CFUNCTYPE(UNCHECKED(None), cmsContext, POINTER(None))# /usr/include/lcms2_plugin.h: 638

_cmsLockMutexFnPtrType = CFUNCTYPE(UNCHECKED(cmsBool), cmsContext, POINTER(None))# /usr/include/lcms2_plugin.h: 639

_cmsUnlockMutexFnPtrType = CFUNCTYPE(UNCHECKED(None), cmsContext, POINTER(None))# /usr/include/lcms2_plugin.h: 640

# /usr/include/lcms2_plugin.h: 650
class struct_anon_81(Structure):
    pass

struct_anon_81.__slots__ = [
    'base',
    'CreateMutexPtr',
    'DestroyMutexPtr',
    'LockMutexPtr',
    'UnlockMutexPtr',
]
struct_anon_81._fields_ = [
    ('base', cmsPluginBase),
    ('CreateMutexPtr', _cmsCreateMutexFnPtrType),
    ('DestroyMutexPtr', _cmsDestroyMutexFnPtrType),
    ('LockMutexPtr', _cmsLockMutexFnPtrType),
    ('UnlockMutexPtr', _cmsUnlockMutexFnPtrType),
]

cmsPluginMutex = struct_anon_81# /usr/include/lcms2_plugin.h: 650

# /usr/include/lcms2_plugin.h: 652
if _libs["lcms2"].has("_cmsCreateMutex", "cdecl"):
    _cmsCreateMutex = _libs["lcms2"].get("_cmsCreateMutex", "cdecl")
    _cmsCreateMutex.argtypes = [cmsContext]
    _cmsCreateMutex.restype = POINTER(c_ubyte)
    _cmsCreateMutex.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/lcms2_plugin.h: 653
if _libs["lcms2"].has("_cmsDestroyMutex", "cdecl"):
    _cmsDestroyMutex = _libs["lcms2"].get("_cmsDestroyMutex", "cdecl")
    _cmsDestroyMutex.argtypes = [cmsContext, POINTER(None)]
    _cmsDestroyMutex.restype = None

# /usr/include/lcms2_plugin.h: 654
if _libs["lcms2"].has("_cmsLockMutex", "cdecl"):
    _cmsLockMutex = _libs["lcms2"].get("_cmsLockMutex", "cdecl")
    _cmsLockMutex.argtypes = [cmsContext, POINTER(None)]
    _cmsLockMutex.restype = cmsBool

# /usr/include/lcms2_plugin.h: 655
if _libs["lcms2"].has("_cmsUnlockMutex", "cdecl"):
    _cmsUnlockMutex = _libs["lcms2"].get("_cmsUnlockMutex", "cdecl")
    _cmsUnlockMutex.argtypes = [cmsContext, POINTER(None)]
    _cmsUnlockMutex.restype = None

# /usr/include/lcms2.h: 81
try:
    LCMS_VERSION = 2090
except:
    pass

# /usr/include/lcms2.h: 256
try:
    cmsMAX_PATH = 256
except:
    pass

# /usr/include/lcms2.h: 259
try:
    FALSE = 0
except:
    pass

# /usr/include/lcms2.h: 262
try:
    TRUE = 1
except:
    pass

# /usr/include/lcms2.h: 266
try:
    cmsD50X = 0.9642
except:
    pass

# /usr/include/lcms2.h: 267
try:
    cmsD50Y = 1.0
except:
    pass

# /usr/include/lcms2.h: 268
try:
    cmsD50Z = 0.8249
except:
    pass

# /usr/include/lcms2.h: 271
try:
    cmsPERCEPTUAL_BLACK_X = 0.00336
except:
    pass

# /usr/include/lcms2.h: 272
try:
    cmsPERCEPTUAL_BLACK_Y = 0.0034731
except:
    pass

# /usr/include/lcms2.h: 273
try:
    cmsPERCEPTUAL_BLACK_Z = 0.00287
except:
    pass

# /usr/include/lcms2.h: 276
try:
    cmsMagicNumber = 1633907568
except:
    pass

# /usr/include/lcms2.h: 277
try:
    lcmsSignature = 1818455411
except:
    pass

# /usr/include/lcms2.h: 503
try:
    cmsSigPerceptualReferenceMediumGamut = 1886547303
except:
    pass

# /usr/include/lcms2.h: 506
try:
    cmsSigSceneColorimetryEstimates = 1935896421
except:
    pass

# /usr/include/lcms2.h: 507
try:
    cmsSigSceneAppearanceEstimates = 1935765605
except:
    pass

# /usr/include/lcms2.h: 508
try:
    cmsSigFocalPlaneColorimetryEstimates = 1718641509
except:
    pass

# /usr/include/lcms2.h: 509
try:
    cmsSigReflectionHardcopyOriginalColorimetry = 1919446883
except:
    pass

# /usr/include/lcms2.h: 510
try:
    cmsSigReflectionPrintOutputColorimetry = 1919971171
except:
    pass

# /usr/include/lcms2.h: 550
try:
    cmsSigStatusA = 1400136001
except:
    pass

# /usr/include/lcms2.h: 551
try:
    cmsSigStatusE = 1400136005
except:
    pass

# /usr/include/lcms2.h: 552
try:
    cmsSigStatusI = 1400136009
except:
    pass

# /usr/include/lcms2.h: 553
try:
    cmsSigStatusT = 1400136020
except:
    pass

# /usr/include/lcms2.h: 554
try:
    cmsSigStatusM = 1400136013
except:
    pass

# /usr/include/lcms2.h: 555
try:
    cmsSigDN = 1145970720
except:
    pass

# /usr/include/lcms2.h: 556
try:
    cmsSigDNP = 1145970768
except:
    pass

# /usr/include/lcms2.h: 557
try:
    cmsSigDNN = 1145982496
except:
    pass

# /usr/include/lcms2.h: 558
try:
    cmsSigDNNP = 1145982544
except:
    pass

# /usr/include/lcms2.h: 562
try:
    cmsReflective = 0
except:
    pass

# /usr/include/lcms2.h: 563
try:
    cmsTransparency = 1
except:
    pass

# /usr/include/lcms2.h: 564
try:
    cmsGlossy = 0
except:
    pass

# /usr/include/lcms2.h: 565
try:
    cmsMatte = 2
except:
    pass

# /usr/include/lcms2.h: 654
try:
    cmsMAXCHANNELS = 16
except:
    pass

# /usr/include/lcms2.h: 674
def FLOAT_SH(a):
    return (a << 22)

# /usr/include/lcms2.h: 675
def OPTIMIZED_SH(s):
    return (s << 21)

# /usr/include/lcms2.h: 676
def COLORSPACE_SH(s):
    return (s << 16)

# /usr/include/lcms2.h: 677
def SWAPFIRST_SH(s):
    return (s << 14)

# /usr/include/lcms2.h: 678
def FLAVOR_SH(s):
    return (s << 13)

# /usr/include/lcms2.h: 679
def PLANAR_SH(p):
    return (p << 12)

# /usr/include/lcms2.h: 680
def ENDIAN16_SH(e):
    return (e << 11)

# /usr/include/lcms2.h: 681
def DOSWAP_SH(e):
    return (e << 10)

# /usr/include/lcms2.h: 682
def EXTRA_SH(e):
    return (e << 7)

# /usr/include/lcms2.h: 683
def CHANNELS_SH(c):
    return (c << 3)

# /usr/include/lcms2.h: 684
def BYTES_SH(b):
    return b

# /usr/include/lcms2.h: 687
def T_FLOAT(a):
    return ((a >> 22) & 1)

# /usr/include/lcms2.h: 688
def T_OPTIMIZED(o):
    return ((o >> 21) & 1)

# /usr/include/lcms2.h: 689
def T_COLORSPACE(s):
    return ((s >> 16) & 31)

# /usr/include/lcms2.h: 690
def T_SWAPFIRST(s):
    return ((s >> 14) & 1)

# /usr/include/lcms2.h: 691
def T_FLAVOR(s):
    return ((s >> 13) & 1)

# /usr/include/lcms2.h: 692
def T_PLANAR(p):
    return ((p >> 12) & 1)

# /usr/include/lcms2.h: 693
def T_ENDIAN16(e):
    return ((e >> 11) & 1)

# /usr/include/lcms2.h: 694
def T_DOSWAP(e):
    return ((e >> 10) & 1)

# /usr/include/lcms2.h: 695
def T_EXTRA(e):
    return ((e >> 7) & 7)

# /usr/include/lcms2.h: 696
def T_CHANNELS(c):
    return ((c >> 3) & 15)

# /usr/include/lcms2.h: 697
def T_BYTES(b):
    return (b & 7)

# /usr/include/lcms2.h: 701
try:
    PT_ANY = 0
except:
    pass

# /usr/include/lcms2.h: 703
try:
    PT_GRAY = 3
except:
    pass

# /usr/include/lcms2.h: 704
try:
    PT_RGB = 4
except:
    pass

# /usr/include/lcms2.h: 705
try:
    PT_CMY = 5
except:
    pass

# /usr/include/lcms2.h: 706
try:
    PT_CMYK = 6
except:
    pass

# /usr/include/lcms2.h: 707
try:
    PT_YCbCr = 7
except:
    pass

# /usr/include/lcms2.h: 708
try:
    PT_YUV = 8
except:
    pass

# /usr/include/lcms2.h: 709
try:
    PT_XYZ = 9
except:
    pass

# /usr/include/lcms2.h: 710
try:
    PT_Lab = 10
except:
    pass

# /usr/include/lcms2.h: 711
try:
    PT_YUVK = 11
except:
    pass

# /usr/include/lcms2.h: 712
try:
    PT_HSV = 12
except:
    pass

# /usr/include/lcms2.h: 713
try:
    PT_HLS = 13
except:
    pass

# /usr/include/lcms2.h: 714
try:
    PT_Yxy = 14
except:
    pass

# /usr/include/lcms2.h: 716
try:
    PT_MCH1 = 15
except:
    pass

# /usr/include/lcms2.h: 717
try:
    PT_MCH2 = 16
except:
    pass

# /usr/include/lcms2.h: 718
try:
    PT_MCH3 = 17
except:
    pass

# /usr/include/lcms2.h: 719
try:
    PT_MCH4 = 18
except:
    pass

# /usr/include/lcms2.h: 720
try:
    PT_MCH5 = 19
except:
    pass

# /usr/include/lcms2.h: 721
try:
    PT_MCH6 = 20
except:
    pass

# /usr/include/lcms2.h: 722
try:
    PT_MCH7 = 21
except:
    pass

# /usr/include/lcms2.h: 723
try:
    PT_MCH8 = 22
except:
    pass

# /usr/include/lcms2.h: 724
try:
    PT_MCH9 = 23
except:
    pass

# /usr/include/lcms2.h: 725
try:
    PT_MCH10 = 24
except:
    pass

# /usr/include/lcms2.h: 726
try:
    PT_MCH11 = 25
except:
    pass

# /usr/include/lcms2.h: 727
try:
    PT_MCH12 = 26
except:
    pass

# /usr/include/lcms2.h: 728
try:
    PT_MCH13 = 27
except:
    pass

# /usr/include/lcms2.h: 729
try:
    PT_MCH14 = 28
except:
    pass

# /usr/include/lcms2.h: 730
try:
    PT_MCH15 = 29
except:
    pass

# /usr/include/lcms2.h: 732
try:
    PT_LabV2 = 30
except:
    pass

# /usr/include/lcms2.h: 739
try:
    TYPE_GRAY_8 = (((COLORSPACE_SH (PT_GRAY)) | (CHANNELS_SH (1))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 740
try:
    TYPE_GRAY_8_REV = ((((COLORSPACE_SH (PT_GRAY)) | (CHANNELS_SH (1))) | (BYTES_SH (1))) | (FLAVOR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 741
try:
    TYPE_GRAY_16 = (((COLORSPACE_SH (PT_GRAY)) | (CHANNELS_SH (1))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 742
try:
    TYPE_GRAY_16_REV = ((((COLORSPACE_SH (PT_GRAY)) | (CHANNELS_SH (1))) | (BYTES_SH (2))) | (FLAVOR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 743
try:
    TYPE_GRAY_16_SE = ((((COLORSPACE_SH (PT_GRAY)) | (CHANNELS_SH (1))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 744
try:
    TYPE_GRAYA_8 = ((((COLORSPACE_SH (PT_GRAY)) | (EXTRA_SH (1))) | (CHANNELS_SH (1))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 745
try:
    TYPE_GRAYA_16 = ((((COLORSPACE_SH (PT_GRAY)) | (EXTRA_SH (1))) | (CHANNELS_SH (1))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 746
try:
    TYPE_GRAYA_16_SE = (((((COLORSPACE_SH (PT_GRAY)) | (EXTRA_SH (1))) | (CHANNELS_SH (1))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 747
try:
    TYPE_GRAYA_8_PLANAR = (((((COLORSPACE_SH (PT_GRAY)) | (EXTRA_SH (1))) | (CHANNELS_SH (1))) | (BYTES_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 748
try:
    TYPE_GRAYA_16_PLANAR = (((((COLORSPACE_SH (PT_GRAY)) | (EXTRA_SH (1))) | (CHANNELS_SH (1))) | (BYTES_SH (2))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 750
try:
    TYPE_RGB_8 = (((COLORSPACE_SH (PT_RGB)) | (CHANNELS_SH (3))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 751
try:
    TYPE_RGB_8_PLANAR = ((((COLORSPACE_SH (PT_RGB)) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 752
try:
    TYPE_BGR_8 = ((((COLORSPACE_SH (PT_RGB)) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 753
try:
    TYPE_BGR_8_PLANAR = (((((COLORSPACE_SH (PT_RGB)) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (DOSWAP_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 754
try:
    TYPE_RGB_16 = (((COLORSPACE_SH (PT_RGB)) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 755
try:
    TYPE_RGB_16_PLANAR = ((((COLORSPACE_SH (PT_RGB)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 756
try:
    TYPE_RGB_16_SE = ((((COLORSPACE_SH (PT_RGB)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 757
try:
    TYPE_BGR_16 = ((((COLORSPACE_SH (PT_RGB)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 758
try:
    TYPE_BGR_16_PLANAR = (((((COLORSPACE_SH (PT_RGB)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 759
try:
    TYPE_BGR_16_SE = (((((COLORSPACE_SH (PT_RGB)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 761
try:
    TYPE_RGBA_8 = ((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 762
try:
    TYPE_RGBA_8_PLANAR = (((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 763
try:
    TYPE_RGBA_16 = ((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 764
try:
    TYPE_RGBA_16_PLANAR = (((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 765
try:
    TYPE_RGBA_16_SE = (((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 767
try:
    TYPE_ARGB_8 = (((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 768
try:
    TYPE_ARGB_8_PLANAR = ((((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (SWAPFIRST_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 769
try:
    TYPE_ARGB_16 = (((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 771
try:
    TYPE_ABGR_8 = (((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 772
try:
    TYPE_ABGR_8_PLANAR = ((((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (DOSWAP_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 773
try:
    TYPE_ABGR_16 = (((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 774
try:
    TYPE_ABGR_16_PLANAR = ((((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 775
try:
    TYPE_ABGR_16_SE = ((((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 777
try:
    TYPE_BGRA_8 = ((((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (DOSWAP_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 778
try:
    TYPE_BGRA_8_PLANAR = (((((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (DOSWAP_SH (1))) | (SWAPFIRST_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 779
try:
    TYPE_BGRA_16 = ((((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 780
try:
    TYPE_BGRA_16_SE = (((((((COLORSPACE_SH (PT_RGB)) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (ENDIAN16_SH (1))) | (DOSWAP_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 782
try:
    TYPE_CMY_8 = (((COLORSPACE_SH (PT_CMY)) | (CHANNELS_SH (3))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 783
try:
    TYPE_CMY_8_PLANAR = ((((COLORSPACE_SH (PT_CMY)) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 784
try:
    TYPE_CMY_16 = (((COLORSPACE_SH (PT_CMY)) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 785
try:
    TYPE_CMY_16_PLANAR = ((((COLORSPACE_SH (PT_CMY)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 786
try:
    TYPE_CMY_16_SE = ((((COLORSPACE_SH (PT_CMY)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 788
try:
    TYPE_CMYK_8 = (((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 789
try:
    TYPE_CMYKA_8 = ((((COLORSPACE_SH (PT_CMYK)) | (EXTRA_SH (1))) | (CHANNELS_SH (4))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 790
try:
    TYPE_CMYK_8_REV = ((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (1))) | (FLAVOR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 791
try:
    TYPE_YUVK_8 = TYPE_CMYK_8_REV
except:
    pass

# /usr/include/lcms2.h: 792
try:
    TYPE_CMYK_8_PLANAR = ((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 793
try:
    TYPE_CMYK_16 = (((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 794
try:
    TYPE_CMYK_16_REV = ((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (2))) | (FLAVOR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 795
try:
    TYPE_YUVK_16 = TYPE_CMYK_16_REV
except:
    pass

# /usr/include/lcms2.h: 796
try:
    TYPE_CMYK_16_PLANAR = ((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (2))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 797
try:
    TYPE_CMYK_16_SE = ((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 799
try:
    TYPE_KYMC_8 = ((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (1))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 800
try:
    TYPE_KYMC_16 = ((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 801
try:
    TYPE_KYMC_16_SE = (((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 803
try:
    TYPE_KCMY_8 = ((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 804
try:
    TYPE_KCMY_8_REV = (((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (1))) | (FLAVOR_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 805
try:
    TYPE_KCMY_16 = ((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (2))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 806
try:
    TYPE_KCMY_16_REV = (((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (2))) | (FLAVOR_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 807
try:
    TYPE_KCMY_16_SE = (((((COLORSPACE_SH (PT_CMYK)) | (CHANNELS_SH (4))) | (BYTES_SH (2))) | (ENDIAN16_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 809
try:
    TYPE_CMYK5_8 = (((COLORSPACE_SH (PT_MCH5)) | (CHANNELS_SH (5))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 810
try:
    TYPE_CMYK5_16 = (((COLORSPACE_SH (PT_MCH5)) | (CHANNELS_SH (5))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 811
try:
    TYPE_CMYK5_16_SE = ((((COLORSPACE_SH (PT_MCH5)) | (CHANNELS_SH (5))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 812
try:
    TYPE_KYMC5_8 = ((((COLORSPACE_SH (PT_MCH5)) | (CHANNELS_SH (5))) | (BYTES_SH (1))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 813
try:
    TYPE_KYMC5_16 = ((((COLORSPACE_SH (PT_MCH5)) | (CHANNELS_SH (5))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 814
try:
    TYPE_KYMC5_16_SE = (((((COLORSPACE_SH (PT_MCH5)) | (CHANNELS_SH (5))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 815
try:
    TYPE_CMYK6_8 = (((COLORSPACE_SH (PT_MCH6)) | (CHANNELS_SH (6))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 816
try:
    TYPE_CMYK6_8_PLANAR = ((((COLORSPACE_SH (PT_MCH6)) | (CHANNELS_SH (6))) | (BYTES_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 817
try:
    TYPE_CMYK6_16 = (((COLORSPACE_SH (PT_MCH6)) | (CHANNELS_SH (6))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 818
try:
    TYPE_CMYK6_16_PLANAR = ((((COLORSPACE_SH (PT_MCH6)) | (CHANNELS_SH (6))) | (BYTES_SH (2))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 819
try:
    TYPE_CMYK6_16_SE = ((((COLORSPACE_SH (PT_MCH6)) | (CHANNELS_SH (6))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 820
try:
    TYPE_CMYK7_8 = (((COLORSPACE_SH (PT_MCH7)) | (CHANNELS_SH (7))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 821
try:
    TYPE_CMYK7_16 = (((COLORSPACE_SH (PT_MCH7)) | (CHANNELS_SH (7))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 822
try:
    TYPE_CMYK7_16_SE = ((((COLORSPACE_SH (PT_MCH7)) | (CHANNELS_SH (7))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 823
try:
    TYPE_KYMC7_8 = ((((COLORSPACE_SH (PT_MCH7)) | (CHANNELS_SH (7))) | (BYTES_SH (1))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 824
try:
    TYPE_KYMC7_16 = ((((COLORSPACE_SH (PT_MCH7)) | (CHANNELS_SH (7))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 825
try:
    TYPE_KYMC7_16_SE = (((((COLORSPACE_SH (PT_MCH7)) | (CHANNELS_SH (7))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 826
try:
    TYPE_CMYK8_8 = (((COLORSPACE_SH (PT_MCH8)) | (CHANNELS_SH (8))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 827
try:
    TYPE_CMYK8_16 = (((COLORSPACE_SH (PT_MCH8)) | (CHANNELS_SH (8))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 828
try:
    TYPE_CMYK8_16_SE = ((((COLORSPACE_SH (PT_MCH8)) | (CHANNELS_SH (8))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 829
try:
    TYPE_KYMC8_8 = ((((COLORSPACE_SH (PT_MCH8)) | (CHANNELS_SH (8))) | (BYTES_SH (1))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 830
try:
    TYPE_KYMC8_16 = ((((COLORSPACE_SH (PT_MCH8)) | (CHANNELS_SH (8))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 831
try:
    TYPE_KYMC8_16_SE = (((((COLORSPACE_SH (PT_MCH8)) | (CHANNELS_SH (8))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 832
try:
    TYPE_CMYK9_8 = (((COLORSPACE_SH (PT_MCH9)) | (CHANNELS_SH (9))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 833
try:
    TYPE_CMYK9_16 = (((COLORSPACE_SH (PT_MCH9)) | (CHANNELS_SH (9))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 834
try:
    TYPE_CMYK9_16_SE = ((((COLORSPACE_SH (PT_MCH9)) | (CHANNELS_SH (9))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 835
try:
    TYPE_KYMC9_8 = ((((COLORSPACE_SH (PT_MCH9)) | (CHANNELS_SH (9))) | (BYTES_SH (1))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 836
try:
    TYPE_KYMC9_16 = ((((COLORSPACE_SH (PT_MCH9)) | (CHANNELS_SH (9))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 837
try:
    TYPE_KYMC9_16_SE = (((((COLORSPACE_SH (PT_MCH9)) | (CHANNELS_SH (9))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 838
try:
    TYPE_CMYK10_8 = (((COLORSPACE_SH (PT_MCH10)) | (CHANNELS_SH (10))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 839
try:
    TYPE_CMYK10_16 = (((COLORSPACE_SH (PT_MCH10)) | (CHANNELS_SH (10))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 840
try:
    TYPE_CMYK10_16_SE = ((((COLORSPACE_SH (PT_MCH10)) | (CHANNELS_SH (10))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 841
try:
    TYPE_KYMC10_8 = ((((COLORSPACE_SH (PT_MCH10)) | (CHANNELS_SH (10))) | (BYTES_SH (1))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 842
try:
    TYPE_KYMC10_16 = ((((COLORSPACE_SH (PT_MCH10)) | (CHANNELS_SH (10))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 843
try:
    TYPE_KYMC10_16_SE = (((((COLORSPACE_SH (PT_MCH10)) | (CHANNELS_SH (10))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 844
try:
    TYPE_CMYK11_8 = (((COLORSPACE_SH (PT_MCH11)) | (CHANNELS_SH (11))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 845
try:
    TYPE_CMYK11_16 = (((COLORSPACE_SH (PT_MCH11)) | (CHANNELS_SH (11))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 846
try:
    TYPE_CMYK11_16_SE = ((((COLORSPACE_SH (PT_MCH11)) | (CHANNELS_SH (11))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 847
try:
    TYPE_KYMC11_8 = ((((COLORSPACE_SH (PT_MCH11)) | (CHANNELS_SH (11))) | (BYTES_SH (1))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 848
try:
    TYPE_KYMC11_16 = ((((COLORSPACE_SH (PT_MCH11)) | (CHANNELS_SH (11))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 849
try:
    TYPE_KYMC11_16_SE = (((((COLORSPACE_SH (PT_MCH11)) | (CHANNELS_SH (11))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 850
try:
    TYPE_CMYK12_8 = (((COLORSPACE_SH (PT_MCH12)) | (CHANNELS_SH (12))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 851
try:
    TYPE_CMYK12_16 = (((COLORSPACE_SH (PT_MCH12)) | (CHANNELS_SH (12))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 852
try:
    TYPE_CMYK12_16_SE = ((((COLORSPACE_SH (PT_MCH12)) | (CHANNELS_SH (12))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 853
try:
    TYPE_KYMC12_8 = ((((COLORSPACE_SH (PT_MCH12)) | (CHANNELS_SH (12))) | (BYTES_SH (1))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 854
try:
    TYPE_KYMC12_16 = ((((COLORSPACE_SH (PT_MCH12)) | (CHANNELS_SH (12))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 855
try:
    TYPE_KYMC12_16_SE = (((((COLORSPACE_SH (PT_MCH12)) | (CHANNELS_SH (12))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 858
try:
    TYPE_XYZ_16 = (((COLORSPACE_SH (PT_XYZ)) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 859
try:
    TYPE_Lab_8 = (((COLORSPACE_SH (PT_Lab)) | (CHANNELS_SH (3))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 860
try:
    TYPE_LabV2_8 = (((COLORSPACE_SH (PT_LabV2)) | (CHANNELS_SH (3))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 862
try:
    TYPE_ALab_8 = (((((COLORSPACE_SH (PT_Lab)) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (EXTRA_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 863
try:
    TYPE_ALabV2_8 = (((((COLORSPACE_SH (PT_LabV2)) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (EXTRA_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 864
try:
    TYPE_Lab_16 = (((COLORSPACE_SH (PT_Lab)) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 865
try:
    TYPE_LabV2_16 = (((COLORSPACE_SH (PT_LabV2)) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 866
try:
    TYPE_Yxy_16 = (((COLORSPACE_SH (PT_Yxy)) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 869
try:
    TYPE_YCbCr_8 = (((COLORSPACE_SH (PT_YCbCr)) | (CHANNELS_SH (3))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 870
try:
    TYPE_YCbCr_8_PLANAR = ((((COLORSPACE_SH (PT_YCbCr)) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 871
try:
    TYPE_YCbCr_16 = (((COLORSPACE_SH (PT_YCbCr)) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 872
try:
    TYPE_YCbCr_16_PLANAR = ((((COLORSPACE_SH (PT_YCbCr)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 873
try:
    TYPE_YCbCr_16_SE = ((((COLORSPACE_SH (PT_YCbCr)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 876
try:
    TYPE_YUV_8 = (((COLORSPACE_SH (PT_YUV)) | (CHANNELS_SH (3))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 877
try:
    TYPE_YUV_8_PLANAR = ((((COLORSPACE_SH (PT_YUV)) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 878
try:
    TYPE_YUV_16 = (((COLORSPACE_SH (PT_YUV)) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 879
try:
    TYPE_YUV_16_PLANAR = ((((COLORSPACE_SH (PT_YUV)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 880
try:
    TYPE_YUV_16_SE = ((((COLORSPACE_SH (PT_YUV)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 883
try:
    TYPE_HLS_8 = (((COLORSPACE_SH (PT_HLS)) | (CHANNELS_SH (3))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 884
try:
    TYPE_HLS_8_PLANAR = ((((COLORSPACE_SH (PT_HLS)) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 885
try:
    TYPE_HLS_16 = (((COLORSPACE_SH (PT_HLS)) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 886
try:
    TYPE_HLS_16_PLANAR = ((((COLORSPACE_SH (PT_HLS)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 887
try:
    TYPE_HLS_16_SE = ((((COLORSPACE_SH (PT_HLS)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 890
try:
    TYPE_HSV_8 = (((COLORSPACE_SH (PT_HSV)) | (CHANNELS_SH (3))) | (BYTES_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 891
try:
    TYPE_HSV_8_PLANAR = ((((COLORSPACE_SH (PT_HSV)) | (CHANNELS_SH (3))) | (BYTES_SH (1))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 892
try:
    TYPE_HSV_16 = (((COLORSPACE_SH (PT_HSV)) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 893
try:
    TYPE_HSV_16_PLANAR = ((((COLORSPACE_SH (PT_HSV)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (PLANAR_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 894
try:
    TYPE_HSV_16_SE = ((((COLORSPACE_SH (PT_HSV)) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (ENDIAN16_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 897
try:
    TYPE_NAMED_COLOR_INDEX = ((CHANNELS_SH (1)) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 900
try:
    TYPE_XYZ_FLT = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_XYZ))) | (CHANNELS_SH (3))) | (BYTES_SH (4)))
except:
    pass

# /usr/include/lcms2.h: 901
try:
    TYPE_Lab_FLT = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_Lab))) | (CHANNELS_SH (3))) | (BYTES_SH (4)))
except:
    pass

# /usr/include/lcms2.h: 902
try:
    TYPE_LabA_FLT = (((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_Lab))) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (4)))
except:
    pass

# /usr/include/lcms2.h: 903
try:
    TYPE_GRAY_FLT = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_GRAY))) | (CHANNELS_SH (1))) | (BYTES_SH (4)))
except:
    pass

# /usr/include/lcms2.h: 904
try:
    TYPE_RGB_FLT = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (CHANNELS_SH (3))) | (BYTES_SH (4)))
except:
    pass

# /usr/include/lcms2.h: 906
try:
    TYPE_RGBA_FLT = (((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (4)))
except:
    pass

# /usr/include/lcms2.h: 907
try:
    TYPE_ARGB_FLT = ((((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (4))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 908
try:
    TYPE_BGR_FLT = (((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (CHANNELS_SH (3))) | (BYTES_SH (4))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 909
try:
    TYPE_BGRA_FLT = (((((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (4))) | (DOSWAP_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 910
try:
    TYPE_ABGR_FLT = ((((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (4))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 912
try:
    TYPE_CMYK_FLT = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_CMYK))) | (CHANNELS_SH (4))) | (BYTES_SH (4)))
except:
    pass

# /usr/include/lcms2.h: 916
try:
    TYPE_XYZ_DBL = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_XYZ))) | (CHANNELS_SH (3))) | (BYTES_SH (0)))
except:
    pass

# /usr/include/lcms2.h: 917
try:
    TYPE_Lab_DBL = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_Lab))) | (CHANNELS_SH (3))) | (BYTES_SH (0)))
except:
    pass

# /usr/include/lcms2.h: 918
try:
    TYPE_GRAY_DBL = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_GRAY))) | (CHANNELS_SH (1))) | (BYTES_SH (0)))
except:
    pass

# /usr/include/lcms2.h: 919
try:
    TYPE_RGB_DBL = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (CHANNELS_SH (3))) | (BYTES_SH (0)))
except:
    pass

# /usr/include/lcms2.h: 920
try:
    TYPE_BGR_DBL = (((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (CHANNELS_SH (3))) | (BYTES_SH (0))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 921
try:
    TYPE_CMYK_DBL = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_CMYK))) | (CHANNELS_SH (4))) | (BYTES_SH (0)))
except:
    pass

# /usr/include/lcms2.h: 924
try:
    TYPE_GRAY_HALF_FLT = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_GRAY))) | (CHANNELS_SH (1))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 925
try:
    TYPE_RGB_HALF_FLT = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 926
try:
    TYPE_RGBA_HALF_FLT = (((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 927
try:
    TYPE_CMYK_HALF_FLT = ((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_CMYK))) | (CHANNELS_SH (4))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 929
try:
    TYPE_RGBA_HALF_FLT = (((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2)))
except:
    pass

# /usr/include/lcms2.h: 930
try:
    TYPE_ARGB_HALF_FLT = ((((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 931
try:
    TYPE_BGR_HALF_FLT = (((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 932
try:
    TYPE_BGRA_HALF_FLT = (((((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (EXTRA_SH (1))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (DOSWAP_SH (1))) | (SWAPFIRST_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 933
try:
    TYPE_ABGR_HALF_FLT = (((((FLOAT_SH (1)) | (COLORSPACE_SH (PT_RGB))) | (CHANNELS_SH (3))) | (BYTES_SH (2))) | (DOSWAP_SH (1)))
except:
    pass

# /usr/include/lcms2.h: 988
try:
    cmsILLUMINANT_TYPE_UNKNOWN = 0
except:
    pass

# /usr/include/lcms2.h: 989
try:
    cmsILLUMINANT_TYPE_D50 = 1
except:
    pass

# /usr/include/lcms2.h: 990
try:
    cmsILLUMINANT_TYPE_D65 = 2
except:
    pass

# /usr/include/lcms2.h: 991
try:
    cmsILLUMINANT_TYPE_D93 = 3
except:
    pass

# /usr/include/lcms2.h: 992
try:
    cmsILLUMINANT_TYPE_F2 = 4
except:
    pass

# /usr/include/lcms2.h: 993
try:
    cmsILLUMINANT_TYPE_D55 = 5
except:
    pass

# /usr/include/lcms2.h: 994
try:
    cmsILLUMINANT_TYPE_A = 6
except:
    pass

# /usr/include/lcms2.h: 995
try:
    cmsILLUMINANT_TYPE_E = 7
except:
    pass

# /usr/include/lcms2.h: 996
try:
    cmsILLUMINANT_TYPE_F8 = 8
except:
    pass

# /usr/include/lcms2.h: 1055
try:
    cmsERROR_UNDEFINED = 0
except:
    pass

# /usr/include/lcms2.h: 1056
try:
    cmsERROR_FILE = 1
except:
    pass

# /usr/include/lcms2.h: 1057
try:
    cmsERROR_RANGE = 2
except:
    pass

# /usr/include/lcms2.h: 1058
try:
    cmsERROR_INTERNAL = 3
except:
    pass

# /usr/include/lcms2.h: 1059
try:
    cmsERROR_NULL = 4
except:
    pass

# /usr/include/lcms2.h: 1060
try:
    cmsERROR_READ = 5
except:
    pass

# /usr/include/lcms2.h: 1061
try:
    cmsERROR_SEEK = 6
except:
    pass

# /usr/include/lcms2.h: 1062
try:
    cmsERROR_WRITE = 7
except:
    pass

# /usr/include/lcms2.h: 1063
try:
    cmsERROR_UNKNOWN_EXTENSION = 8
except:
    pass

# /usr/include/lcms2.h: 1064
try:
    cmsERROR_COLORSPACE_CHECK = 9
except:
    pass

# /usr/include/lcms2.h: 1065
try:
    cmsERROR_ALREADY_DEFINED = 10
except:
    pass

# /usr/include/lcms2.h: 1066
try:
    cmsERROR_BAD_SIGNATURE = 11
except:
    pass

# /usr/include/lcms2.h: 1067
try:
    cmsERROR_CORRUPTION_DETECTED = 12
except:
    pass

# /usr/include/lcms2.h: 1068
try:
    cmsERROR_NOT_SUITABLE = 13
except:
    pass

# /usr/include/lcms2.h: 1125
try:
    AVG_SURROUND = 1
except:
    pass

# /usr/include/lcms2.h: 1126
try:
    DIM_SURROUND = 2
except:
    pass

# /usr/include/lcms2.h: 1127
try:
    DARK_SURROUND = 3
except:
    pass

# /usr/include/lcms2.h: 1128
try:
    CUTSHEET_SURROUND = 4
except:
    pass

# /usr/include/lcms2.h: 1130
try:
    D_CALCULATE = (-1)
except:
    pass

# /usr/include/lcms2.h: 1259
try:
    SAMPLER_INSPECT = 16777216
except:
    pass

# /usr/include/lcms2.h: 1276
try:
    cmsNoLanguage = '\\0\\0'
except:
    pass

# /usr/include/lcms2.h: 1277
try:
    cmsNoCountry = '\\0\\0'
except:
    pass

# /usr/include/lcms2.h: 1320
try:
    cmsPRINTER_DEFAULT_SCREENS = 1
except:
    pass

# /usr/include/lcms2.h: 1321
try:
    cmsFREQUENCE_UNITS_LINES_CM = 0
except:
    pass

# /usr/include/lcms2.h: 1322
try:
    cmsFREQUENCE_UNITS_LINES_INCH = 2
except:
    pass

# /usr/include/lcms2.h: 1324
try:
    cmsSPOT_UNKNOWN = 0
except:
    pass

# /usr/include/lcms2.h: 1325
try:
    cmsSPOT_PRINTER_DEFAULT = 1
except:
    pass

# /usr/include/lcms2.h: 1326
try:
    cmsSPOT_ROUND = 2
except:
    pass

# /usr/include/lcms2.h: 1327
try:
    cmsSPOT_DIAMOND = 3
except:
    pass

# /usr/include/lcms2.h: 1328
try:
    cmsSPOT_ELLIPSE = 4
except:
    pass

# /usr/include/lcms2.h: 1329
try:
    cmsSPOT_LINE = 5
except:
    pass

# /usr/include/lcms2.h: 1330
try:
    cmsSPOT_SQUARE = 6
except:
    pass

# /usr/include/lcms2.h: 1331
try:
    cmsSPOT_CROSS = 7
except:
    pass

# /usr/include/lcms2.h: 1445
try:
    cmsEmbeddedProfileFalse = 0
except:
    pass

# /usr/include/lcms2.h: 1446
try:
    cmsEmbeddedProfileTrue = 1
except:
    pass

# /usr/include/lcms2.h: 1447
try:
    cmsUseAnywhere = 0
except:
    pass

# /usr/include/lcms2.h: 1448
try:
    cmsUseWithEmbeddedDataOnly = 2
except:
    pass

# /usr/include/lcms2.h: 1482
try:
    LCMS_USED_AS_INPUT = 0
except:
    pass

# /usr/include/lcms2.h: 1483
try:
    LCMS_USED_AS_OUTPUT = 1
except:
    pass

# /usr/include/lcms2.h: 1484
try:
    LCMS_USED_AS_PROOF = 2
except:
    pass

# /usr/include/lcms2.h: 1617
try:
    INTENT_PERCEPTUAL = 0
except:
    pass

# /usr/include/lcms2.h: 1618
try:
    INTENT_RELATIVE_COLORIMETRIC = 1
except:
    pass

# /usr/include/lcms2.h: 1619
try:
    INTENT_SATURATION = 2
except:
    pass

# /usr/include/lcms2.h: 1620
try:
    INTENT_ABSOLUTE_COLORIMETRIC = 3
except:
    pass

# /usr/include/lcms2.h: 1623
try:
    INTENT_PRESERVE_K_ONLY_PERCEPTUAL = 10
except:
    pass

# /usr/include/lcms2.h: 1624
try:
    INTENT_PRESERVE_K_ONLY_RELATIVE_COLORIMETRIC = 11
except:
    pass

# /usr/include/lcms2.h: 1625
try:
    INTENT_PRESERVE_K_ONLY_SATURATION = 12
except:
    pass

# /usr/include/lcms2.h: 1626
try:
    INTENT_PRESERVE_K_PLANE_PERCEPTUAL = 13
except:
    pass

# /usr/include/lcms2.h: 1627
try:
    INTENT_PRESERVE_K_PLANE_RELATIVE_COLORIMETRIC = 14
except:
    pass

# /usr/include/lcms2.h: 1628
try:
    INTENT_PRESERVE_K_PLANE_SATURATION = 15
except:
    pass

# /usr/include/lcms2.h: 1636
try:
    cmsFLAGS_NOCACHE = 64
except:
    pass

# /usr/include/lcms2.h: 1637
try:
    cmsFLAGS_NOOPTIMIZE = 256
except:
    pass

# /usr/include/lcms2.h: 1638
try:
    cmsFLAGS_NULLTRANSFORM = 512
except:
    pass

# /usr/include/lcms2.h: 1641
try:
    cmsFLAGS_GAMUTCHECK = 4096
except:
    pass

# /usr/include/lcms2.h: 1642
try:
    cmsFLAGS_SOFTPROOFING = 16384
except:
    pass

# /usr/include/lcms2.h: 1645
try:
    cmsFLAGS_BLACKPOINTCOMPENSATION = 8192
except:
    pass

# /usr/include/lcms2.h: 1646
try:
    cmsFLAGS_NOWHITEONWHITEFIXUP = 4
except:
    pass

# /usr/include/lcms2.h: 1647
try:
    cmsFLAGS_HIGHRESPRECALC = 1024
except:
    pass

# /usr/include/lcms2.h: 1648
try:
    cmsFLAGS_LOWRESPRECALC = 2048
except:
    pass

# /usr/include/lcms2.h: 1651
try:
    cmsFLAGS_8BITS_DEVICELINK = 8
except:
    pass

# /usr/include/lcms2.h: 1652
try:
    cmsFLAGS_GUESSDEVICECLASS = 32
except:
    pass

# /usr/include/lcms2.h: 1653
try:
    cmsFLAGS_KEEP_SEQUENCE = 128
except:
    pass

# /usr/include/lcms2.h: 1656
try:
    cmsFLAGS_FORCE_CLUT = 2
except:
    pass

# /usr/include/lcms2.h: 1657
try:
    cmsFLAGS_CLUT_POST_LINEARIZATION = 1
except:
    pass

# /usr/include/lcms2.h: 1658
try:
    cmsFLAGS_CLUT_PRE_LINEARIZATION = 16
except:
    pass

# /usr/include/lcms2.h: 1661
try:
    cmsFLAGS_NONEGATIVES = 32768
except:
    pass

# /usr/include/lcms2.h: 1664
try:
    cmsFLAGS_COPY_ALPHA = 67108864
except:
    pass

# /usr/include/lcms2.h: 1667
def cmsFLAGS_GRIDPOINTS(n):
    return ((n & 255) << 16)

# /usr/include/lcms2.h: 1670
try:
    cmsFLAGS_NODEFAULTRESOURCEDEF = 16777216
except:
    pass

# /usr/include/lcms2_plugin.h: 66
try:
    VX = 0
except:
    pass

# /usr/include/lcms2_plugin.h: 67
try:
    VY = 1
except:
    pass

# /usr/include/lcms2_plugin.h: 68
try:
    VZ = 2
except:
    pass

# /usr/include/lcms2_plugin.h: 193
try:
    cmsPluginMagicNumber = 1633906800
except:
    pass

# /usr/include/lcms2_plugin.h: 195
try:
    cmsPluginMemHandlerSig = 1835363656
except:
    pass

# /usr/include/lcms2_plugin.h: 196
try:
    cmsPluginInterpolationSig = 1768845384
except:
    pass

# /usr/include/lcms2_plugin.h: 197
try:
    cmsPluginParametricCurveSig = 1885434440
except:
    pass

# /usr/include/lcms2_plugin.h: 198
try:
    cmsPluginFormattersSig = 1718775112
except:
    pass

# /usr/include/lcms2_plugin.h: 199
try:
    cmsPluginTagTypeSig = 1954115656
except:
    pass

# /usr/include/lcms2_plugin.h: 200
try:
    cmsPluginTagSig = 1952540488
except:
    pass

# /usr/include/lcms2_plugin.h: 201
try:
    cmsPluginRenderingIntentSig = 1768846408
except:
    pass

# /usr/include/lcms2_plugin.h: 202
try:
    cmsPluginMultiProcessElementSig = 1836082504
except:
    pass

# /usr/include/lcms2_plugin.h: 203
try:
    cmsPluginOptimizationSig = 1869640776
except:
    pass

# /usr/include/lcms2_plugin.h: 204
try:
    cmsPluginTransformSig = 2053533000
except:
    pass

# /usr/include/lcms2_plugin.h: 205
try:
    cmsPluginMutexSig = 1836350024
except:
    pass

# /usr/include/lcms2_plugin.h: 217
try:
    MAX_TYPES_IN_LCMS_PLUGIN = 20
except:
    pass

# /usr/include/lcms2_plugin.h: 278
try:
    CMS_LERP_FLAGS_16BITS = 0
except:
    pass

# /usr/include/lcms2_plugin.h: 279
try:
    CMS_LERP_FLAGS_FLOAT = 1
except:
    pass

# /usr/include/lcms2_plugin.h: 280
try:
    CMS_LERP_FLAGS_TRILINEAR = 256
except:
    pass

# /usr/include/lcms2_plugin.h: 283
try:
    MAX_INPUT_DIMENSIONS = 8
except:
    pass

# /usr/include/lcms2_plugin.h: 360
try:
    CMS_PACK_FLAGS_16BITS = 0
except:
    pass

# /usr/include/lcms2_plugin.h: 361
try:
    CMS_PACK_FLAGS_FLOAT = 1
except:
    pass

_cmsContext_struct = struct__cmsContext_struct# /usr/include/lcms2.h: 1029

_cms_curve_struct = struct__cms_curve_struct# /usr/include/lcms2.h: 1162

_cmsPipeline_struct = struct__cmsPipeline_struct# /usr/include/lcms2.h: 1193

_cmsStage_struct = struct__cmsStage_struct# /usr/include/lcms2.h: 1194

_cms_MLU_struct = struct__cms_MLU_struct# /usr/include/lcms2.h: 1274

_cms_NAMEDCOLORLIST_struct = struct__cms_NAMEDCOLORLIST_struct# /usr/include/lcms2.h: 1350

_cmsDICTentry_struct = struct__cmsDICTentry_struct# /usr/include/lcms2.h: 1407

_cms_io_handler = struct__cms_io_handler# /usr/include/lcms2_plugin.h: 112

_cmsPluginBaseStruct = struct__cmsPluginBaseStruct# /usr/include/lcms2_plugin.h: 207

_cms_interp_struc = struct__cms_interp_struc# /usr/include/lcms2_plugin.h: 285

_cmstransform_struct = struct__cmstransform_struct# /usr/include/lcms2_plugin.h: 341

_cms_typehandler_struct = struct__cms_typehandler_struct# /usr/include/lcms2_plugin.h: 380

# No inserted files

# No prefix-stripping

