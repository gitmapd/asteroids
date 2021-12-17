import math
import numpy as np

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self) -> str:
        return f"{Vector(self.x,self.y,self.z)}"
