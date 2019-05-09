import requests
import os
import sys
import Adafruit_DHT


dweetIO = "https://dweet.io/dweet/for/"
myName = "Grupo7"
myKey1 = "temp"
myKey2 = "temperature"
myKey3 = "humidity"

tempC = []

for i in range(0,26):
    tempC.append(0)
    
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    
    ostemp = os.popen('vcgencmd measure_temp').readline()
    temp = (ostemp.replace("temp=", "").replace("'C\n", ""))
 #   print(temp)
    tempC.append(temp)
    tempC.pop(0)

    #Send to Cloud, dweet.io
    rqsString1 = dweetIO+myName+'?'+myKey1+'='+str(temp)
    rqsString2 = dweetIO+myName+'?'+myKey2+'='+str(temperature)
    rqsString3 = dweetIO+myName+'?'+myKey3+'='+str(humidity)
#    rqsString = dweetIO+myName+'?'+myKey+'='+str(temp)+'&'+myLink
    print(rqsString1)
    rqs1 = requests.get(rqsString1)
    
    print(rqsString2)
    rqs2 = requests.get(rqsString2)
    
    print(rqsString3)
    rqs3 = requests.get(rqsString3)
#    print (rqs.status_code)
#    print (rqs.headers)
#    print (rqs.content)
    
#    plt.pause(.5)
