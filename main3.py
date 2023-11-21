import numpy as np
import matplotlib.pyplot as plt

g = 9.81
hmax = 5
length = 10
pp = np.arange(length)
hh = np.linspace(0, hmax, length)## h lefelé növekszik
hh0 = hh.copy()


def simulate(hh):
    tt = np.array([])
    v = 1
    for h in range(1, len(hh)):
        v_1 = v
        if hh[h]<0:
            return 1
        v = np.sqrt(2*g*hh[h])
        dh = hh[h]-hh[h-1]
        t = 2*np.sqrt(dh**2+1)/(v+v_1)
        tt = np.append(tt, t)
    return tt


def accept(t0, t1, T):
    if t1 < t0:
        return True
    else:
        r = np.random.rand()
        if r < np.exp(-(t1-t0)/T):
            return False
        else:
            return False


tlist = np.array([])
t = np.sum(simulate(hh))
T = 1
for i in range(10000):
    for h in range(1, len(hh)-1):
        hhc = hh.copy()
        #hhc = hmax*hhc/hhc[p-1]
        change = np.random.normal(0, 1)
        for hc in range(h, len(hhc)-1):
            hhc[hc] += change*(np.exp(h-hc))
        tt = simulate(hhc)
        if type(tt)!=int:
            t1 = sum(tt)
        else:
            t1 = 9999999
        if accept(t, t1, T):
            t = t1
            tlist = np.append(tlist, t)
            hh = hhc.copy()
    T = T*0.9

plt.ylabel("Position")
plt.xlim(0, max(hmax, length - 1))
plt.ylim(-max(hmax, length - 1), 0)
plt.plot(pp, -hh)

plt.show()
plt.ylabel("Time")
plt.plot(tlist)
plt.show()
print(hh)
