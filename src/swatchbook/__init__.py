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
from datetime import *
from color import *

__version__ = "0.7"

# from http://code.djangoproject.com/browser/django/trunk/django/utils/datastructures.py
class SortedDict(dict):
	"""
	A dictionary that keeps its keys in the order in which they're inserted.
	"""
	def __new__(cls, *args, **kwargs):
		instance = super(SortedDict, cls).__new__(cls, *args, **kwargs)
		instance.keyOrder = []
		return instance

	def __init__(self, data=None):
		if data is None:
			data = {}
		super(SortedDict, self).__init__(data)
		if isinstance(data, dict):
			self.keyOrder = data.keys()
		else:
			self.keyOrder = []
			for key, value in data:
				if key not in self.keyOrder:
					self.keyOrder.append(key)

	def __deepcopy__(self, memo):
		from copy import deepcopy
		return self.__class__([(key, deepcopy(value, memo))
							   for key, value in self.iteritems()])

	def __setitem__(self, key, value):
		super(SortedDict, self).__setitem__(key, value)
		if key not in self.keyOrder:
			self.keyOrder.append(key)

	def __delitem__(self, key):
		super(SortedDict, self).__delitem__(key)
		self.keyOrder.remove(key)

	def __iter__(self):
		for k in self.keyOrder:
			yield k

	def pop(self, k, *args):
		result = super(SortedDict, self).pop(k, *args)
		try:
			self.keyOrder.remove(k)
		except ValueError:
			# Key wasn't in the dictionary in the first place. No problem.
			pass
		return result

	def popitem(self):
		result = super(SortedDict, self).popitem()
		self.keyOrder.remove(result[0])
		return result

	def items(self):
		return zip(self.keyOrder, self.values())

	def iteritems(self):
		for key in self.keyOrder:
			yield key, super(SortedDict, self).__getitem__(key)

	def keys(self):
		return self.keyOrder[:]

	def iterkeys(self):
		return iter(self.keyOrder)

	def values(self):
		return [super(SortedDict, self).__getitem__(k) for k in self.keyOrder]

	def itervalues(self):
		for key in self.keyOrder:
			yield super(SortedDict, self).__getitem__(key)

	def update(self, dict_):
		for k, v in dict_.items():
			self.__setitem__(k, v)

	def setdefault(self, key, default):
		if key not in self.keyOrder:
			self.keyOrder.append(key)
		return super(SortedDict, self).setdefault(key, default)

	def value_for_index(self, index):
		"""Returns the value of the item at the given zero-based index."""
		return self[self.keyOrder[index]]

	def insert(self, index, key, value):
		"""Inserts the key, value pair before the item with the given index."""
		if key in self.keyOrder:
			n = self.keyOrder.index(key)
			del self.keyOrder[n]
			if n < index:
				index -= 1
		self.keyOrder.insert(index, key)
		super(SortedDict, self).__setitem__(key, value)

	def copy(self):
		"""Returns a copy of this object."""
		# This way of initializing the copy means it works for subclasses, too.
		obj = self.__class__(self)
		obj.keyOrder = self.keyOrder[:]
		return obj

	def __repr__(self):
		"""
		Replaces the normal dict.__repr__ with a version that returns the keys
		in their sorted order.
		"""
		return '{%s}' % ', '.join(['%r: %r' % (k, v) for k, v in self.items()])

	def clear(self):
		super(SortedDict, self).clear()
		self.keyOrder = []

class FileFormatError(Exception):
	pass

class Info(object):
	# Dublin Core (translatable,longtext)
	dc = {'contributor': (True,True),
	      'coverage': (True,False),
	      'creator': (True,False),
	      'description': (True,True),
	      'identifier': (False,False),
	      'language': (False,False),
	      'publisher': (True,False),
	      'relation': (True,False),
	      'rights': (True,True),
	      'source': (True,False),
	      'subject': (True,False),
	      'title': (True,False),
	      # DCMI Metadata Terms
	      'license': (False,False)}

	def __init__(self):
		self.format = 'application/swatchbook'
		self.type = 'http://purl.org/dc/dcmitype/Dataset'
		self.date = False
		for dc in self.dc:
			exec('self.'+dc+' = ""')
			if self.dc[dc][0]:
				exec('self.'+dc+'_l10n = {}')

		self.version = ""

