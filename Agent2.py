from task_02 import Task
from environment_02 import Env
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q
from pybrain.rl.experiments import Experiment
from pybrain.rl.explorers import EpsilonGreedyExplorer

import pylab
import numpy as np

#Rasberry Pi imports
import RPi.GPIO as GPIO
import time
from time import sleep

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

#exhibition sensors

PIR = 17

ECHO = 24
TRIG = 23
#
def ultrasonic (ECHO, TRIG):
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.output(TRIG, 0)

    GPIO.setup(ECHO, GPIO.IN)

    time.sleep(0.1)

    print ("messuring ultrasound...")
    GPIO.output(TRIG, 1)
    time.sleep(0.1)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass
    start = time.time()

    while GPIO.input(ECHO) == 1:
        pass
    stop = time.time()

    DISTANCE = (stop - start) * 17000
    
    print (DISTANCE)

#    DISTANCE = 100
    
    if DISTANCE >= 20:
       return 1 
#        print("sensor 1")
    elif DISTANCE < 20:
        return 0
#        print ("sensor 0")
    else :
        print ("x")



def PIR_sensing (PIR):
    
    GPIO.setup(PIR, GPIO.IN)
    current_state = 0

    time.sleep(0.1)
    current_state = GPIO.input(PIR)
    
    if current_state == 1:
       return 1 
#        print("sensor 1")
    elif current_state == 0:
        return 0
#        print ("sensor 0")
    else :
        print ("x")


# define action-value table:
# number of environment states:
# 165 states agent can be in the environment - comfortable / uncomfortable
#
# number of actions:
# 3 the number of action values the environment accepts -  Foreward, Backward and Snooze

states = 165 #Has to match class Env(Environment) - outdim  in environment_01.py
actions = 2 #Has to match class Env(Environment) - indim  in environment_01.py

try:
    arr = np.loadtxt('/home/pi/Desktop/ray_bot/ray_bot2.csv', delimiter=';')
    # open action value table  from .csv file
except Exception as e:
#    print e
    arr = np.zeros((states, actions))
    # except if the file does not exist - ie. first time - then creat and initialize it with numpy of zeros

av_table = ActionValueTable(states, actions)
av_table.initialize(arr.flatten())

# define Q-learning agent
learner = Q(0.1, 0.5)
learner._setExplorer(EpsilonGreedyExplorer(0.5))
agent = LearningAgent(av_table, learner)

# define the environment
env = Env()

# define the task
task = Task(env)

# define experiment
experiment = Experiment(task, agent)

# ready to go, start the process
#while PIR_sensing(PIR)==1 and ultrasonic (ECHO, TRIG)==1:

while True:
    if PIR_sensing(PIR)==1 and ultrasonic(ECHO, TRIG)==1 :
        experiment.doInteractions(3)
        
#        print ("distance: ")
#        print(ultrasonic (ECHO, TRIG))
        
        '''After n-number (here 3) steps, we call the agent’s learn() method and then reset it.
        This will make the agent forget the previously executed steps but of course it won’t undo the changes it learned.'''
    
        agent.learn()
        agent.reset()

        export_arr = av_table.getActionValues(np.arange(states))
        export_arr = export_arr.reshape((states, actions))

        np.savetxt("/home/pi/Desktop/ray_bot/ray_bot2.csv", export_arr, fmt='%.3f', delimiter=';')
        # save action value table to .csv file
    elif PIR_sensing(PIR)==0 and ultrasonic(ECHO, TRIG)==1:
        
        print("Waiting for humans")
        
    elif PIR_sensing(PIR)==1 and ultrasonic(ECHO, TRIG)==0:
        Rotation()
        print("edge alarm")
# Clean-up actions   
try:
    pass
    
except KeyboardInterrupt:
    pass
    
finally:
    GPIO.cleanup()
    