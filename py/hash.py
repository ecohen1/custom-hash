#! /usr/bin/env python

class Hash:

	def __init__(self,size):
		self.size = size
		self.items = 0
		self.values = [ { "key": None, "value": None } for i in range(self.size) ]
	
	def set(self,key,value):
		for v in self.values:
			if not v["key"]:
				v["key"] = key
				v["value"] = value
				self.items += 1
				return True
		return False

	def get(self,key):
		for v in self.values:
			if v["key"] == key:
				return v["value"]
		return None

	def delete(self,key):
		for v in self.values:
			if v["key"] == key:
				value = v["value"]
				v["key"] = None
				v["value"] = None
				self.items -= 1
				return value
		return None

	def load(self):
		return float(self.items)/self.size

myHash = Hash(2)
print myHash.set("k1","v1")
print myHash.set(1,2)
print myHash.set(-1,"z")
print myHash.get("k1")
print myHash.get(1)
print myHash.get(-1)
print myHash.delete("k1")
print myHash.get("k1")
print myHash.get(1)
print myHash.delete(1)
print myHash.get(1)

# True, True, False, v1, 2, None, v1, None, 2, 2, None
