import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR:
    def __init__(self, linkName): #class constructor
        self.linkName = linkName
        self.Prepare_To_Sense()

    def Get_Value(self, timestep):
        self.values[timestep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)     

    def Prepare_To_Sense(self):
        self.values = numpy.zeros(c.NUM_ITERS)

    def Save_Values(self):
        numpy.save("data/sensor_vals", self.values)