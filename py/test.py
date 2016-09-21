from time import time
import random
import basichash
import hashhash
import twochoicehash

itr = 100.0
size = 10000
ops = 5000
SET = 0
GET = 1
DEL = 2
setTime = 0
getTime = 0
delTime = 0
setOps = 0
getOps = 0
delOps = 0
actions = [ int(10*random.random()) % 3 for i in range(ops) ]

# SANITY TESTS
def sanityTest(Hash):
	# myHash = Hash
	# print myHash.set("k1",{'test':'it'})
	# print myHash.load()
	# print myHash.set(1,2)
	# print myHash.load()
	# print myHash.set(-1,"z")
	# print myHash.load()
	# print myHash.get("k1")
	# print myHash.get(1)
	# print myHash.get(-1)
	# print myHash.delete("k1")
	# print myHash.load()
	# print myHash.get("k1")
	# print myHash.get(1)
	# print myHash.delete(1)
	# print myHash.load()
	# print myHash.get(1)
	print '\n\n\n'

def initHash(hashType):
	global itr,size,ops,SET,GET,DEL,setTime,getTime,delTime,setOps,getOps,delOps
	print hashType
	if hashType == 'basichash':
		calcTime(basichash.Hash(size))
		sanityTest(basichash.Hash(size))
	elif hashType == 'hashhash':
		calcTime(hashhash.Hash(size))
		sanityTest(hashhash.Hash(size))
	elif hashType == 'twochoicehash':
		calcTime(twochoicehash.Hash(size))
		sanityTest(twochoicehash.Hash(size))

def calcTime(Hash):
	global itr,size,ops,SET,GET,DEL,setTime,getTime,delTime,setOps,getOps,delOps,actions
	myHash = Hash
	keyArr = []
	for i in range(ops):
		action = actions[i]
		if action == SET:
			setOps += 1
			key = str(random.random())
			val = str(random.random())
			startTime = time()
			result = myHash.set(key,val)
			setTime += time() - startTime
			if result:
				keyArr.append(key)
		elif action == GET:
			if len(keyArr) != 0:
				getOps += 1
				keyIndex = int(size*random.random()) % len(keyArr)
				key = keyArr[keyIndex]
				startTime = time()
				myHash.get(key)
				getTime += time() - startTime
		elif action == DEL:
			if len(keyArr) != 0:
				delOps += 1
				keyIndex = int(size*random.random()) % len(keyArr)
				key = keyArr[keyIndex]
				startTime = time()
				myHash.delete(key)
				delTime += time() - startTime
				keyArr.remove(key)

	print 'not found =', myHash.notfound
	print 'SET =',setTime/(setOps)
	print 'GET =',getTime/(getOps)
	print 'DEL =',delTime/(delOps)
	print 'AVG =',float(setTime+getTime+delTime)/3,'\n\n\n'

hashTypeArr = ['basichash','hashhash','twochoicehash']

for hashType in hashTypeArr:
	initHash(hashType)

# True, .5, True, 1, False, 1, {...}, 2, None, {...}, .5, None, 2, 2, 0, None