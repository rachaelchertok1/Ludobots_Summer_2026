import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

num_iters = 1000

amplitude_backLeg = numpy.pi/4
frequency_backLeg = 40
phaseOffset_backLeg = 0

amplitude_frontLeg = numpy.pi/4
frequency_frontLeg = 40
phaseOffset_frontLeg = 0

#Set up
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
robot2Id = p.loadURDF("body_2.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robot2Id)
backLegSensorValues = numpy.zeros(num_iters)
frontLegSensorValues = numpy.zeros(num_iters)

'''
#Create an empty array to add the degree vals into
vals = numpy.empty(num_iters)
step = 360/num_iters
for i in range(0, num_iters):
    vals[i] = i * step

#Create array of sin of each degree value computed above, do conversion to radians before putting into sin func
targetAngles = (numpy.pi / 4) * numpy.sin(vals * numpy.pi/180)
#numpy.save("data/targetAngles", targetAngles)
'''

targetAngles_backLeg = numpy.empty(num_iters)
for i in range(0, num_iters):
    targetAngles_backLeg[i] = amplitude_backLeg * numpy.sin( 2 * numpy.pi * frequency_backLeg * i /num_iters + phaseOffset_backLeg)

#numpy.save("data/targetAngles_backLeg", targetAngles_backLeg)

targetAngles_frontLeg = numpy.empty(num_iters)
for i in range(0, num_iters):
    targetAngles_frontLeg[i] = amplitude_frontLeg * numpy.sin( 2 * numpy.pi * frequency_frontLeg * i /num_iters + phaseOffset_frontLeg)
#numpy.save("data/targetAngles_frontLeg", targetAngles_frontLeg)  
#exit()

#Keep sim running
for i in range(0,num_iters):
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
