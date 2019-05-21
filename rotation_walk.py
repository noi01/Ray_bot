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

def Rotation():
#    position A
    kit.servo[0].angle = 90
    kit.servo[8].angle = 90
    sleep(0.2)    
    kit.servo[1].angle = 90
    kit.servo[9].angle = 90
    sleep(0.2)
    kit.servo[2].angle = 90
    kit.servo[10].angle = 90
    sleep(0.2)
    kit.servo[3].angle = 90
    kit.servo[11].angle = 90
    sleep(0.2)
    
#   rotate
    kit.servo[0].angle = 125
    kit.servo[1].angle = 125
    kit.servo[2].angle = 125
    kit.servo[3].angle = 125
    sleep(0.2)


#   steps align
    kit.servo[8].angle = 70
    kit.servo[0].angle = 90
    sleep(0.1)
    kit.servo[8].angle = 90
    sleep(0.2)
    
    kit.servo[10].angle = 110
    kit.servo[2].angle = 90
    sleep(0.1)
    kit.servo[10].angle = 90
    sleep(0.2)
    
    kit.servo[9].angle = 110
    kit.servo[1].angle = 90
    sleep(0.1)
    kit.servo[9].angle = 90
    sleep(0.2)
    
    kit.servo[11].angle = 70
    kit.servo[3].angle = 90
    sleep(0.1)
    kit.servo[11].angle = 90
    sleep(0.2)

def Forward():
#    position A
    kit.servo[0].angle = 110
    kit.servo[8].angle = 90
    sleep(0.1)    
    kit.servo[1].angle = 100
    kit.servo[9].angle = 90
    sleep(0.2)
    kit.servo[2].angle = 80
    kit.servo[10].angle = 90
    sleep(0.2)
    kit.servo[3].angle = 70
    kit.servo[11].angle = 90
    sleep(0.2)
    
#    step front left leg
    kit.servo[9].angle = 70
    kit.servo[1].angle = 60

    sleep(0.2)
    kit.servo[9].angle = 90


    
#   position B
    kit.servo[0].angle = 80
    sleep(0.2)    
    kit.servo[1].angle = 70
    sleep(0.2)
    kit.servo[2].angle = 110
    sleep(0.2)
    kit.servo[3].angle = 60
    sleep(0.2)
    
#   step 2
    kit.servo[11].angle = 110
    kit.servo[3].angle = 100

    sleep(0.2)
    kit.servo[11].angle = 90

#   step 3
    kit.servo[8].angle = 110
    kit.servo[0].angle = 120

    sleep(0.2)
    kit.servo[8].angle = 90

#   position C
    kit.servo[0].angle = 110
    kit.servo[8].angle = 90
    sleep(0.2)    
    kit.servo[1].angle = 100
    kit.servo[9].angle = 90
    sleep(0.2)
    kit.servo[2].angle = 120
    kit.servo[10].angle = 90
    sleep(0.2)
    kit.servo[3].angle = 70
    kit.servo[11].angle = 90
    sleep(0.2)
    
    #   step 4
    kit.servo[10].angle = 70
    kit.servo[2].angle = 80

    sleep(0.2)
    kit.servo[10].angle = 90

def Transition_A():
    kit.servo[8].angle = 60   
    kit.servo[0].angle = 90
    sleep(0.1)
    kit.servo[8].angle = 90
    sleep(0.2)
    
    kit.servo[9].angle = 120
    kit.servo[1].angle = 90
    sleep(0.1)
    kit.servo[9].angle = 90
    sleep(0.2)
    
    kit.servo[10].angle = 120
    kit.servo[2].angle = 90
    sleep(0.1)
    kit.servo[10].angle = 90
    sleep(0.2)
    
    kit.servo[11].angle = 60
    kit.servo[3].angle = 90
    sleep(0.1)
    kit.servo[11].angle = 90
    sleep(0.2)

def Transition_B():
    kit.servo[8].angle = 130   
    kit.servo[0].angle = 110
    sleep(0.1)
    kit.servo[8].angle = 90
    sleep(0.2)
    
    kit.servo[9].angle = 120
    kit.servo[1].angle = 120
    sleep(0.1)
    kit.servo[9].angle = 90
    sleep(0.2)
    
    kit.servo[10].angle = 120
    kit.servo[2].angle = 80
    sleep(0.1)
    kit.servo[10].angle = 90
    sleep(0.2)
    
    kit.servo[11].angle = 60
    kit.servo[3].angle = 70
    sleep(0.1)
    kit.servo[11].angle = 90
    sleep(0.2)


for x in range(10):
#    Rotation()
#    Transition_B()
    Forward()
# 
    print ("cycle")
    input("Press enter to continue")
