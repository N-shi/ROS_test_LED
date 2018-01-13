#!/usr/bin/env python
import rospy
import time
import wiringpi as w 

w.wiringPiSetup()
w.pinMode(0,1)
while 1:
  w.digitalWrite(0,1)
  time.sleep(1)
  w.digitalWrite(0,0)
  time.sleep(1)
