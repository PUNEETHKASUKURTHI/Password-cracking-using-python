from hashlib import sha256 as sha
import sys as s
import timeit
import time as t

try:
	s.argv[1]
	s.argv[2]
except IndexError:
	print ("Give Correct Arguments")
	exit(0)

with open(s.argv[1], 'r') as file:
	inp = file.read()
inp = inp.rstrip("\r\n")

slt,pwd = inp.split('$')

with open(s.argv[2], encoding='utf-8', errors='ignore') as file:
	ls = file.read()

def hashP(slt, pword):
	assert(slt is not None and pword is not None)
	has = sha()
	has.update(slt.encode('utf-8'))
	has.update(pword.encode('utf-8'))
	return has.hexdigest()

ls = ls.split("\n")



begin = t.time()
idd = 0
for ele in ls:
	idd += 1
	if hashP(slt,ele) == pwd:
		print (ele)
		break
fulltime = t.time() - begin

print("No. of Guess's per second : ", int(idd/fulltime))


