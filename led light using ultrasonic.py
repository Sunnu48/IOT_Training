import RPi.GPIO as R
import time
R.setmode(R.BOARD)
R.setup(3,R.IN)
R.setup(5,R.OUT)
R.setup(7,R.OUT)
#trig=7
#echo =3
while(1):
    R.output(7,1)
    time.sleep(0.00001)
    R.output(7,0)
    while(R.input(3)==0):
        pass
    t1=time.time()
    while(R.input(3)==1):
        pass
    t2=time.time()
    t3=t2-t1
    d=(34100*t3)/2
    print(d)
    time.sleep(1)
    if(d<100):
        R.output(5,1)
        time.sleep(1)
    if(d>100):
        R.output(5,0)
        time.sleep(1)
