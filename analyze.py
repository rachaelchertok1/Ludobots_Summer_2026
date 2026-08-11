import numpy
import matplotlib.pyplot as mp

#numpy.load returns a numpy array
backLegSensorValues = numpy.load("data/backLegSensorVals.npy")
print(backLegSensorValues)

frontLegSensorValues = numpy.load("data/frontLegSensorVals.npy")
print(frontLegSensorValues)

#Since we're supplying 1 arg, it'll be treated as the y vals
mp.plot(backLegSensorValues, label="Back Leg Sensor Values", linewidth=3)
mp.plot(frontLegSensorValues, label = "Front Leg Sensor Values")
mp.legend()
mp.show()