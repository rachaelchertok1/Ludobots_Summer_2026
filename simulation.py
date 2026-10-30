from world import WORLD
from robot import ROBOT

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time

class SIMULATION:
    def __init__(self): #class constructor
        #Set up
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        #Keep sim running
        for timestep in range(0,c.NUM_ITERS):
            time.sleep(1/240)
            p.stepSimulation() #updates the simulated world

            #The robot then senses some (but perhaps not all) of the changes that have occurred
            self.robot.Sense(timestep)
            #Robot then acts on that world
            self.robot.Act(timestep)

    def __del__(self):
        p.disconnect()