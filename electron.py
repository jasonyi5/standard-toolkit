#electron v0.0
#author: Jason Yi
#jtyi@ucdavis.edu
#Description: This file is an electron object. It is a simulated version of
#an electron to be used in simple quantum mechanical simulations.
#This is by no means an accurate depiction of an electron, rather a simplified
#version.

#position in 1D, 2D, and 3D; set and change position
#only one time dimension
#movement of charged particle induces magnetic force and force
#opposite charges oppose each other

import numpy as np
from random import random
class Electron:
    def __init__(self,config):
        self.mass = (9.10938 * (10 ** -31)) #kilograms
        self.charge = -(1.60218 * (10 ** -19)) #coloumbs
        self.spin = random()
        self.x, self.y, self.z = 0, 0, 0
        if self.spin >= 0.5:
            self.spin = 0.5
        else:
            self.spin = -0.5
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
    #instance variable return functions
    def getPos(self):
        return self.pos
    def getMass(self):
        return self.mass
    def getCharge(self):
        return self.charge
    def getSpin(self):
        return self.spin
