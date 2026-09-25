from world import WORLD
from robot import ROBOT

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self): #class constructor
        pass
        
        #Set up
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        
        #self.robot2Id = p.loadURDF("body_2.urdf")     #robotId = p.loadURDF("body.urdf")
        #pyrosim.Prepare_To_Simulate(self.robot2Id)

        self.world = WORLD()
        self.robot = ROBOT()
        
