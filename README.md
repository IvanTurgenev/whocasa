# whocasa

UPDATE: Found a better way to detect iphones but my coding skills suck to translate this C# code to python. http://www.power-home.com/forum/forum_posts.asp?TID=3250

Send notifications who leaves or enters home by cellphones, laptops etc

nice on mini linux boards

1) register in http://www.pushetta.com

2) create a channel in pushetta and grab your api key from the dashboard

3) paste the api key and channel name in the config.py

4) do pip3 install pushetta

5) install pusheta in your phone

6) suscribe to your channel in the app

7) use nmap or Fing(android app) to determine the MAC adresses of the devices you wanna keep track

8) add those MAC adresses to ids.csv MACADDRESS,NAMEDEVICE

9) script at start up add to /etc/rc.local the line before exit 0. python3 /home/pi/ph/ph.py &

