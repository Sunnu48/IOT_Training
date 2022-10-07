import RPi.GPIO as r
import time as t
r.setmode(r.BOARD)
r.setwarnings(False)
li=[7,8,10,11]
RS=3
EN=5
a=len(li)
for i in range (0,a):
    r.setup(li[i],r.OUT)
r.setup(RS,r.OUT)
r.setup(EN,r.OUT)

for i in range (0,a):
    r.output(li[i],0)
r.output(RS,0)
r.output(EN,0)

def PORT(P):
    j=0x10
    for i in range (0,a):
        if((P & j)==j):
            r.output(li[i],1)
        else:
            r.output(li[i],0)
        j=j*2

def LCD_CMD(C):
    print(C)
    P=(C & 0xF0)
    PORT(P)
    r.output(RS,0)
    r.output(EN,1)
    t.sleep(0.01)
    r.output(EN,0)

    P=((C<<4) & 0xF0)
    PORT(P)
    r.output(RS,0)
    r.output(EN,1)
    t.sleep(0.01)
    r.output(EN,0)

    
def LCD_data(d):
    print(d)
    P=(d & 0xF0)
    PORT(P)
    r.output(RS,1)
    r.output(EN,1)
    t.sleep(0.01)
    r.output(EN,0)
    

    
    P=((d<<4) & 0xF0)
    PORT(P)
    r.output(RS,1)
    r.output(EN,1)
    t.sleep(0.01)
    r.output(EN,0)


def LCD_init():
    
    LCD_CMD(0x01)
    LCD_CMD(0x02)
    LCD_CMD(0x28)
    LCD_CMD(0x06)
    LCD_CMD(0x0c)

def LCD_strinng(s):
    g=''
    g=s
    for i in range(0,len(g)):
        LCD_data(ord(g[i]))
    
LCD_init()
t.sleep(2)
LCD_CMD(0x40)
LCD_CMD(0X04)
LCD_data(0x0E)
LCD_data(0x1F)
LCD_data(0x1F)
LCD_data(0x00)
LCD_data(0x02)
LCD_data(0x00)
LCD_data(0x00)

LCD_CMD(0x48)
LCD_CMD(0X04)
LCD_data(0x0E)
LCD_data(0x1F)
LCD_data(0x1F)
LCD_data(0x00)
LCD_data(0x02)
LCD_data(0x00)
LCD_data(0x00)

LCD_CMD(0x50)
LCD_CMD(0X04)
LCD_data(0x0E)
LCD_data(0x1F)
LCD_data(0x1F)
LCD_data(0x00)
LCD_data(0x02)
LCD_data(0x00)
LCD_data(0x00)

LCD_CMD(0x58)
LCD_CMD(0X04)
LCD_data(0x0E)
LCD_data(0x1F)
LCD_data(0x1F)
LCD_data(0x00)
LCD_data(0x02)
LCD_data(0x00)
LCD_data(0x00)

LCD_CMD(0x60)
LCD_CMD(0X04)
LCD_data(0x0E)
LCD_data(0x1F)
LCD_data(0x1F)
LCD_data(0x00)
LCD_data(0x02)
LCD_data(0x00)
LCD_data(0x00)
"""LCD_CMD(0x01)
    t.sleep(1)
    LCD_CMD(0x80)
    LCD_strinng('sunit')
    t.sleep(3)
    LCD_CMD(0x01)
    for i in range(10):
        LCD_CMD(0x86)
        LCD_strinng(str(i))
        t.sleep(3)
        LCD_CMD(0x01)
    LCD_CMD(0x86)
    LCD_strinng(str(i))
    LCD_data(i)
    LCD_CMD(0x88)
    t.sleep(1)
    LCD_CMD(0x01)
    i=i+1"""
lis=[0,1,2,1,0,3,4,3,1]
t.sleep(1)
LCD_CMD(0x01)
t.sleep(1)

while(1):
    for i in range(len(lis)):
        t.sleep(0.1)
        LCD_CMD(0x80)
        LCD_data(lis[i])
        t.sleep(2)
        print("ft")
    
    
    
    
        
    print('ft')
