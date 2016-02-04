# whocasa
Send notifications who leaves or enters home

1) register in http://www.pushetta.com

2) create a channel in pushetta and grab you api key

3) paste the in the script your api key and channel name

4) do pip3 install pushetta

5) install pusheta in your phone

6) suscribe to your channel in the app

7) use nmap or Fing(android app) to determine the MAC adresses of the devices you wanna keep track and inform

8) add those MAC adresses to ids.csv MACADDRESS,NAMEDEVICE

9) script at start up add to /etc/rc.local the line before exit 0. python3 /home/pi/ph/ph.py &

