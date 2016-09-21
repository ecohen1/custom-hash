import hashhash as hh
import newhashhash as tch
from time import time

size = 10000
hh = hh.Hash(size)
tch = tch.Hash(size)
htime = 0
ttime = 0

for i in range(size/2):
	st = time()
	hh.set(str(i),i)
	htime += time() - st
	st = time()
	tch.set(str(i),i)
	ttime += time() - st
	print '\n\n'

print hh.notfound
print hh.looking
print htime,'\n'
print tch.notfound
print tch.looking
print ttime