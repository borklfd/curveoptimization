import numpy as np
import matplotlib.pyplot as plt

g = 9.81
hmax = 100
p = 200
hh = np.linspace(0, hmax, p)## h lefelé növekszik
hh0 = hh.copy()
print(hh)

def simulate(hh):
    tt = np.array([])
    v = 0
    vv = np.array([v])
    for h in range(1, len(hh)):
        v_1 = v
        v = np.sqrt(2*g*hh[h])
        vv = np.append(vv, v)
        dh = hh[h]-hh[h-1]
        t = 2*np.sqrt(dh**2+1)/(v+v_1)
        tt = np.append(tt, t)
    return tt


def accept(t0, t1, T):
    if t1 < t0:
        return True
    else:
        r = np.random.rand()
        if r < np.exp(-(t1 - t0) / T):
            return True
        else:
            return False


t = np.sum(simulate(hh))
T = 1
for i in range(1000):
    for h in range(1, len(hh)):
        hhc = hh.copy()
        hhc = hmax*hhc/hhc[p-1]
        change = (-1)**(np.random.rand()>0.5)*0.1
        for hc in range(h, len(hhc)):
            hhc[hc]+= change
        t1 = sum(simulate(hhc))
        if accept(t, t1, T):
            t = t1
            hh = hhc.copy()
    T = T*0.9


plt.plot(-hh)

plt.show()
print(hh)
