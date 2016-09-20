#! /usr/bin/env python

class Hash:

	def __init__(self,size):
		self.size = size
		self.items = 0
		self.keys = [ None for i in range(self.size) ]
		self.values = [ None for i in range(self.size) ]
	
	def set(self,key,value):
		if isinstance(key,int) or isinstance(key,str):
			for index,k in enumerate(self.keys):
				if k is None:
					self.keys[index] = key
					self.values[index] = value
					self.items += 1
					return True
		return False

	def get(self,key):
		if isinstance(key,int) or isinstance(key,str):
			for index,k in enumerate(self.keys):
				if k == key:
					return self.values[index]
		return None

	def delete(self,key):
		if isinstance(key,int) or isinstance(key,str):
			for index,k in enumerate(self.keys):
				if k == key:
					value = self.values[index]
					self.keys[index] = None
					self.values[index] = None
					self.items -= 1
					return value
		return None

	def load(self):
		return float(self.items)/self.size