class Book(object):
	def __init__(self):
		self.display = {'rows': False,
		                'columns': False}
		self.items = [] # Group,Swatch,Spacer,Break

class SwatchBook(object):
	"""Output values
       sRGB,RGB,HSV,HSL,CMY,CMYK,nCLR: 0 -> 1
       YIQ: Y 0 -> 1 : IQ -0.5 -> 0.5
       Lab: L 0 -> 100 : ab -128 -> 127
       XYZ: 0 -> ~100 (cfr. ref)"""

	def __init__(self, file=False,codec=False,websvc=False,webid=False):
		self.info = Info()
		self.profiles = {}
		self.materials = {}
		self.book = Book()
		self.codec = False

		if file:
			self.read(file,codec)
		elif websvc:
			self.webread(websvc,webid)

	def test(self,file,codec=False):
		# test 1: codec
		test = False
		if codec:
			try:
				test = eval('codecs.'+codec).test(file)
			except (IOError,SyntaxError,struct.error):
				codec = False
			if test:
				return codec
		# test 2: extension
		ext =  os.path.splitext(os.path.basename(file))[1].lower()[1:]
		if ext in codecs.readexts:
			for codec in codecs.readexts[ext]:
				test = False
				try:
					test = eval('codecs.'+codec).test(file)
				except (IOError,SyntaxError,struct.error):
					pass
				if test:
					return codec
			else:
				codec = False
		# test 3: free
		for codec in codecs.reads:
			test = False
			try:
				test = eval('codecs.'+codec).test(file)
			except (IOError,SyntaxError,struct.error):
				pass
			if test: return codec
		else:
			codec = False
		return codec

	def webread(self,websvc,webid):
		import swatchbook.websvc as web
		svc = eval('web.'+websvc+'()')
		svc.read(self,webid)

	def read(self,file,codec):
		import swatchbook.codecs as codecs
		codec = self.test(file,codec)
		if codec:
			self.codec = codec
			eval('codecs.'+codec).read(self,file)
			if sys.platform == 'win32':
				encoding = "UTF-8"
			else:
				encoding = sys.getfilesystemencoding()
			if encoding == 'UTF-8' and isinstance(file,unicode):
				filename =  os.path.splitext(os.path.basename(file))[0]
			else:
				filename =  os.path.splitext(os.path.basename(file))[0].decode(encoding)
			if self.info.title == '':
				self.info.title = filename.replace('_',' ')
		else:
			raise FileFormatError

	def write(self,format,output=None):
		import swatchbook.codecs as codecs
		if format in codecs.writes:
			codec = eval('codecs.'+format)
			if output == None:
				print codec.write(self)
			else:
				content = codec.write(self)
				# TODO check if writable
				bookfile = open(output, 'wb')
				bookfile.write(content)
				bookfile.close()
		else:
			raise FileFormatError,'unsupported output format'

class Group(object):
	def __init__(self,parent=None):
		self.info = Info()
		self.items = []

class Swatch(object):
	def __init__(self,material,parent=None):
		self.material = material

class Spacer(object):
	def __init__(self,parent=None):
		pass

class Break(object):
	def __init__(self,parent=None):
		pass

class Color(object):
	def __init__(self,swatchbook=None):
		self.info = Info()
		self.values = SortedDict()
		self.usage = []
		self.extra = {}
		self.swatchbook = swatchbook

	def toRGB(self,prof_out=False):
		for key in self.values:
			if key[1]:
				prof_in = self.swatchbook.profiles[key[1]].uri
			else:
				prof_in = False
			if toRGB(key[0],self.values[key],prof_in,prof_out):
				return toRGB(key[0],self.values[key],prof_in,prof_out)
				break
		else:
			return False
			
	def toRGB8(self,prof_out=False):
		if self.toRGB(prof_out):
			R,G,B = self.toRGB(prof_out)
			return (int(round(R*0xFF)),int(round(G*0xFF)),int(round(B*0xFF)))
		else:
			return False