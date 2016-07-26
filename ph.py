import subprocess
import csv
import sys
import time
import config
from pushetta import Pushetta

nmap = "nmap -sn 192.168.1.0/24 | grep --color=never -Po 'Address: \K.[^ ]*'"


def nmac():
    try:
        x = subprocess.check_output(
            nmap,
            shell=True).decode(sys.stdout.encoding).split("\n")
    # print("NMAC X POP")
    # print(x.pop())
    except subprocess.CalledProcessError as e:
        print(e.output)
        print("retrying in 60 seconds")
        time.sleep(60)
        x = nmac()
    x.pop()
    return (x)


def push(x):
    # API_KEY="YOU API KEY"
    # CHANNEL_NAME="YOUR CHANNEL NAME"
    ps = Pushetta(config.API_KEY)
    ps.pushMessage(config.CHANNEL_NAME, x)


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


def prk(vbx):
    for key in vbx:
        print(vbx[key])


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
            arlnotx.append(key)
    return(arlnotx)


def tmee():
    return(time.strftime("%H:%M:%S"))


if __name__ == '__main__':

    (kid, ids) = opcsv("ids.csv")
    # print("KID")
    # print(kid)
    vb = {}
    vb1 = {}
    count = 1
    while True:
        print(count)
        if not vb1:
            vb = ctb(kid, vb)
            print("TABLA DE VERDAD")
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
                print("TABLA DE VERDAD 1")
                count -= 1
                arlnot = earlnot(vbr, vb1, arlnot)
                print("vb1")
                # print(vb1)
                print(time.strftime("%H:%M:%S"))
                for key in vb1:
                    print(ids[key])
                    print(vb1[key])
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
                        if vbr1[key]:
                            print(ids[key] + config.HASEN + " NOT NOF " + tme)
                            # push(ids[key] + config.HASEN + " " + tme)
                        else:
                            push(ids[key] + config.HASLE + " " + tme)
        count += 1
        print("vb")
        print(time.strftime("%H:%M:%S"))
        for key in vb:
            print(ids[key])
            print(vb[key])
        # print(vb)
        time.sleep(60)
