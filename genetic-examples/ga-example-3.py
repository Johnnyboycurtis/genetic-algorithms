#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 09:01:44 2018

@author: jn107154
"""

'''
GENETIC ALGORITHM STEPS

1. CREATE INITIAL POPULATION

2. EVALUATE THE FITNESS  OF EACH INDIVIDUAL

3. SAMPLE THE PARENTS BASED ON FITNESS

4. CREATE A NEW POPULATION
'''



import numpy as np
import matplotlib.pyplot as plt


def _fitness(x):
    #x = np.array(x)
    if x > -11 and x < 11:
        y = (x**2+x)*np.cos(2*x) + x**2
        return round(y, 6)
    else:
        return 0

'''

def _fitness(x):
    if x > -11 and x < 11:
        y = x**2 + x + 10
        return round(y, 6)
    else:
        return 0
'''

fitness = np.vectorize(_fitness)



def _get_fittest_parent(parents, fitness):
    _fitness = fitness(parents)
    PFitness = list(zip(parents, _fitness))
    PFitness.sort(key = lambda x: x[1], reverse=True)
    best_parent, best_fitness = PFitness[0]
    return round(best_parent, 4), round(best_fitness, 4)
    


def _generate_parents(population, n):
    parents = np.random.choice(population, size=n)
    return parents

def _mutate(parents, fitness, decay = 0.01):
    n = int(len(parents) * (1-decay))
    scores = fitness(parents)
    idx = scores > 0 ## positive values only
    scores = scores[idx]
    parents = np.array(parents)[idx]
    ## resample parents with probabilities proportional to fitness
    ## then, add some noise for 'random' mutation
    children = np.random.choice(parents, size=n, p = scores / scores.sum()) + np.random.uniform(-0.51,0.51, size=n)
    return children.tolist() ## new parents
    

def find_best_fit(parents, fitness, initialize_fn, mutate_fn, popsize = 100, max_iter = 100):
    History = []
    ## initial parents; gen zero
    best_parent, best_fitness = _get_fittest_parent(parents, fitness)
    
    x = np.linspace(start=-20, stop=20, num=100)
    
    plt.plot(x, fitness(x))
    plt.scatter(parents, fitness(parents), marker= 'x')    
    
    ## first generation
    _x = [-np.inf]
    ## next generation
    for i in range(1, max_iter + 1):
        parents = _mutate(parents, fitness=fitness)
        
        curr_parent, curr_fitness = _get_fittest_parent(parents, fitness)
        
        ax = plt.scatter(parents, fitness(parents))
        plt.pause(0.09)
        if curr_fitness > best_fitness:
            best_fitness = curr_fitness 
            best_parent = curr_parent 
            
        curr_parent, curr_fitness = _get_fittest_parent(parents, fitness)
        print('generation {}| best fitness {}| current fitness {} | current_parent {}'.format(i, best_fitness, curr_fitness, curr_parent))
        _x.append(np.max(fitness(parents)))
        History.append((i, np.max(fitness(parents))))
        
        ax.remove() ## remove points
    
    
    print(best_parent, best_fitness)
    plt.scatter(parents, fitness(parents))
    plt.scatter(best_parent, fitness(best_parent), marker = '.', c = 'b', s = 200)
    plt.pause(0.09)
    plt.ioff()
    ## return best parents
    print('STOP generation {}| best fitness {}| best_parent {}'.format(i, best_fitness, best_parent))
    
    import time
    time.sleep(5)
    
    return best_parent, best_fitness, History





if __name__ == '__main__':
    plt.ion()
    init_pop = np.linspace(start=-20, stop=20, num=200) ## population range
    parent_, fitness_, history_ = find_best_fit(init_pop, fitness, _generate_parents, _mutate)
    print('top parent {}, top fitness {}'.format(parent_, fitness_))

    