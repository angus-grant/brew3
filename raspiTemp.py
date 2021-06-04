#!/usr/bin/python
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.OUT)

tFile = open('/sys/class/thermal/thermal_zone0/temp')
temp = float(tFile.read())
tempC = temp/1000
tempStatus = round(tempC, 1)
#print tempC

if tempC > 43.5:
#  GPIO.output(17, 1)
  tempStatus = str(tempStatus) + "-HOT"
else:
#  GPIO.output(17, 0)
  tempStatus = str(tempStatus) + "-COLD"

print tempStatus
