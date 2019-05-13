from task_01 import Task
from environment_01 import Env
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

GPIO.setmode(GPIO.BCM)

#exhibition sensors

PIR = 17

#ECHO = 24
#TRIG = 23
#
#def ultrasonic (ECHO, TRIG):
#    GPIO.setup(TRIG, GPIO.OUT)
#    GPIO.output(TRIG, 0)
#
#    GPIO.setup(ECHO, GPIO.IN)
#
#    time.sleep(0.1)
#
#    print ("messuring ultrasound...")
#    GPIO.output(TRIG, 1)
#    time.sleep(0.1)
#    GPIO.output(TRIG, 0)
#
#    while GPIO.input(ECHO) == 0:
#        pass
#    start = time.time()
#
#    while GPIO.input(ECHO) == 1:
#        pass
#    stop = time.time()
#
#    DISTANCE = (stop - start) * 17000
#
#    print ("DISTANCE")
#    return DISTANCE

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
# 1024 states agent can be in the environment - comfortable / uncomfortable
#
# number of actions:
# 3 the number of action values the environment accepts -  Foreward, Backward and Snooze

states = 165 #Has to match class Env(Environment) - outdim  in environment_01.py
actions = 2 #Has to match class Env(Environment) - indim  in environment_01.py

try:
    arr = np.loadtxt('/home/pi/Desktop/ray_bot/ray_bot.csv', delimiter=';')
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
    if PIR_sensing(PIR)==1:
        experiment.doInteractions(12)
    
        '''After n-number (here 12) steps, we call the agent’s learn() method and then reset it.
        This will make the agent forget the previously executed steps but of course it won’t undo the changes it learned.'''
    
        agent.learn()
        agent.reset()

        export_arr = av_table.getActionValues(np.arange(states))
        export_arr = export_arr.reshape((states, actions))

        np.savetxt("/home/pi/Desktop/ray_bot/ray_bot.csv", export_arr, fmt='%.3f', delimiter=';')
        # save action value table to .csv file
    elif PIR_sensing(PIR)==0:
        
        print("Waiting for humans")
# Clean-up actions   
try:
    pass
    
except KeyboardInterrupt:
    pass
    
finally:
    GPIO.cleanup()
    