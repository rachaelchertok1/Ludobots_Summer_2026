import pyrosim.pyrosim as pyrosim

x=0
y=0
z=0.5

a=1
b=1
c=1

x2=1
y2=0
z2=1.5
pyrosim.Start_SDF("boxes.sdf")
for i in range(0,10):
    a*=0.9
    b*=0.9
    z+=1
    pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[a,b,c])

#pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[1,1,1])
#pyrosim.Send_Cube(name="Box", pos=[x2,y2,z2], size=[1,1,1])
pyrosim.End()