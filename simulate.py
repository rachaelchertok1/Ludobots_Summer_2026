from simulation import SIMULATION

simulation = SIMULATION() #Creates an instance of the SIMULATION class called simulation
'''
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import constants as c
'''
'''


backLegSensorValues = numpy.zeros(c.NUM_ITERS)
frontLegSensorValues = numpy.zeros(c.NUM_ITERS)


targetAngles_backLeg = numpy.empty(c.NUM_ITERS)
for i in range(0, c.NUM_ITERS):
    targetAngles_backLeg[i] = c.AMPLITUDE_BACKLEG * numpy.sin( 2 * numpy.pi * c.FREQUENCY_BACKLEG * i /c.NUM_ITERS + c.PHASEOFFSET_BACKLEG)

#numpy.save("data/targetAngles_backLeg", targetAngles_backLeg)

targetAngles_frontLeg = numpy.empty(c.NUM_ITERS)
for i in range(0, c.NUM_ITERS):
    targetAngles_frontLeg[i] = c.AMPLITUDE_FRONTLEG * numpy.sin( 2 * numpy.pi * c.FREQUENCY_FRONTLEG * i /c.NUM_ITERS + c.PHASEOFFSET_FRONTLEG)
#numpy.save("data/targetAngles_frontLeg", targetAngles_frontLeg)  
#exit()

#Keep sim running
for i in range(0,c.NUM_ITERS):
    time.sleep(1/240)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot2Id,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_backLeg[i], 
        maxForce = 500
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot2Id,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_frontLeg[i], 
        maxForce = 500
    )


numpy.save("data/backLegSensorVals", backLegSensorValues)
numpy.save("data/frontLegSensorVals", frontLegSensorValues)

p.disconnect()
'''