import RPi.GPIO as R
import time
R.setmode(R.BOARD)
R.setwarning(False)
l=[7,8,10,11]
RS=3
EN=5
cmd=0
pin=0
data=0
for i in range(len(l)):
    R.setup(l[i],R.OUT)
    R.setup(RS,R.OUT)
    R.setup(EN,R.OUT)

def port(pin):
    i=0x10
    for j in range(len(l)):
        if((pin&i)==i):
            R.output(l[j],1)
        else:
            R.output(l[j],0)
    i=i*2

def LCD_CMD(cmd):
    print(cmd)
    cmd1=(cmd & 0xF0)
    port(cmd1)
    R.output(RS,0)
    R.output(EN,1)
    time.sleep(0.01)
    R.output(EN,0)

    cmd1=((cmd<<4)&0XF0)
    port(cmd1)
    R.output(RS,0)
    R.output(EN,1)
    time.sleep(0.01)
    R.output(EN,0)

    
def LCD_data(data):
    print(data)
    data1=(data & 0XF0)
    port(data1)
    R.output(RS,1)
    R.output(EN,1)
    time.sleep(0.01)
    R.output(EN,0)

    data1=((data<<4)&0*F0)
    port(data1)
    R.output(RS,1)
    R.output(EN,1)
    time.sleep(1)
    R.output(EN,0)
def LCD_init():
    LCD_CMD(0x28)
    LCD_CMD(0x0C)
    LCD_CMD(0x06)
    LCD_CMD(0x02)
    LCD_CMD(0X01)

LCD_init()
time.sleep(1)
LCD_CMD(0x80)
LCD_data(0x41)
    
