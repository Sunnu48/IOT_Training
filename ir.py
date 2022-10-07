import RPi.GPIO as R
import time
R.setmode(R.BOARD)
R.setup(3,R.IN)
R.setup(7,R.IN)
p=0
count=0
while(1):
    y=R.input(7)
    x=R.input(3)
    if(y==1):
        if(x==1 and p==0):
            print("yes")
            count=count+1
            print(count)
            p=1
    elif(x==1):
        if(y==1 and p==0):
            print("yes")
            count=count-1
            print(count)
            p=1
    elif(x==0 or y==0 and p==1):
        print("no")
        p=0
    else:
        continue
