import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import math
#Set up
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
robot2Id = p.loadURDF("body_2.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robot2Id)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)


#Keep sim running
for i in range(0,1000):
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot2Id,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = -math.pi/4.0,
        maxForce = 500
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot2Id,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = math.pi/4.0,
        maxForce = 500
    )


numpy.save("data/backLegSensorVals", backLegSensorValues)
numpy.save("data/frontLegSensorVals", frontLegSensorValues)

p.disconnect()
