import RPi.GPIO as R
import time
R.setmode(R.BOARD)
##R.setup(3,R.OUT)
l=[3,5]
for i in range(len(l)):
    R.setup(l[i],R.OUT)
for i in range(len(l)):
    R.output(l[i],1)
    time.sleep(1)
for i in range(len(l)):
    R.output(l[i],0)
    
    

 
