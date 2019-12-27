#collObj v0.0
#author: Jason Yi
#jtyi@ucdavis.edu
#Description: This file is used to create a collision object used to simulate
#collisions between objects of undefined shapes

from formulaBox import FormulaBox
fb = FormulaBox()
class CollObj():
    def __init__(self,mass,vi,config):
        self.mass = mass #kilograms
        self.v = vi #meters per second
        self.x, self.y, self.z = 0, 0, 0
        if config == 1:
            self.pos = [self.x]
        elif config == 2:
            self.pos = [self.x,self.y]
        elif config == 3:
            self.pos = [self.x,self.y,self.z]
    #position functions
    def setPos1D(self,x):
        self.pos = [x]
        return
    def setPos2D(self,x,y):
        self.pos = [x,y]
        return
    def setPos3D(self,x,y,z):
        self.pos = [x,y,z]
        return
    def setVelocity(self,v):
        self.v = v
        return
    #instance variable return functions
    def getPos(self):
        return self.pos
    def getPosX(self):
        return self.pos[0]
    def getMass(self):
        return self.mass
    def getVelocity(self):
        return self.v
