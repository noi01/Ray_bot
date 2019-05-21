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

def Snooze():
    print("Snooze")

#SETUP INPUT

#define the sensor pins that goes to the circuit

import Adafruit_DHT


class Env(Environment):
    """ Environment for RL our agent will be able to observe"""       

    # the number of action values the environment accepts - Foreward, Backward and Snooze
    indim = 2
    
    # the number of sensor values the environment produces - analog in photoresistor_sensor
    outdim = 165
    
    
    
    def getSensors(self):
        """ the currently visible state of the world (the observation may be stochastic - repeated calls returning different values) 
            :rtype: by default, this is assumed to be a numpy array of doubles
        """
#        obj_temp = sensor_temp.readObjTempC()
#        die_temp = sensor_temp.readDieTempC()
#        
#        temp_diff = ((obj_temp+40) - (die_temp+40))*10
#        temp_observation = round(temp_diff, 0)
#        print('Object temperature diff: {0:0.3F}*C'.format(temp_observation))
#        sleep(3)
        sensor=Adafruit_DHT.DHT11
        gpio=27
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
#        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        sensor_value = temperature #sensor messurment
        temp_observation = sensor_value
#        print (temp_observation)
# return needs to be formated in such way to be digestable by Pybrain library, I think... otherwise there are errors
        return [float(temp_observation),]
        
                    
    def performAction(self, action):
        """ perform an action on the world that changes it's internal state (maybe stochastically).
            :key action: an action that should be executed in the Environment. 
            :type action: by default, this is assumed to be a numpy array of doubles
        """
        print ("Action performed: ", action)
        if  action == 1:
            print ("ENV_PerformAction:Walk")
            Forward()
            time.sleep(1)

        elif action == 0:
            Snooze()
            print ("ENV_PerformAction:Snooze")
            time.sleep(1)
            

        

    def reset(self):
        """ Most environments will implement this optional method that allows for reinitialization. 
        """
