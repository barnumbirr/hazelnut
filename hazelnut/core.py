#!/usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = 'hazelnut'
__version__ = '0.1'
__author__ = 'Martin Simon <me@martinsimon.me>'
__repo__ = 'https://github.com/c0ding/hazelnut'
__license__ = 'Apache v2.0 License'

class MemInfo(object):

	def __init__(self, path='/proc/meminfo'):
		self.path = path

	def __str__(self):
		with open(self.get_path(), 'r') as f:
			lines = [line.strip() for line in f]
			return '\n'.join(lines)

	def __repr__(self):
		return self.__str__()

	def get_path(self):
		return self.path
	
	def dict(self):
		d = {}
		with open(self.get_path(), 'r') as f:
			d = dict(x.strip().split(None, 1) for x in f)
		return d

	def search(self, inp):
		with open(self.get_path(), 'r') as f:
			match = [s for s in f if inp in s]
			# will have to figure out a way to make this case insensitive.
			# mem.search('Swap') and mem.search('swap') should both match.
			return match
