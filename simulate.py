import pybullet as p
import pybullet_data
import time

#Set up
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")

#Keep sim running
for i in range(0,1000):
    time.sleep(1/60)
    p.stepSimulation()
    print(i)
p.disconnect()