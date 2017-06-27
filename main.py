"""
Todo:
Fix args
Try/Catch
"""
import sys, pyowm, os

owm = pyowm.OWM('') #API Key from https://home.openweathermap.org/api_keys
observation = owm.weather_at_place(sys.argv[1]) #Get weather from CMD line arguments
w = observation.get_weather() #Get Weather
status = w.get_status()

if not os.path.exists('/etc/hostapd/hostapd.conf'): #if it doesn't exist
 os.system("cp hostapd.conf /etc/hostapd/hostapd.conf") #copy the blank file
file = open('/etc/hostapd/hostapd.conf', 'w') #Open file for writign

fileContentsHostAPD = ""

if not len(sys.argv) > 2: # If the args length isn't bigger than two, then set default interface to the wireless
 fileContentsHostAPD = """interface=wlan0
 driver=nl80211
 ssid="""+status+"""
 channel=6
 hw_mode=g
 macaddr_acl=0
 auth_algs=1
 ignore_broadcast_ssid=0
 wpa=2
 wpa_passphrase=12345678
 wpa_key_mgmt=WPA-PSK
 wpa_pairwise=TKIP
 rsn_pairwise=CCMP
 """
else: #Else set it to the arguement
 fileContentsHostAPD = """interface="""+sys.argv[2]+""" 
 driver=nl80211
 ssid="""+status+"""
 channel=6
 hw_mode=g
 macaddr_acl=0
 auth_algs=1
 ignore_broadcast_ssid=0
 wpa=2
 wpa_passphrase=12345678
 wpa_key_mgmt=WPA-PSK
 wpa_pairwise=TKIP
 rsn_pairwise=CCMP
 """

file.write(fileContentsHostAPD) #Write the info 
file.close() #Save it, then close.
os.system("killall hostapd") #Kill hostapd - Useful for restarting when using auto-update script
os.system("hostapd -B /etc/hostapd/hostapd.conf") #Run hostapd in the background with that config file
print('---------------------------------------------') #Just for formatting
os.system("iwconfig") #Just make sure everything is A-OK :)
