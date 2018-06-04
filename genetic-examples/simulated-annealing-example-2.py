import numpy as np
import matplotlib.pyplot as plt


'''
def h(x):
    if x < -10 or x > 10:
        y = 0
    else:
        y = (x**2+x)*np.cos(2*x)
    return y


'''
def h(x):
    if x < -1 or x > 1:
        y = 0
    else:
        y = (np.cos(50*x) +  np.sin(20*x))**2
    return y
#'''

hv = np.vectorize(h)



def SA(search_space, func, T):
    scale = np.sqrt(T)
    #scale = np.sqrt(max(search_space) - min(search_space))
    start = np.random.choice(search_space)
    x = start * 1
    cur = func(x)
    for i in range(1000):
        prop = x + np.random.normal()*scale #.uniform(-1, 1, size=1) * scale
        if prop > 1 or prop < 0 or np.log(np.random.rand()) * T > (func(prop) - cur):
            prop = x
        x = prop
        #print(x)
        cur = func(x)
        #T -= T/100 # reduce T by T%
        T = 0.9 *T
    return (start,x), (func(start), func(x))


X = np.linspace(-1, 2, num=1000)
x1, y1 = SA(X, h, T = 4)
print(x1, y1)

plt.plot(X, hv(X))
plt.scatter(x1, y1, marker='x')
plt.plot(x1, y1)
