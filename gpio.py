
import RPi.GPIO as GPIO
import os
import sys
from datetime import datetime

timeStart = datetime.now()
print timeStart

target_pin = int(sys.argv[1])
pin_state = int(sys.argv[2])
duty_cycle = float(sys.argv[3])/100.0

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(target_pin,GPIO.OUT)

# Turn on/off LED based on user input
if pin_state is 1:
    GPIO.output(target_pin,GPIO.HIGH)
    print("gpio activated")

    if duty_cycle < 2.0:
	secondsDiff = (datetime.now() - timeStart).total_seconds()

        while secondsDiff < duty_cycle:
            secondsDiff = (datetime.now() - timeStart).total_seconds()
#            sys.stdout.write(str(secondsDiff) + "\r\n")

        GPIO.output(target_pin,GPIO.LOW)
	print "gpio turned off"
elif pin_state is 0:
    GPIO.output(target_pin,GPIO.LOW)
    print("LED is off")

