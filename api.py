import requests
import time
import RPi.GPIO as R
R.setmode(R.BOARD)
l=[3,5,7,11]
for i in range(len(l)):
    R.setup(l[i],R.OUT)

a=(input("enter value 1"))
b=(input("enter value 2"))
c=(input("enter value 3"))
d=(input("enter value 4"))
api="https://api.thingspeak.com/update?api_key=MYWA5HXNS0EQKFGH"
api1=api+'&field1='+a+'&field2='+b+'&field3='+c+'&field4='+d
requests.post(api1)
print("h1")
time.sleep(10)
g=requests.get("https://api.thingspeak.com/channels/788892/feeds.json?api_key=GHR411ZWGJMXGHUW&results=1")
h=g.json()
s1=h['feeds'][0]['field1']
s2=h['feeds'][0]['field2']
s3=h['feeds'][0]['field3']
s4=h['feeds'][0]['field4']
if(int(s1)==1):
    R.output(3,1)
    print("fe")
if(int(s2)==1):
    R.output(5,1)
    print("fe")
if(int(s3)==0):
    R.output(7,0)
    print("fe")
if(int(s4)==0):
    R.output(11,0)
    print("fe")
    
print(s1,s2,s3,s4)
R.output(5,0)
R.output(3,0)
"""R.output(3,1)
time.sleep(1)
R.output(3,0)"""

    

