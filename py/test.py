from timeit import timeit
from hashhash import Hash

itr = 10
endCodeString = '''\
keyArr = []
for i in range(size):
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

# BASELINE
basichash = '''\
# PARAMS
size = 1000
# CODE
import basichash
import random
myHash = basichash.Hash(size)
''' + endCodeString
calcTime(basichash)

# TIMED TESTS
hashhash = '''\
# PARAMS
size = 1000
# CODE
import hashhash
import random
myHash = hashhash.Hash(size)
''' + endCodeString
calcTime(hashhash)

# FUNCTIONALITY TESTS
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