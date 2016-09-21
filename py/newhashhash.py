#! /usr/bin/env python

class Hash:

	def __init__(self,size):
		self.size = size
		self.items = 0
		self.keys = [ None for i in range(self.size) ]
		self.values = [ None for i in range(self.size) ]
		self.notfound = 0
		self.looking = 0
	
	def set(self,key,value):
		if isinstance(key,int) or isinstance(key,str):
			hashindex = hash(key) % self.size
			for index in range(len(self.keys[hashindex:len(self.keys)])):
				quadIndex = index**2
				if quadIndex >= len(self.keys[hashindex:len(self.keys)]):
					break
				k = self.keys[hashindex:len(self.keys)][quadIndex]
				self.looking += 1
				if k is None:
					print index+hashindex
					self.keys[index + hashindex] = key
					self.values[index + hashindex] = value
					self.items += 1
					return True
			for index in range(len(self.keys[0:hashindex])):
				quadIndex = index**2
				if quadIndex >= len(self.keys[0:hashindex]):
					break
				k = self.keys[hashindex:len(self.keys)][quadIndex]				
				self.looking += 1
				if k is None:
					print index+hashindex
					self.keys[index] = key
					self.values[index] = value
					self.items += 1
					return True
		self.notfound += 1
		return False

	def get(self,key):
		if isinstance(key,int) or isinstance(key,str):
			hashindex = hash(key) % self.size
			for index,k in enumerate(self.keys[hashindex:len(self.keys)]):
				if k == key:
					return self.values[index + hashindex]
				elif k is None:
					self.notfound += 1
					return None
			for index,k in enumerate(self.keys[0:hashindex]):
				if k == key:
					return self.values[index]
				elif k is None:
					self.notfound += 1
					return None
		self.notfound += 1
		return None

	def delete(self,key):
		if isinstance(key,int) or isinstance(key,str):
			hashindex = hash(key) % self.size
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
		self.notfound += 1
		return None

	def load(self):
		return float(self.items)/self.size
