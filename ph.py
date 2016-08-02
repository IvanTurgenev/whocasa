
import os
import subprocess
import csv
import sys
import time
import config
from pushetta import Pushetta


ipr = config.ipr
nmap = "nmap -sn " + ipr + " | awk '/Address:/ {print $3}' "


def nmac():
    try:
        x = subprocess.check_output(
            nmap,
            shell=True).decode(sys.stdout.encoding).split("\n")
    # print("NMAC X POP")
    # print(x.pop())
    except subprocess.CalledProcessError as e:
        cfl(fln, [str(e.output), "retrying in 60 seconds"])
        # print(e.output)
        # print("retrying in 60 seconds")
        time.sleep(60)
        x = nmac()
    # x.pop()
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
            cfl(fln, [ids[key] + config.HASEN + " " + tme])
            arlnotx.append(key)
    return(arlnotx)


def tmee():
    return(time.strftime("%H:%M:%S"))


def nlog():
    fln = time.strftime("%d %m %Y")
    if os.path.isfile(fln):
        count = 1
        while True:
            if os.path.isfile(fln + " #" + str(count)) is False:
                return(fln + " #" + str(count))
            else:
                count += 1
    else:
        return(fln)


def cfl(fln, ln):
    with open(fln, 'a') as f:
        f.write("\n".join(ln))
        print("\n".join(ln))


def lstvb(idsx, vbx):
    lst = []
    for key in vbx:
        lst.append(str(idsx[key]))
        lst.append(str(vbx[key]))
    return(lst)


if __name__ == '__main__':

    fln = nlog()
    (kid, ids) = opcsv("ids.csv")
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
                cfl(fln, ["vb1", tmee(), "#cicle " + str(count)] + vbl1)
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
                            cfl(fln, ntf)
                        # print(ids[key] + config.HASEN + " NOT NOF"+tme)
                        # push(ids[key] + config.HASEN + " " + tme)
        vbl = lstvb(ids, vb)
        cfl(fln, ["vb", tmee(), "#cicle " + str(count)] + vbl)
        count += 1
        # print("vb")
        # print(time.strftime("%H:%M:%S"))
        time.sleep(60)
