#!/usr/bin/env python
import rospy
import time
import pigpio

pi = pigpio.pi()
pi.set_mode(25, pigpio.OUTPUT)
while 1:
  pi.write(25,1)
  time.sleep(1)
  pi.write(25,0)
  time.sleep(1)
