from timeit import timeit
from hashhash import Hash

itr = 100
endCodeString = '''\
import random
myHash = hashlib.Hash(size)
keyArr = []
for i in range(size/2):
	key = str(random.random())
	myHash.set(key,str(random.random()))
	keyArr.append(key)
for key in keyArr:
	myHash.get(key)
for key in keyArr:
	myHash.delete(key)
# END'''

def calcTime(string):
	totaltime = timeit(string,number=itr)
	print '\n\n\nTOTAL =',totaltime
	print 'AVG =',float(totaltime)/itr,'\n\n\n'

# BASIC
basichash = '''\
# PARAMS
size = 1000
# CODE
import basichash as hashlib
''' + endCodeString
calcTime(basichash)

# HASH
hashhash = '''\
# PARAMS
size = 1000
# CODE
import hashhash as hashlib
''' + endCodeString
calcTime(hashhash)

# SANITY TESTS
myHash = Hash(2)
print myHash.set("k1",{'test':'it'})
print myHash.load()
print myHash.set(1,2)
print myHash.load()
print myHash.set(-1,"z")
print myHash.load()
print myHash.get("k1")
print myHash.get(1)
print myHash.get(-1)
print myHash.delete("k1")
print myHash.load()
print myHash.get("k1")
print myHash.get(1)
print myHash.delete(1)
print myHash.load()
print myHash.get(1)

# True, .5, True, 1, False, 1, {...}, 2, None, {...}, .5, None, 2, 2, 0, None