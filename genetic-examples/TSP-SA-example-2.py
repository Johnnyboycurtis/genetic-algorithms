#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:07:20 2018

@author: jn107154
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


def gen_locations(seed=123, size=15):
    np.random.seed(seed)
    x = np.random.randint(low = 1, high = 10+1, size = size)
    y = np.random.randint(low = 1, high = 10+1, size = size)
    #print(list(zip(x,y)))
    return x,y



class Path:
    def __init__(self, points):
        self.points = points # genes
        self._create_path() # genes
    
    def __repr__(self):
        return 'Path Distance: {}'.format(round(self.distance, 3))
    
    def __len__(self):
        return len(self.points)
    
    def copy(self):
        return Path(points = self.points)
        
    def _create_path(self, return_=False):
        points = self.points.copy()
        _init = points.pop(0) # get first item as start
        p1 = tuple(_init) # make copy; it will be end as well
        path = [p1]
        d = 0
        for p2 in points:
            path.append(p2)
            d += distance(p1, p2)
            #print(p1, p2, d)
            p1 = p2
        path.append(_init) ## start == end
        d += distance(p1, _init)
        #print(p1, _init, d)
        #path.append(_init) # append starting point as ending point
        self.path = path
        self.distance = d
        
        if return_:
            return d, path
    
    def plot(self, i=''):
        x,y = list(zip(*self.points))
        plt.scatter(x, y, marker='x')
        a,b = list(zip(*self.path))
        plt.plot(a,b)
        plt.title('{} Distnace: {}'.format(i,round(self.distance, 3)))


def distance(p1, p2):
    '''Returns Euclidean Distance between two points'''
    x1, y1 = p1
    x2, y2 = p2
    d = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d == 0:
        d = np.inf
    return d



def path_cost(path):
    start = path.pop() ## should be in order
    d = 0 # distance
    for p2 in reversed(path):
        d += distance(start, p2)
        print('{} --> {}: {}'.format(start, p2, round(d, 3)))
        start = p2
    return d




class SA:
    def __init__(self, points, T):
        self.points = random.sample(population=points, k=len(points))
        self.T = T
        #self.func = func
    
    def solve(self, N=50):
        T = self.T
        path = Path(self.points)
        plt.ion()
        iterations = np.arange(N)
        fitness = []
        best_path = path.copy()
        for it in iterations:
            points = self._rearrange(path.points.copy())
            prop = Path(points)
            hprop = prop.distance
            hcur = path.distance
            p = max(0, min(1, np.exp(-(hprop - hcur) / T)))
            if hcur > hprop: ## suggested by Zbigniew Michaelwics and David Fogel (How to Solve It: Modern Heuristics)
                p = 1
            if np.random.rand() < p:
                path = prop
            T = 0.95 * T
            fitness.append(path.distance)
            if best_path.distance > path.distance:
                best_path = path.copy()
            plt.cla()
            path.plot('{} with p={}'.format(it, round(p,3)))
            plt.pause(0.15)
        plt.cla()
        best_path.plot()
        plt.pause(5)
        plt.cla()
        plt.plot(iterations, fitness)
        plt.xlabel('iterations')
        plt.ylabel('distance')
        plt.title('fitness over time (lower is better)')
        plt.show()
        plt.pause(5)
        self.T = T
        return best_path
    
    def _rearrange(self, points):
        '''
        Rearrangements. An efficient set of moves has been suggested by Lin [6] . The
        moves consist of two types: (i) A section of path is removed and then replaced
        with the same cities running in the opposite order; or (ii) a section of path is
        removed and then replaced in between two cities on another, randomly chosen,
        part of the path.
        '''
        stop = random.randint(1, len(points))
        start = random.randint(0, stop)
        points[start:stop] = reversed(points[start:stop])
        return points
        



if __name__ == '__main__':
    x,y = gen_locations(456,15) ## lowest distance 32.85
    #x,y = example()
    points = list(zip(x,y))
    p = Path(points)
    print('Initial', p)
    #func = lambda x: (100 / x)**2 # weighting function; higher means shorter distance
    solver = SA(points = points, T = 125)
    solution = solver.solve(N=2000)
    solution.plot()
    print('Solution', solution, 'final temp', round(solver.T, 6))
    print(str(solution.path))
    plt.show()
    # does not return optimal solution
    # optimal solution = 48.39
    # a, b, f, e, d, c, a
    '''
    solution.path
    Out[17]: 
    [(5, 7),
     (6, 7),
     (5, 6),
     (4, 4),
     (3, 4),
     (3, 1),
     (5, 1),
     (6, 1),
     (9, 3),
     (9, 4),
     (10, 6),
     (8, 10),
     (6, 9),
     (2, 9),
     (3, 8),
     (5, 7)]
    #distance 32.85
    '''
