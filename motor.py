import numpy
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim
class MOTOR:
    def __init__(self, jointName): #class constructor
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.NUM_ITERS)

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.AMPLITUDE_FRONTLEG
        self.frequency = c.FREQUENCY_FRONTLEG
        self.offset = c.PHASEOFFSET_FRONTLEG

        for i in range(0, c.NUM_ITERS):
            if self.jointName == b'Torso_FrontLeg':
                self.motorValues[i] = self.amplitude * numpy.sin( 2 * numpy.pi * (self.frequency/2) * i /c.NUM_ITERS + self.offset)
            else:      
                self.motorValues[i] = self.amplitude * numpy.sin( 2 * numpy.pi * self.frequency * i /c.NUM_ITERS + self.offset)
    
    
    def Set_Value(self, robot, timestep):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[timestep],
            maxForce = 500
        )

    def Save_Values(self):
        numpy.save("data/motorValues", self.motorValues)

