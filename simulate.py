import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim

#Set up
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
robot2Id = p.loadURDF("body_2.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robot2Id)
#Keep sim running
for i in range(0,1000):
    time.sleep(1/60)
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print("Back leg touch sensor: ", backLegTouch)
    print("Sim idx: ", i)
p.disconnect()