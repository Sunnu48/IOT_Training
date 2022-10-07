import RPi.GPIO as R
import time
R.setmode(R.BOARD)
R.setup(3,R.OUT)

R.output(3,1)
time.sleep(1)
R.output(3,0)

