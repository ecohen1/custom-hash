#! /usr/bin/env python

class Hash:

	def __init__(self,size):
		self.size = size
		self.items = 0
		self.keys = [ None for i in range(self.size) ]
		self.values = [ None for i in range(self.size) ]
	
	def set(self,key,value):
		if isinstance(key,int) or isinstance(key,str):
			hashmod = hash(key) % 10
			hashindex = int( hashmod*(self.size/10) )
			for index,k in enumerate(self.keys[hashindex:len(self.keys)]):
				if k is None:
					self.keys[index + hashindex] = key
					self.values[index + hashindex] = value
					self.items += 1
					return True
			for index,k in enumerate(self.keys[0:hashindex]):
				if k is None:
					self.keys[index] = key
					self.values[index] = value
					self.items += 1
					return True
		return False

	def get(self,key):
		if isinstance(key,int) or isinstance(key,str):
			hashmod = hash(key) % 10
			hashindex = int( hashmod*(self.size/10) )
			for index,k in enumerate(self.keys[hashindex:len(self.keys)]):
				if k == key:
					return self.values[index + hashindex]
			for index,k in enumerate(self.keys[0:hashindex]):
				if k == key:
					return self.values[index]
		return None

	def delete(self,key):
		if isinstance(key,int) or isinstance(key,str):
			hashmod = hash(key) % 10
			hashindex = int( hashmod*(self.size/10) )
			for index,k in enumerate(self.keys[hashindex:len(self.keys)]):
				if k == key:
					value = self.values[index + hashindex]
					self.keys[index + hashindex] = None
					self.values[index + hashindex] = None
					self.items -= 1
					return value
			for index,k in enumerate(self.keys[0:hashindex]):
				if k == key:
					value = self.values[index]
					self.keys[index] = None
					self.values[index] = None
					self.items -= 1
					return value
		return None

	def load(self):
		return float(self.items)/self.size
