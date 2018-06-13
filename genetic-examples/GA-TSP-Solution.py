#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:13:37 2018

@author: jn107154
"""

import numpy as np
import matplotlib.pyplot as plt
import random

'''
This is based on traveling-salesman-ga-example.py

REFERENCES:
    http://pesona.mmu.edu.my/~ianchai/teaching/ECP1032/greedy.html
    http://lcm.csa.iisc.ernet.in/dsa/node186.html
    http://www-eio.upc.es/~nasini/Blog/TSP_Notes.pdf
    https://www.hds.utc.fr/~tdenoeux/dokuwiki/_media/en/combinatorial_optimization.pdf

Calculating Complexity:
    https://stackoverflow.com/questions/22977748/complexity-for-greedy-algo-travelling-salesman-and-nearest-neighbor-search    
    
Greedy Search Fails:
    https://matheducators.stackexchange.com/questions/10692/counterexamples-to-the-greedy-algorithm
'''


def gen_locations(seed=123, size=15):
    np.random.seed(seed)
    x = np.random.randint(low = 1, high = 10+1, size = size)
    y = np.random.randint(low = 1, high = 10+1, size = size)
    return x,y



def example():
    '''
    c = (1,7), b = (4,3),  a = (0,0)
    d = (15, 7), e = (15, 4), f = (18, 0)
    greedy search will return a `good enough` solution
    '''
    x = np.array([1,4,0,15,15,18])
    y = np.array([7,3,0,7,4,0])
    return x,y


class GASolve:
    def __init__(self, points, n = 100, decay = 0, mutation_rate=0.5):
        x, y = list(zip(*points))
        self.x = x 
        self.y = y
        self.points = points
        self.decay = decay
        self.mutation_rate = mutation_rate
        self._generate_parents(n)
        self.path = None
    
    def _sample(self):
        return random.sample(self.points, k=len(self.points))
    
    def _generate_parents(self, n):
        parents = []
        for _ in range(n):
            points = self._sample()
            parents.append(Path(points))
        self._init_parents = parents
    
    def solve(self, generations=10):
        parents = self._init_parents
        
        print('\nFITTEST PARENTS')
        print('----------------')
        plt.ion()
        for i_ in range(generations):
            parents.sort(key = lambda x: x.distance, reverse=False)
            best_ = parents[0]
            print('Generation', i_,':', best_)
            #print(parents[:3])
            parents = _mutate(parents, self.decay, self.mutation_rate)
            
            plt.cla()
            best_.plot(i_)
            plt.pause(0.36)
            
        parents.sort(key = lambda x: x.distance, reverse=False)
        plt.ioff()
        #plt.show()
        plt.close()
        

        self.last_generation = parents
        self.path = parents[0]
        
        
def _rearrange(path, mutation_rate):
    '''
    Rearrangements. An efficient set of moves has been suggested by Lin [6] . The
    moves consist of two types: (i) A section of path is removed and then replaced
    with the same cities running in the opposite order; or (ii) a section of path is
    removed and then replaced in between two cities on another, randomly chosen,
    part of the path.
    '''
    points = path.points
    if random.random() < mutation_rate:
        stop = random.randint(1, len(points))
        start = random.randint(0, stop)
        points[start:stop] = reversed(points[start:stop])
    return Path(points)
            

def _mutate(parents, decay, mutation_rate):
    # parents is a list of Paths
    # sample parents based on fitness
    k = int(len(parents) * (1 - decay))
    weights = np.array([1/np.exp(path.distance) for path in parents]) # we want a smaller distance
    weights = weights / weights.sum()
    children = random.choices(population=parents, weights=weights, k = k)
    ## sanity check
    LENGTHS = [len(child) for child in children]
    if min(LENGTHS) != max(LENGTHS):
        print('DIFFERENT LENGTHS', min(LENGTHS), max(LENGTHS))
    ## random mutation per child
    children = [_random_mutate(child, mutation_rate) for child in children]
    #children = [_rearrange(child, mutation_rate) for child in children]
    return children


def _random_mutate(path, mutation_rate):
    if random.random() < mutation_rate:
        points = path.points.copy() # parent genes
        id1 = random.randint(0, len(points)-1)
        id2 = random.randint(0, len(points)-1)
        a, b = points[id1], points[id2]
        childgenes = points.copy()
        childgenes[id1] = b
        childgenes[id2] = a
        path = Path(childgenes)
    return path
    
    

class Path:
    def __init__(self, points):
        self.points = points # genes
        self._create_path() # genes
    
    def __repr__(self):
        return 'Path Distance: {}'.format(round(self.distance, 3))
    
    def __len__(self):
        return len(self.points)
        
    def _create_path(self, return_=False):
        points = self.points.copy()
        _init = points.pop(0) # get first item as start
        p1 = tuple(_init) # make copy; it will be end as well
        path = [p1]
        d = 0
        for p2 in points:
            path.append(p2)
            d += distance(p1, p2)
            p1 = p2
        path.append(_init) ## start == end
        d += distance(p1, _init)
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


def unique(x):
    return list(set(x))
    

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


if __name__ == '__main__':
    x,y = gen_locations(456,15) ## lowest distance 32.85
    #x,y = example()
    points = list(zip(x,y))
    p = Path(points)
    print(p)
    ga = GASolve(points, n=200, decay=0, mutation_rate=0.36)
    ga.solve(generations=50)
    solution = ga.path
    solution.plot()
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