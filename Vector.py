import math
import numpy as np

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self) -> str:
        return f"{Vector(self.x,self.y,self.z)}"
    
    def __str__(self) -> str:
        return f"{self.x,self.y,self.z}"
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __mul__(self,other):
        if isinstance(other,Vector):
            return (self.x*other.x + self.y*other.y + self.z*other.z)
        elif isinstance(other,(int,float)):
            return Vector(self.x*other,self.y*other,self.z*other)
        else:
            raise TypeError("operand must int or float")
    def __truediv__(self,other):
        if isinstance(other,(int,float)):
            return Vector(self.x/other,self.y/other, self.z/other)
        else:
            raise TypeError("operand must int or float")


a=Vector(2,3,4)
b=Vector(2,3,4)
d=3
c=a/d
print(c)