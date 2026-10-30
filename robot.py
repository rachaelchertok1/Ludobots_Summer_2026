import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
class ROBOT:
    def __init__(self): #class constructor
        self.robot2Id = p.loadURDF("body_2.urdf")     #robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot2Id)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()


    def Prepare_To_Sense(self):
        #Creating empty sensor dictionary
        self.sensors = {}
        
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    
    def Sense(self, timestep):
        for sensor in self.sensors.values(): #self.sensors is a dictionary, so we need the value to give us the sensor val at the key (e.g. BackLeg)
            sensor.Get_Value(timestep) #Stores the current value of the touch sensor in self.vavlues

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            print(jointName)
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, timestep):
        for motor in self.motors.values(): #self.sensors is a dictionary, so we need the value to give us the sensor val at the key (e.g. BackLeg)
            motor.Set_Value(self.robot2Id, timestep) #Stores the current value of the touch sensor in self.vavlues