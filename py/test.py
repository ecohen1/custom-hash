#! /usr/bin/env python

	# This test script loads both hash table implementations and performs a randomized sequence of actions on them.
	# Each action (either SET, GET, or DELETE) is timed and recorded. 
	# The average of each, and the average of all three, are presented for each implementation, as well as the number of collisions.

from time import time
import random
import basichash
import goodhash

# CONSTANTS
SET = 0
GET = 1
DEL = 2
itr = 100.0 # number of times to repeat the action sequence to obtain an accurate estimate
size = 10000 # size of the hashtable
ops = 25000 # number of operations

# VARIABLES
setTime = 0 # total time spent setting
getTime = 0 # total time spent getting
delTime = 0 # total time spent deleting
setOps = 0.0 # number of setting operations
getOps = 0.0 # number of getting operations
delOps = 0.0 # number of deleting operations
actions = [ int(10*random.random()) % 3 for i in range(ops) ] # generate randomized set/get/del sequence, but same between the two implementations

# SANITY TEST
def sanityTest(Hash):
	myHash = Hash
	k2 = 1
	k3 = -1
	print myHash.get("k1")					# None
	print myHash.set("k1",1)				# True
	print myHash.load()						# 0.5
	print myHash.set(k2,"2")				# True
	print myHash.load()						# 1.0
	print myHash.set(k3,"doesn't work")		# False
	print myHash.load()						# 1.0
	print myHash.get("k1")					# 1
	print myHash.get(k2)					# 2
	print myHash.get(k3)					# None
	print myHash.delete("k1")				# 1
	print myHash.load()						# 0.5
	print myHash.get("k1")					# None
	print myHash.get(k2)					# 2
	print myHash.delete(k2)					# 2
	print myHash.load()						# 0.0
	print myHash.get(k2)					# None
	print '\n\n\n'

# TEST BOTH HASH CLASSES
def initHash(hashType):
	global itr,size,ops,SET,GET,DEL,setTime,getTime,delTime,setOps,getOps,delOps
	print hashType
	# perform time calculations and basic sanity tests on each implementation
	if hashType == 'basichash':
		calcTime(basichash.Hash(size))
		sanityTest(basichash.Hash(2))
	elif hashType == 'goodhash':
		calcTime(goodhash.Hash(size))
		sanityTest(goodhash.Hash(2))

# ESTIMATE THE RUNTIMES FOR EACH IMPLEMENTATION
def calcTime(myHash):
	global itr,size,ops,SET,GET,DEL,setTime,getTime,delTime,setOps,getOps,delOps,actions
	setTime = 0
	getTime = 0
	delTime = 0
	keyArr = []
	for i in range(ops):
		action = actions[i]
		if action == SET: #add element to the hash table
			setOps += 1
			# generate random keys and values
			key = str(random.random())
			val = str(random.random())
			# time the operation
			startTime = time()
			result = myHash.set(key,val)
			setTime += time() - startTime
			# add to a list of valid keys
			if result:
				keyArr.append(key)
		elif action == GET: # retrieve element from the table
			# check that there are keys for us to search for
			if len(keyArr) != 0:
				getOps += 1
				# find a key
				keyIndex = int(size*random.random()) % len(keyArr)
				key = keyArr[keyIndex]
				# time the operation
				startTime = time()
				myHash.get(key)
				getTime += time() - startTime
		elif action == DEL: # delete element from the table
			# check that there are keys for us to search for
			if len(keyArr) != 0:
				delOps += 1
				# find a key
				keyIndex = int(size*random.random()) % len(keyArr)
				key = keyArr[keyIndex]
				# time the operation
				startTime = time()
				myHash.delete(key)
				delTime += time() - startTime
				# remove from our valid keys list
				keyArr.remove(key)

	# print performance characteristics
	performanceArr = [setTime/setOps, getTime/getOps, delTime/delOps]
	print 'collisions:', myHash.collisions # collisions when setting/getting/deleting
	print 'SET =',setTime/setOps # average time to set a key/value pair
	print 'GET =',getTime/getOps # average time to get a value
	print 'DEL =',delTime/delOps # average time to delete a key/value pair
	print 'AVG =',sum(performanceArr)/len(performanceArr),'\n\n\n' # average operation time

hashTypeArr = ['basichash','goodhash']

for hashType in hashTypeArr:
	initHash(hashType)