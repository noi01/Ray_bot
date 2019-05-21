from scipy import clip, asarray

from pybrain.rl.environments.task import Task
from numpy import *

#Rasberry Pi imports
import RPi.GPIO as GPIO
import time

#Sensors that are used as part of task assesment
GPIO.setmode(GPIO.BCM)

class Task(Task):
    """ A task is associating a purpose with an environment. It decides how to evaluate the observations, potentially returning reinforcement rewards or fitness values. 
    Furthermore it is a filter for what should be visible to the agent.
    Also, it can potentially act as a filter on how actions are transmitted to the environment. """

    def __init__(self, environment):
        """ All tasks are coupled to an environment. """
        self.env = environment
        self.lastreward = 0
        # keep last reward. Q lerning reward is given for the interaction before current interaction!

    def performAction(self, action):
        """ A filtered mapping towards performAction of the underlying environment. """                
        self.env.performAction(action)
        
    def getObservation(self):
        """ A filtered mapping to getSample of the underlying environment. """
        sensors = self.env.getSensors()
        return sensors
    
    def getReward(self):
        """ Compute and return the current reward (i.e. corresponding to the last action performed) """
        sensors = self.env.getSensors()#input from environment_01.py

        reward = 0
        f = 0 #will chang to true (1) to when if statement is fullfilled, otherwise false
        
        print ("Sensor read: ", sensors)

        
        if any(x>=10 for x in sensors):
#           if sensors >= 500 : #works in python2
            reward = 1
            f = 1

            
        elif any(x<10 for x in sensors):
            reward = 0
            f = 0  
  
        
        # retrieve last reward - save current received reward
        cur_reward = self.lastreward
        self.lastreward = reward
        
        print ("Reward: ", cur_reward)
    
        return cur_reward
        
        

    @property
    def indim(self):
        return self.env.indim
    
    @property
    def outdim(self):
        return self.env.outdim
