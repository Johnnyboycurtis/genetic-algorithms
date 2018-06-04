#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:13:37 2018

@author: jn107154
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


#x = (1,2,1,3,4)
#y = (10, 2,10, 3,1)
#plt.plot(x,y)

'''
REFERENCES:
    http://pesona.mmu.edu.my/~ianchai/teaching/ECP1032/greedy.html
    http://lcm.csa.iisc.ernet.in/dsa/node186.html
    http://www-eio.upc.es/~nasini/Blog/TSP_Notes.pdf    
'''


def gen_locations(seed=123, size=5):
    np.random.seed(seed)
    x = np.random.randint(low = 1, high = 10+1, size = size)
    y = np.random.randint(low = 1, high = 10+1, size = size)
    print(list(zip(x,y)))
    return x,y



def example():
    x = np.array([1,4,15,15,18])
    y = np.array([7,3,0,7,4,0])
    return x,y


class TPSolve:
    def __init__(self, x, y):
        '''
        Greedy solution for Traveling Salesman Probmem
        
          The main idea behind a greedy algorithm is local optimization. 
          That is, the algorithm picks what seems to be the best thing to do at
          the particular time, instead of considering the global situation.
          Hence it is called "greedy" because a greedy person grabs anything 
          good he can at the particular time without considering the long-range 
          implications of his actions.
        '''
        self.x = x
        self.y = y
        self.path = None # (np.array, np.array)
    
    def plot(self):
        plt.scatter(self.x, self.y)
        if self.path:
            a,b = list(zip(*self.path))
            plt.plot(a,b)
            plt.title('Distnace: {}'.format(self.distance))

    def solve(self, return_=False):
        '''Greedy iterative solution to the TP problem from (0,0)'''
        points = list(zip(self.x, self.y))
        start = (0,0)
        d = 0
        path = [start]
        iters = range(len(points))
        for _ in tqdm(iters):
            dist, p2 = _return_closest(start, points)
            points.remove(p2)
            path.append(p2)
            d += dist
            start = p2
        d += distance(start, (0,0))
        path.append((0,0))
        
        print(path)
        self.path = path
        self.distance = round(d, 3)
        
        if return_:
            return round(d,3), path

        
def _return_closest(p1, candidates):
    distances = []
    for p2 in candidates:
        d = distance(p1, p2)
        distances.append((d, p2))
    distances.sort(key = lambda x: x[0], reverse=False)
    return distances[0] ## return (distance, p2)
    
            

def distance(p1, p2):
    '''Returns Euclidean Distance between two points'''
    x1, y1 = p1
    x2, y2 = p2
    d = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d == 0:
        d = np.inf
    return d



if __name__ == '__main__':
    x,y = gen_locations(456,15)
    solution = TPSolve(x, y)
    solution.plot()
    solution.solve()
    solution.plot()
    
