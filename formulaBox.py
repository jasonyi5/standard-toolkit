#formulaBox v0.0
#author: Jason Yi
#jtyi@ucdavis.edu
#Description: This file is a generic formula sheet with formulas here used to
#describe atomic and electromagnetic interactions.
#This is by no means close to a complete list. Formulas are added based on
#necessity depending on the current enviroment

import numpy as np
import math

class FormulaBox:
    def __init__(self):
        #useful constants
        self.c = (2.99792 * (10 ** 8)) #m/s; speed of light
        self.h = (6.62607 * (10 ** -34)) #Js; Planck's constant
        self.Avo = (6.02214 * (10 ** 23)) #dimensionless; Avogadro's Number
        self.fundamentalCharge = (1.60218 * (10 ** -19)) # c; fundamental charge
        self.amu = (1.66054 * (10 ** -27)) #kg; atomic mass unit in kg, also the mass of a proton/neutron
        self.k = (8.988 * (10 ** 9)) #Nm^2/c^2; Coloumb's constant
        self.rydberg = (1.09737 * (10 ** 7)) #m^-1; Rydberg's constant
        self.vp = (8.85418 * (10 ** -12)) #c^2/Nm^2; vacuum permittivity constant
        
        return

    #math formulas
    def oneDimDist(self,rA,rB):
        return abs(rA - rB)
    
    #basic kinomatic equations

    #kinomatic equation one, solved for every variable
    def kinomaticOnexf(self,xi,vi,a,t):
        return xi + (vi*t) + (0.5 * a * (t ** 2))
    def kinomaticOnexi(self,xf,vi,a,t):
        return xf - (vi*t) - (0.5 * a * (t ** 2))
    def kinomaticOnevi(self,xi,xf,a,t):
        return (xf - xi - (0.5 * a * (t ** 2))) / t
    def kinomaticOnea(self,xi,xf,vi,t):
        return (2 * (xf - xi - (vi * t))) / (t ** 2)

    #kinomatic equation two, solved for every variable
    def kinomaticTwovf(self,vi,a,t):
        return vi + (a * t)
    def kinomaticTwovi(self,vf,a,t):
        return vf - (a * t)
    def kinomaticTwoa(self,vi,vf,t):
        return (vf - vi) / t
    def kinomataicTwot(self,vi,vf,a):
        return (vf - vi) / a

    #kinomatic equation three, solved for every variable
    def kinomaticThreevf(self,vi,a,xi,xf):
        return math.sqrt((vi ** 2) + 2 * a * (xf - xi))
    def kinomaticThreevi(self,vf,a,xi,xf):
        return math.sqrt((vf ** 2) - 2 * a * (xf - xi))
    def kinomaticThreea(self,vi,vf,xi,xf):
        return ((vf ** 2) - (vi ** 2)) / (xf - xi)
    def kinomaticThreexf(self,vi,vf,a,xi):
        return (((vf ** 2) - (vi ** 2)) + (2 * a * xi)) / (2 * a)
    def kinomaticThreexi(self,vi,vf,a,xf):
        return (((vf ** 2) - (vi ** 2)) - (2 * a * xi)) / (-2 * a)

    #force equations
    def generalForce(self,m,a):
        return m * a
    def electroStatic(self,q1,q2,r):
        return (self.k * q1 * q2) / (r ** 2)
    def friction(self,mu,mass):
        return mu * (mass * 9.8)

    #energy
    def electroPoten(self,q1,q2,r):
        return (self.k * q1 * q2) / (r)
    def kinetic(self,m,v):
        return 0.5 * m * (v ** 2)
    
    #momentum
    def momentum(self,m,v):
        return m * v
