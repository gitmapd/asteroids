import math
import numpy as np

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f'Vector3D({self.x!r}, {self.y!r}, {self.z!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y, self.z)

    def __bool__(self):
        return bool(abs(self))

    def __mul__(self,other):
        if isinstance(other,Vector3D):
            return (self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(other,(float,int)):
            return (self.x * other, self.y * other, self.z * other)

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z= self.z+other.z
        return Vector3D(x,y,z)

    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        z=self.z-other.z
        return Vector3D(x,y,z)

    def dot(self,other):
        x=self.x*other.x
        y=self.y*other.y
        z=self.z*other.z
        return x+y+z

    def angle_between(self,other,degrees=False):
        dp = self.dot(other)
        cos_theta = dp / abs(self) * abs(other)
        theta = math.acos(cos_theta)
        if degrees:
            return theta * 180 / math.pi



