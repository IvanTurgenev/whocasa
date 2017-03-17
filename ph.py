import os
import subprocess
import csv
import sys
import time
import config
from pushetta import Pushetta
import configuser as config

ipr = config.ipr
nmap = "nmap -sn " + ipr + " | awk '/Address:/ {print $3}' "


def nmac():
    try:
        x = subprocess.check_output(nmap,shell=True).decode(sys.stdout.encoding).split("\n")
    # print("NMAC X POP")
    # print(x.pop())
    except subprocess.CalledProcessError as e:
        cfl(  [str(e.output), "retrying in 60 seconds"])
        # print(e.output)
        # print("retrying in 60 seconds")
        time.sleep(60)
        x = nmac()
    # x.pop()
    return (x)


def push(x):
    # API_KEY="YOU API KEY"
    # CHANNEL_NAME="YOUR CHANNEL NAME"
    try:
        ps = Pushetta(config.API_KEY)
        ps.pushMessage(config.CHANNEL_NAME, x)
    except:
        cfl(  x)
# sys.exit()


def addb(dic, key, val):
    dic.setdefault(key, [])
    dic[key].append(val)


# def remb(dic,key):
# del (dic[key])[0]


def ctb(kid, vb):
    mac = nmac()
    # print("NMAC")
    # print(mac)
    matchv = list(set(kid).intersection(mac))
    matchf = list(set(kid).difference(matchv))

    for key in matchv:
        addb(vb, key, True)
    for key in matchf:
        addb(vb, key, False)
    return (vb)


def opcsv(nmbr):
    # ids csv file of MACADDRESS,DEVICENAME
    ids = {}
    for key, val in csv.reader(open(nmbr)):
        ids[key] = val
    return(list(ids.keys()), ids)


def crvbr(vbx, vbrx):
    for key in vbx:
        if True in vbx[key]:
            vbrx[key] = True
        else:
            vbrx[key] = False


def earlnot(vbrx, vbx, arlnotx):
    tme = tmee()
    for key in vbrx:
        if ((vbrx[key] is False) and
            (True in vbx[key]) and (key not in arlnotx)):
            push(ids[key] + config.HASEN + " " + tme)
            cfl(  [ids[key] + config.HASEN + " " + tme])
            arlnotx.append(key)
    return(arlnotx)


def tmee():
    return(time.strftime("%H:%M:%S"))




def cfl(ln):
    dia = time.strftime("%d %m %Y")
    with open(dia(), 'a') as f:
        f.write(join(ln+" " + tmee()+  " "+"\n"))
        print("\n".join(ln))


def lstvb(idsx, vbx):
    lst = []
    for key in vbx:
        lst.append(str(idsx[key]))
        lst.append(str(vbx[key]))
    return(lst)

def createUserConf:
    if not isfile("configuser.py"):
        conu = open("configuser.py",'x')
        cons = open("config.py",'r')
        conu.write.cons.read()
        print("NO CONFIG USER FILE DETECTED CREATING ONE FROM TEMPLATE MODIFY ACCORDINLY config.py --> configuser.py")
        sys.exit()
    elif not isfile("idsuser.csv"):
        idsu = open("idsuser.csv",'x')
        idss = open("ids.csv",'r')
        idsu.write.idss.read()
        print("NO IDS USER FILE DETECTED CREATING ONE FROM TEMPLATE MODIFY ACCORDINLY ids.csv --> idsuser.csv")
        sys.exit()



if __name__ == '__main__':
    (kid, ids) = opcsv("idsuser.csv")
    # print("KID")
    # print(kid)
    vb = {}
    vb1 = {}
    count = 1
    while True:
        # print(count)
        if not vb1:
            vb = ctb(kid, vb)
            # print("VB")
            # print(vb)
        else:
            vb = dict(vb1)
            vb1 = {}
            count = 10
        if count == 10:
            vbr = {}
            crvbr(vb, vbr)
            # print("VBR")
            # print(vbr)
            arlnot = []
            while count != 1:
                vb1 = ctb(kid, vb1)
                # print("TABLA DE VERDAD 1")
                arlnot = earlnot(vbr, vb1, arlnot)
                # print("vb1")
                # print(vb1)
                # print(time.strftime("%H:%M:%S"))
                # for key in vb1:
                # print(ids[key])
                # print(vb1[key])
                vbl1 = lstvb(ids, vb1)
                cfl(  ["vb1", tmee(), "#cicle " + str(count)] + vbl1)
                count -= 1
                time.sleep(60)
                if count == 1:
                    vbr1 = {}
                    for key in vb1:
                        if True in vb1[key]:
                            vbr1[key] = True
                        else:
                            vbr1[key] = False
                            chan = [k for k in vbr if vbr[k] != vbr1[k]]
                            # print("chan")
                            # print(chan)
                    tme = tmee()
                    for key in chan:
                        # print(ids[key])
                        if not vbr1[key]:
                            push(ids[key] + config.HASLE + " " + tme)
                        else:
                            ntf = [ids[key] + config.HASEN + " NOT NOF " + tme]
                            cfl(  ntf)
                            # print(ids[key] + config.HASEN + " NOT NOF"+tme)
                            # push(ids[key] + config.HASEN + " " + tme)
        vbl = lstvb(ids, vb)
        cfl(  ["vb", tmee(), "#cicle " + str(count)] + vbl)
        count += 1
        # print("vb")
        # print(time.strftime("%H:%M:%S"))
        time.sleep(60)
