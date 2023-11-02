import numpy as np
import matplotlib.pyplot as plt
from segment import Segment
import time

#suppose that gravity is g=1 ms-2 and the object has a mass of m=1 kg



def compare(t1, t2):
    diff = t1-t2
    return diff

def goodsqrt(x):
    if x < 0:
        return -np.sqrt(-x)
    return np.sqrt(x)


st = np.array([])
a = np.array([100.0])

for i in range(100):
    a = np.append(a, 99.0-i)
a_1 = a.copy()

for p in range(1, 99):
    a[p] += np.random.rand()*2-1
plt.plot(a)
plt.show()
iterations = np.array([])

for i in range(1000):
    s = Segment(a[0], a[1])
    iterations = np.append(iterations, s)
t = np.array([])

for i in range(100):
    t = np.append(t, 1)
t_1 = t.copy()


for i in iterations:
    diff_t = compare(t, t_1)
    diff_a = compare(a, a_1)
    t_1 = t.copy()
    t = np.array([100])

    for p in range(1, 99):
        if diff_a[p]*diff_t[p]>0:
            a[p] -= goodsqrt(diff_t[p]/diff_a[p])*np.random.normal(0.5, 0.2)
        elif diff_t[p] != 0:
            a[p] += goodsqrt(diff_t[p]/diff_a[p])*np.random.normal(0.5, 0.2)
        else:
            a[p] += 0

    #plt.plot(a)
    #plt.show()
    i.p1 = a[1]
    for j in a[2:]:
        dt = i.transition(j)
        t = np.append(t, dt)
    st = np.append(st, t.sum())


###########################################
plt.plot(a)
plt.show()

print(st)