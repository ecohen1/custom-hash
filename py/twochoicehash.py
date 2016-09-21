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
			hashArr = self.keys[:]
			hashArr.extend(hashArr[0:hashindex])
			hashArr = hashArr[hashindex:]
			for i,k in enumerate(hashArr):
				self.looking += 1
				# index = (hashindex + i) % self.size
				# k = self.keys[index]
				if k is None:
					if i < len(self.keys) - hashindex:
						i = i + hashindex
					else:
						i = i - (len(self.keys) - hashindex)
					index = i
					print index
					self.keys[index] = key
					self.values[index] = value
					self.items += 1
					return True
		self.notfound += 1
		return False

	def get(self,key):
		if isinstance(key,int) or isinstance(key,str):
			hashindex = hash(key) % self.size
			for i in range(self.size):
				index = (hashindex + i) % self.size
				k = self.keys[index]
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
			for i in range(self.size):
				index = (hashindex + i) % self.size
				k = self.keys[index]
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
