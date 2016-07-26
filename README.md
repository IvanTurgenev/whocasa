
# whocasa

UPDATE: Someone has found a better way to detect iphones but my coding skills suck to translate this C# code to python. [HERE](http://www.power-home.com/forum/forum_posts.asp?TID=3250)

UPDATE: Thought on doing also some `tcpdump` to check if a device is sending stuff like discovery services etc. So it aways listens.

REQUIREMENTS: nmap, python3.

Send notifications who leaves or enters home by cellphones, laptops etc

Nice on mini linux boards

1) Register in http://www.pushetta.com.

2) Create a channel in pushetta and grab your api key from the dashboard.

3) Paste the api key and channel name in the `config.py` file.

4) Do `sudo pip3 install pushetta`

5) Install pusheta in your phone

6) Subscribe to your channel in the app

7) Use `nmap` or Fing (android app) to determine the MAC adresses of the devices you wanna keep track.

8) Add those MAC adresses to `ids.csv` file with the format `MACADDRESS,NAMEDEVICE`

9) Script must run as root, or `sudo`.(i think `nmap` requires this)

10) To start at boot add this line `python3 /home/pi/ph/ph.py &` to `/etc/rc.local` in the line before exit 0.



