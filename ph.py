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

#ids csv file of MACADDRESS,DEVICENAME
ids = {}
for key, val in csv.reader(open("ids.csv")):
    ids[key] = val

kid = list(ids.keys())

mac = nmac()

matchv = list(set(kid).intersection(mac))

matchf = list(set(kid).difference(matchv))

vb = {}
for key in matchv:
	vb[key] = True
for key in matchf:
	vb[key] = False


#----------------
#bolean dictionaries
def loop(bc):
	time.sleep(60)

	mac1 = nmac()

	matchv1 = list(set(kid).intersection(mac1))

	matchf1 = list(set(kid).difference(matchv1))

	vb1 = {}
	for key in matchv1:
        	vb1[key] = True
	for key in matchf1:
        	vb1[key] = False

	#vb1 = dict(vb)
	#False = vb1['MACADDDRES']
	chan = [k for k in bc if bc[k] != vb1[k]]

	print (chan)
	for key in chan:
		if vb1[key] == True:
			push(ids[key] + HASEN) 
		else:
			push(ids[key] + HASLE)
	loop(vb1)

loop(vb)
