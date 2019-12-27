#pointCharge v0.0
#author: Jason Yi
#jtyi@ucdavis.edu
#Description: This file is used to create a point charge object for quantum
#mechanical and classical simulations.

from formulaBox import FormulaBox
fb = FormulaBox()
class PointCharge():
    def __init__(self,mass,vi,q,config):
        self.charge = q #coloumbs
        self.mass = mass
        self.v = vi
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
    def getMass(self):
        return self.mass
    def getCharge(self):
        return self.charge
    def getVelocity(self):
        return self.v
