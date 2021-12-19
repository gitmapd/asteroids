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
    def mul_elems(self,other):
        """return a new vector holding each element multipled , = "hadamard product", not the same as scaling or dot product""" 
        if isinstance(other,Vector):
            return (self.x*other.x , self.y*other.y , self.z*other.z)
    def scaling_factor(self,scaling_fac):
        if isinstance(scaling_fac,(int,float)):
            return Vector(self.x*scaling_fac,self.y*scaling_fac,self.z*scaling_fac)  


a=Vector(2,3,4)
b=Vector(2,3,4)
c=b.mul_elems(a)
print(c)