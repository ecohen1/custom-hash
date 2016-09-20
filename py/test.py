from timeit import timeit
from myhash import Hash

itr = 100

# BASELINE
totaltime = 0
stmt = '''\
# PARAMS
size = 1000
# CODE
from basichash import BasicHash
import random
myHash = BasicHash(size)
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

totaltime = timeit(stmt,number=itr)
print '\n\n\nTOTAL =',totaltime
print 'AVG =',float(totaltime)/itr,'\n\n\n'

# TIMED TESTS
totaltime = 0
stmt = '''\
# PARAMS
size = 1000
# CODE
from myhash import Hash
import random
myHash = Hash(size)
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

totaltime = timeit(stmt,number=itr)
print '\n\n\nTOTAL =',totaltime
print 'AVG =',float(totaltime)/itr,'\n\n\n'

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