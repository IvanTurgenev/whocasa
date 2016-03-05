import subprocess
import csv
import sys
import time
from config import *
from pushetta import Pushetta

def nmac():
	x = subprocess.check_output(""" sudo nmap -sn 192.168.1.0/24 | grep --color=never -Po 'Address: \K.[^ ]*' """,shell=True).decode(sys.stdout.encoding).split("\n")
	x.pop()
	return (x)


def push(x):
#	API_KEY="YOU API KEY"
#	CHANNEL_NAME="YOUR CHANNEL NAME"
	p=Pushetta(API_KEY)
	p.pushMessage(CHANNEL_NAME, x)


#sys.exit()

def addb(dic,key,val):
	dic.setdefault(key, [])
	dic[key].append(val)

#def remb(dic,key):
#	del (dic[key])[0]

def ctb(ids,vb) :
	mac = nmac()
	matchv = list(set(kid).intersection(mac))
	matchf = list(set(kid).difference(matchv))

	for key in matchv:
		addb(vb,key,True)
	for key in matchf:
		addb(vb,key,False)
	
	return (vb)

#ids csv file of MACADDRESS,DEVICENAME
ids = {}
for key, val in csv.reader(open("ids.csv")):
    ids[key] = val

kid = list(ids.keys())

vb = {}
vb1 = {}

count = 1
while True :
	
	if not vb1:
		vb = ctb(kid,vb)	
	else:
		vb = vb1
		vb1 = {}

	if count == 10 :
		vbr = {}
		for key in vb:
			if True in vb[key]:
				vbr[key] = True
			else:
				vbr[key] = False
				
		while count != 1:
			vb1 = ctb(kid,vb1)
			count -= 1
			print("vb1")
			print(vb1)
			time.sleep(60)
			if count == 1:
				vbr1 = {}
				for key in vb1:
					if True in vb1[key]:
						vbr1[key] = True
					else:
						vbr1[key] = False
				chan = [k for k in vbr if vbr[k] != vbr1[k]]
				print("chan")
				print(chan)
				for key in chan:
					if vb1[key] == True:
						push(ids[key] + HASEN)
					else:
						push(ids[key] + HASLE)
	count += 1
	print("vb")
	print(vb)
	time.sleep(60)

#----------------
#bolean dictionaries
#def loop(bc):
#	time.sleep(60)

#	mac1 = nmac()

#	matchv1 = list(set(kid).intersection(mac1))

#	matchf1 = list(set(kid).difference(matchv1))

#	vb1 = {}
#	for key in matchv1:
#        	vb1[key] = True
#	for key in matchf1:
#       	vb1[key] = False

	#vb1 = dict(vb)
	#False = vb1['MACADDDRES']
#	chan = [k for k in bc if bc[k] != vb1[k]]

#	print (chan)
#	for key in chan:
#		if vb1[key] == True:
#			push(ids[key] + HASEN) 
#		else:
#			push(ids[key] + HASLE)
#	loop(vb1)

#loop(vb)
