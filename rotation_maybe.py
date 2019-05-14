from pybrain.rl.environments.environment import Environment
from scipy import zeros
import random

#Rasberry Pi imports
import RPi.GPIO as GPIO
import time
from time import sleep

#SETUP OUTPUT

GPIO.setmode(GPIO.BCM)

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def Forward():
#    position A
    kit.servo[0].angle = 90
    kit.servo[12].angle = 90
    sleep(0.2)    
    kit.servo[1].angle = 90
    kit.servo[13].angle = 90
    sleep(0.2)
    kit.servo[2].angle = 90
    kit.servo[15].angle = 90
    sleep(0.2)
    kit.servo[3].angle = 90
    kit.servo[14].angle = 90
    sleep(0.2)
    
#   rotate
    kit.servo[0].angle = 120
    kit.servo[1].angle = 120
    kit.servo[2].angle = 120
    kit.servo[3].angle = 120
    sleep(0.2)


#   steps align
    kit.servo[12].angle = 80
    kit.servo[0].angle = 90
    kit.servo[12].angle = 90
    sleep(0.2)

    kit.servo[13].angle = 100
    kit.servo[1].angle = 90
    kit.servo[13].angle = 90
    sleep(0.2)
	
    kit.servo[15].angle = 100
    kit.servo[2].angle = 90
    kit.servo[15].angle = 90
    sleep(0.2)
	
    kit.servo[14].angle = 80
    kit.servo[3].angle = 90
    kit.servo[14].angle = 90
    sleep(0.2)
