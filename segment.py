import numpy as np


class Segment:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        self.len = self.length()
        self.slope = p1-p0
        self.v = self.vx(p1)

    """simulated annealing"""

    def total_velocity(self, p):
        if p > 100:
            return 0
        return np.sqrt(200-2*p)

    def length(self):
        return np.sqrt((self.p0-self.p1)**2+1)

    def angle(self):
        return np.arccos(1/self.length())

    def time(self):
        if self.v <= 0:
            return 999999
        return 1/self.v

    def vx(self, p):
        return self.total_velocity(p)/self.len

