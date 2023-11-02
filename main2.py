from segment import Segment
import numpy as np
import matplotlib.pyplot as plt

h = 100#height of graph
n = 100 #number of segments
k = 100 #number of iterations
T = 0 #time
T_1 = 0 #previous time
points = np.linspace(n-1, 0, 100) #y-coordinates of points
print(points)
plt.plot(points)
plt.show()
a = np.array([])#scaling modifier
for i in range(1, k+1):
    a = np.append(a, h/(2*np.sqrt(i)))
s = Segment(n, points[1])
t = s.time()
T += t
for i in range(1, n-2):
    s = Segment(points[i], points[i+1])
    t = s.time()
    #(t)
    T += t
s = Segment(points[n-2], 0)
t = s.time()
T += t
print(T)
#########################
for iteration in range(k):
    for segment in range(1, n-2):
        T_1 = T
        T = 0
        temp_points = points.copy()
        temp_points[segment] -= a[iteration]
        s = Segment(n, points[1])
        t = s.time()
        T += t
        for i in range(1, n-2):
            s = Segment(temp_points[i], temp_points[i+1])
            t = s.time()
            T += t
            #print("time:", T)
        s = Segment(temp_points[n-2], 0)
        t = s.time()
        T += t
        if T < T_1:
            points = temp_points.copy()
        else:
            T = T_1



print(points)
print(T)
plt.plot(points)
plt.show()