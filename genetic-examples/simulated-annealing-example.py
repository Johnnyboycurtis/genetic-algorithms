import numpy as np
import matplotlib.pyplot as plt


#'''
def h(x):
    if x < -10 or x > 10:
        y = 0
    else:
        y = (x**2+x)*np.cos(2*x) + 20
    return y


'''
def h(x):
    if x < -1 or x > 1:
        y = 0
    else:
        y = (np.cos(50*x) +  np.sin(20*x))**2
    return y
'''

hv = np.vectorize(h)


'''
def SA(search_space, func, T):
    scale = np.sqrt(T)
    start = -0.21 #np.random.choice(search_space)
    x = start * 1
    for i in range(10):
        prop = x + np.random.uniform(-1, 1) * scale
        if func(prop) > func(x):
            p = 1
        else:
            p = max(0, min(1, np.exp( (func(prop) - func(x))/ T)))
        if np.random.rand() < p:
            print((prop,func(prop)), (x, func(x)))    
            x = prop
        T = 0.9 *T ## cooling
    return (start,x), (func(start), func(x))
'''



def SA(search_space, func, T, N=100):
    scale = np.sqrt(T)
    start = -0.4 # np.random.choice(search_space)
    x = start * 1
    xsol = []
    ysol = []
    for i in range(N):
        prop = x + np.random.normal() * scale
        p = max(0, min(1, np.exp( (func(prop) - func(x))/ T)))
        if np.random.rand() < p:
            #print((prop,func(prop)), (x, func(x)))    
            x = prop
        T = 0.9 *T ## cooling
        xsol.append(x)
        ysol.append(func(x))
    #return (start,x), (func(start), func(x))
    xsol = np.array(xsol)
    ysol = np.array(ysol)
    return xsol, ysol


if __name__ == '__main__':    
    X = np.linspace(-15, 15, num=100)
    plt.ion()
    for it in range(20):
        plt.cla()
        x1, y1 = SA(X, h, T = 8)
        #print(x1, y1)
        
        plt.plot(X, hv(X))
        #plt.scatter(x1, y1, marker='x')
        plt.plot(x1, y1, '--')
        plt.title('Run:{}, 100 iterations'.format(it))
        plt.pause(0.5)
    
    plt.ioff()
