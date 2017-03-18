
# whocasa

Send notifications who leaves or enters home by cellphones, laptops etc.

## Posible better ways or improvements.

1: Someone has found a better way to detect iphones but my coding skills suck to translate this C# code to python. [HERE](http://www.power-home.com/forum/forum_posts.asp?TID=3250)

2: Thought on doing also some `tcpdump` to check if a device is sending stuff like discovery services etc. So it aways listens.

3: Might be better if we had control over the router/modem, DD-WRT, relay all traffic to the host idk.

4: Use nmap api.

5: WIFI dongle usb monitor mode.

6: The volume of the pushetta notification is loud as fuck lol.

## Setup

REQUIREMENTS:`nmap`, `sudo`, python3.


1) Register in http://www.pushetta.com.

2) Create a channel in pushetta and grab your api key from the dashboard.

3) Paste the api key and channel name in the `configuser.py` file, also paste your ip range.

4) Do `sudo pip3 install pushetta.`

5) Install pusheta in your phone.

6) Subscribe to your channel in the app.

7) Use `nmap` or Fing (android app) to determine the MAC adresses of the devices you wanna keep track.

8) Add those MAC adresses to `idsuser.csv` file with the format `MACADDRESS,NAMEDEVICE`.

9) Script must run as root, or `sudo`.(i think `nmap` requires this for mac addresses).

10) To start at boot add this line `python3 /home/pi/ph/ph.py &` to `/etc/rc.local` in the line before exit 0, depending on you distribution.


## How it Works

Takes `idsuser.csv` creates a list of of booleans wherever a device is detected.

*pseudocode*

```
12:23:DE,[True ,False,True ]
23:EF:43,[False,False,False]
```

Then it creates another list, this list contains bools if the device has been seen at least once during the cycle.

```
12:23:DE,[True ,False,True ,.....] -> 12:23:DE,True
23:EF:43,[False,False,False,.....] -> 23:EF:43,False
```

Then it begins another cycle. For another 10~ itinerations, and appends another boolead True if the device has been seen at least once.

```
12:23:DE,[False,False,True,....] -> 12:23:DE,True
23:EF:43,[True ,True ,True,....] -> 23:EF:43,True
```

Then it compares the resulting lists from the last two cycles looking for change so.

```
False then False : device is not present dont send notification
True  then True  : device is present dont send notification
False then True  : device was not present, then is present so send notification is has arrived
True  then False : devces was present, then is not present so send notification is has left
```

Then it repeats using the last cycle as starting point.
