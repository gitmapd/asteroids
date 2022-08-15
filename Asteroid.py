import numpy as numpy

class Asteroid:
    def __init__(self, Vector3D, vx, vy, vz, m):
        self.x  = Vector3D.x
        self.y  = Vector3D.y
        self.z  = Vector3D.z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.m  = m
    def __repr__(self):
        return f'Vector3D({self.x!r},{self.y!r}, {self.z!r})'

    def move(self,t):
        self.x += self.vx * t
        self.y += self.vy * t
        self.z += self.vz * t
        return self.x, self.y, self.z

