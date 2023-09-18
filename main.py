import math # will be changed to numpy at some point

class Segment():
    def __init__(self, p0, p1, v): #p0, p1 are lists
        self.p0 = p0.copy()
        self.p1 = p1.copy()
        self.v = v
        self.len = self.length(p0, p1)
        self.ang = self.angle()
        
        
    def length(self):
        """Calculates the length of segment"""
        return math.sqrt((p1[0]-p0[0])**2+(p1[1]-p0[1])**2)

    def angle(self):
        """Calculates the beesési szög"""
        return math.acos(1/self.len)

    def transition(self, p2):
        """Assumes the properties of the new segment"""
        self.p0 = self.p1.copy()
        self.p1 = p2.copy()
        self.len = self.length()
        newang = self.angle()
        self.v = math.sin(newang)*self.v/math.sin(self.ang)
        self.ang = newang

    def time(self):
        """Calculate the time needed to travrese the segment"""
        return self.len/self.v

###################################################################################################
#testing area, will be deleted at some point
points = []
for i in range(10, -1, -1):
    points.append(i)
print(points)
segment = Segment([0, points[0]], [1, points[1]], 10)
time = 0
for i in range(2, len(points)):
    time += segment.time()
    print("Segment no. {n}, time = {t}".format(n=i, t=segment.time()))
    print("angle = {a}".format(a=segment.ang))
    print(segment.p0)
    print(segment.p1)
    print(segment.len)
    segment.transition([i, points[i]])
    
    
print("time =", time)

