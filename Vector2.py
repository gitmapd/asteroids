import math
import numpy as np


class Vector2:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __repr__(self):
        return f"{Vector2(self.x,self.y)}"
    def __str__(self):
        return f"{self.x,self.y}"
    def __add__(self,other):
        return f"{Vector2(self.x+other.x,self.y+other.y)}"
    def __sub__(self,other):
        return f"{Vector2(self.x-other.x,self.y-other.y)}"
    def __mul__(self,other):
        if isinstance(other,Vector2):
            return f"{self.x*other.x,self.y*other.x}"
        if isinstance(other,(int,float)):
            return f"{self.x*other,self.y*other}"
    def __truediv__(self,other):
        if isinstance(other,(int,float)):
            return f"{Vector2(self.x/other,self.y/other)}"
    def dot(self,other):
        return self.x*other.x+self.y*other.y
    def length(self):  
        return math.sqrt( self.x**2 + self.y**2 ) 

    def angle_between(self, other, degrees=False):
        """ Returns the angle of self and other vector in radians
            or in degrees (if degrees=True)
        """
        dp = self.dot(other)
        cos_theta = dp / (self.length() * other.length())
        theta = math.acos(cos_theta)
        if degrees:
            return theta * 180 / math.pi
        return theta
    def normalize(self):
        return Vector2(self.x/self.length(),self.y/self.length())
    def to_polar(self):
        return self.length(), math.degrees(math.atan2(self.y, self.x))

