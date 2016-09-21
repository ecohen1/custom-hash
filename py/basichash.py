#! /usr/bin/env python

class Hash:

	def __init__(self,size):
		# init parameters
		self.size = size
		self.items = 0
		# generate array of specified size with None placeholders
		self.keys = [ None for i in range(self.size) ]
		self.values = [ None for i in range(self.size) ]
		self.collisions = 0
	
	def set(self,key,value):
		# add a key/value pair to the hash table
		# only allows string or integer keys
		if isinstance(key,int) or isinstance(key,str):
			# go through the key array sequentially until empty bucket is found
			for index,k in enumerate(self.keys):
				if k is None:
					# empty bucket found, set key and value in appropriate arrays
					self.keys[index] = key
					self.values[index] = value
					self.items += 1
					return True
				# otherwise, record the collision
				self.collisions += 1
		return False

	def get(self,key):
		# access a value from the hash table given its key
		if isinstance(key,int) or isinstance(key,str):
			# iterate sequentially
			for index,k in enumerate(self.keys):
				if k == key:
					# return the key
					return self.values[index]
				# otherwise, record the collision
				self.collisions += 1
		return None

	def delete(self,key):
		# remove a key/value pair from the hash table
		if isinstance(key,int) or isinstance(key,str):
			# iterate sequentially
			for index,k in enumerate(self.keys):
				if k == key:
					# set key and value back to placeholder value of None
					value = self.values[index]
					self.keys[index] = None
					self.values[index] = None
					self.items -= 1
					return value
				# otherwise, record the collision
				self.collisions += 1
		return None

	def load(self):
		# return load factor, which is kept track of as items are added/removed
		return float(self.items)/self.size
