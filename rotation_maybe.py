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
    kit.servo[10].angle = 105
    kit.servo[8].angle = 90
    sleep(0.1)    
    kit.servo[11].angle = 120
    kit.servo[9].angle = 80
    sleep(0.2)
    kit.servo[2].angle = 60
    kit.servo[0].angle = 80
    sleep(0.2)
    kit.servo[3].angle = 75
    kit.servo[1].angle = 105
    sleep(0.2)
    
#    step front left leg
    kit.servo[8].angle = 130
    sleep(0.2)
    kit.servo[10].angle = 40

    sleep(0.2)
    kit.servo[8].angle = 90


    
#   moveA
    kit.servo[10].angle = 60
    sleep(0.2)    
    kit.servo[11].angle = 75
    sleep(0.2)
    kit.servo[2].angle = 40
    sleep(0.2)
    kit.servo[3].angle = 120
    sleep(0.2)
    
#   step 2
    kit.servo[0].angle = 50
    sleep(0.1)
    kit.servo[2].angle = 105
    sleep(0.2)
    kit.servo[0].angle = 95

#   step 3
    kit.servo[9].angle = 50
    sleep(0.1)
    kit.servo[11].angle = 140
    sleep(0.2)
    kit.servo[9].angle = 80

#   position C
    kit.servo[10].angle = 105
    kit.servo[8].angle = 90
    sleep(0.2)    
    kit.servo[11].angle = 120
    kit.servo[9].angle = 80
    sleep(0.2)
    kit.servo[2].angle = 60
    kit.servo[0].angle = 80
    sleep(0.2)
    kit.servo[3].angle = 140
    kit.servo[1].angle = 105
    sleep(0.2)
    
    #   step 4
    kit.servo[1].angle = 130
    sleep(0.1)
    kit.servo[3].angle = 75
    sleep(0.2)
    kit.servo[1].angle = 105

def Rotate():


    kit.servo[10].angle = 110
    sleep(0.1)
    kit.servo[11].angle = 110
    sleep(0.1)
    kit.servo[2].angle = 110
    sleep(0.1)
    kit.servo[3].angle = 110
    sleep(0.1)
    
    kit.servo[8].angle = 130
    sleep(0.1)
    kit.servo[10].angle = 90
    sleep(0.2)
    kit.servo[8].angle = 90

    kit.servo[9].angle = 50
    sleep(0.1)
    kit.servo[11].angle = 90
    sleep(0.2)
    kit.servo[9].angle = 80

    kit.servo[0].angle = 50
    sleep(0.1)
    kit.servo[2].angle = 90
    sleep(0.2)
    kit.servo[0].angle = 80

    
    kit.servo[1].angle = 130
    sleep(0.5)
    kit.servo[3].angle = 90
    sleep(0.2)
    kit.servo[1].angle = 105
    
    sleep(0.2)


#for x in range(10):
while True:     
    Forward()
#    Rotate()
#    Rotate()
#    Rotate()


#    input("Press enter to continue")    




















