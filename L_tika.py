#!/usr/bin/env python
import roslib
import rospy
import time
import wiringpi
import subprocess

#main
if __name__ == '__main__':
    ### init io port ###
    subprocess.check_call('gpio export 11 out',shell=True)
    subprocess.check_call('gpio export 8 out',shell=True)
    ###
    rospy.init_node('ledflash')

    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
    io.pinMode(11,io.OUTPUT)  # Setup pin 11
    io.pinMode(8,io.OUTPUT)  # Setup pin 8 

    while not rospy.is_shutdown():
        io.digitalWrite(11,1)
        io.digitalWrite(8,0)
        time.sleep(1)
        io.digitalWrite(11,0)
        io.digitalWrite(8,1)
        time.sleep(1)

    print('\rStopped')
