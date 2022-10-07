import requests
import time
import RPi.GPIO as R
R.setmode(R.BOARD)
l=[3,5,7,11]
#l1=3
#l2=5
#l3=7
#l4=11
for i in range(len(l)):
    R.setup(l[i],R.OUT)

a=(input("enter value 1"))
api="https://api.thingspeak.com/update?api_key=MYWA5HXNS0EQKFGH"
api1=api+'&field1='+a
requests.post(api1)
print("h1")
time.sleep(10)
g=requests.get("https://api.thingspeak.com/channels/788892/feeds.json?api_key=GHR411ZWGJMXGHUW&results=1")
h=g.json()
s1=h['feeds'][0]['field1']
print(s1)
R.output(3,0)
R.output(5,0)
R.output(7,0)
R.output(11,0)
if(int(s1)==1):
    R.output(3,1)
    R.output(5,0)
    R.output(7,1)
    R.output(11,0)
    print("case1")
if(int(s1)==2):
    R.output(3,0)
    R.output(5,0)
    R.output(7,1)
    R.output(11,0)
    print("case2")
if(int(s1)==3):
    R.output(3,1)
    R.output(5,0)
    R.output(7,0)
    R.output(11,0)
    print("case3")
if(int(s1)==4):
    R.output(3,0)
    R.output(5,1)
    R.output(7,0)
    R.output(11,1)
    print("case4")
if(int(s1)==5):
    R.output(3,0)
    R.output(5,0)
    R.output(7,0)
    R.output(11,0)
    print("case5")
