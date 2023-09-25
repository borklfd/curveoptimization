import numpy as np
import matplotlib.pyplot as plt
import time

#suppose that gravity is g=1 ms-2 and the object has a mass of m=1 kg
class Segment:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        self.len = self.length()
        self.v = self.vx(p0)


    def total_velocity(self, p):
        return np.sqrt(20-2*p)
    def length(self):
        return np.sqrt((self.p0-self.p1)**2+1)

    def angle(self):
        return np.arccos(1/self.length())

    def time(self):
        return 1/self.v

    def vx(self, p):
        return self.total_velocity(p)/self.len

    def transition(self, p2):
        p0 = self.p1
        p1 = p2
        self.p0 = p0
        self.p1 = p1
        self.len = self.length()
        self.v = self.vx(p0)
        return self.time()



def compare(t1, t2):
    diff = t1-t2
    return diff

def goodsqrt(x):
    if x < 0:
        return -np.sqrt(-x)
    return np.sqrt(x)

st = np.array([])
a = np.array([10.0])
for i in range(10):
    a = np.append(a, 9.0-i)
a_1 = a.copy()
for p in range(1, 9):
    a[p] += np.random.rand()*2-1
#plt.plot(a)
#plt.show()
iterations = np.array([])
for i in range(20):
    s = Segment(a[0], a[1])
    iterations = np.append(iterations, s)
t = np.array([])
for i in range(10):
    t = np.append(t, 1)
t_1 = t.copy()

for i in iterations:
    diff_t = compare(t_1, t)
    diff_a = compare(a_1, a)
    t_1 = t.copy()
    t = np.array([10])

    for p in range(1, 9):
        if diff_a[p]*diff_t[p]>0:
            a[p] -= diff_t[p]/goodsqrt(diff_a[p])*np.random.rand()*0.5
        elif diff_a[p] != 0:
            a[p] += diff_t[p]/goodsqrt(diff_a[p])*np.random.rand()*0.5
        else:
            a[p] += np.random.rand()*0.5
    plt.plot(a)
    plt.show()
    i.p1 = a[1]
    for j in a[2:]:
        dt = i.transition(j)
        t = np.append(t, dt)
    st = np.append(st, t.sum())
    time.sleep(0.1)


###########################################


print(st)
