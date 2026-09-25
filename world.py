import pybullet as p
class WORLD:
    def __init__(self): #class constructor
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")