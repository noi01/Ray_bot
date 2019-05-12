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
    kit.servo[0].angle = 110
    kit.servo[12].angle = 90
    sleep(0.2)    
    kit.servo[1].angle = 100
    kit.servo[13].angle = 90
    sleep(0.2)
    kit.servo[2].angle = 80
    kit.servo[15].angle = 90
    sleep(0.2)
    kit.servo[3].angle = 70
    kit.servo[14].angle = 90
    sleep(0.2)
    
#    step front left leg
    kit.servo[13].angle = 120
    kit.servo[1].angle = 60

    sleep(0.2)
    kit.servo[13].angle = 90


    
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
    kit.servo[14].angle = 60
    kit.servo[3].angle = 100

    sleep(0.2)
    kit.servo[14].angle = 90

#   step 3
    kit.servo[12].angle = 60
    kit.servo[0].angle = 120

    sleep(0.2)
    kit.servo[12].angle = 90

#   position C
    kit.servo[0].angle = 110
    kit.servo[12].angle = 90
    sleep(0.2)    
    kit.servo[1].angle = 100
    kit.servo[13].angle = 90
    sleep(0.2)
    kit.servo[2].angle = 120
    kit.servo[12].angle = 90
    sleep(0.2)
    kit.servo[3].angle = 70
    kit.servo[12].angle = 90
    sleep(0.2)
    
    #   step 4
    kit.servo[15].angle = 120
    kit.servo[2].angle = 80

    sleep(0.2)
    kit.servo[15].angle = 90    

def Snooze():
    print("Snooze")

#SETUP INPUT

#define the sensor pins that goes to the circuit

import Adafruit_TMP.TMP006 as TMP006

sensor_temp = TMP006.TMP006(address=0x41, busnum=1)
sensor_temp.begin()


class Env(Environment):
    """ Environment for RL our agent will be able to observe"""       

    # the number of action values the environment accepts - Foreward, Backward and Snooze
    indim = 2
    
    # the number of sensor values the environment produces - analog in photoresistor_sensor
    outdim = 1024
    
    
    
    def getSensors(self):
        """ the currently visible state of the world (the observation may be stochastic - repeated calls returning different values) 
            :rtype: by default, this is assumed to be a numpy array of doubles
        """
        obj_temp = sensor_temp.readObjTempC()
        die_temp = sensor_temp.readDieTempC()
        
        temp_diff = (obj_temp - die_temp)*10
        temp_observation = round(temp_diff, 0)
        print('Object temperature diff: {0:0.3F}*C'.format(temp_observation))
        sleep(0.2)
        sensor_value = temp_observation #sensor messurment
# return needs to be formated in such way to be digestable by Pybrain library, I think... otherwise there are errors
        return [float(temp_observation),]
        
                    
    def performAction(self, action):
        """ perform an action on the world that changes it's internal state (maybe stochastically).
            :key action: an action that should be executed in the Environment. 
            :type action: by default, this is assumed to be a numpy array of doubles
        """
        print ("Action performed: ", action)
        if  action == 1:
            print ("I Walk")
            Forward()
            time.sleep(1)

        elif action == 0:
            Snooze()
            time.sleep(1)
            

        

    def reset(self):
        """ Most environments will implement this optional method that allows for reinitialization. 
        """
