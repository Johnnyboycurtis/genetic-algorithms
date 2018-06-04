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

3. SELECT THE PARENTS BASED ON FITNESS

4. CREATE A NEW POPULATION
'''



import numpy as np
import matplotlib.pyplot as plt

def _fitness(x):
    #x = np.array(x)
    if x > -11 and x < 11:
        y = (x**2+x)*np.cos(2*x)
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
    


def _generate_parents(population):
    parents = np.random.choice(population, size=30)
    return parents

def _mutate(parents, fitness, percent = 0.10):
    scores = fitness(parents)
    PFitness = list(zip(parents, scores))
    PFitness.sort(key=lambda x: x[1], reverse=True) ## ascending
    n = len(parents)
    n_parents = np.ceil(n*percent).astype('int')
    fittest_parents = np.array([par for par, _ in PFitness[:n_parents] ])
    children = np.random.choice(fittest_parents, size=n) + np.random.randn(n)
    #children = np.random.uniform(mu-sd, mu+sd, size = n).tolist()
    return children.tolist() ## new parents
    

def find_best_fit_W(population, fitness, initialize_fn, mutate_fn, max_iter = 10):
    firstparents = initialize_fn(population)
    History = []
    ## initial parents; gen zero
    _get_fittest_parent(firstparents, fitness)
    best_parent, best_fitness = _get_fittest_parent(firstparents, fitness)
    
    ## first generation
    parents = _mutate(firstparents, fitness=fitness)
    curr_parent, curr_fitness = _get_fittest_parent(parents, fitness)
    i = 1
    print('generation {}| best fitness {}| current fitness {} | current_parent {}'.format(i, best_fitness, curr_fitness, curr_parent))
    
    _x = [-np.inf]
    ## next generation
    while np.abs(np.mean(_x) - best_fitness) > 0.01:
        if curr_fitness > best_fitness:
            best_fitness = curr_fitness * 1
            best_parent = curr_parent * 1
            
        i += 1
        parents = _mutate(parents, fitness=fitness)
        curr_parent, curr_fitness = _get_fittest_parent(parents, fitness)
        #print('generation {}| best fitness {}| current fitness {} | current_parent {}'.format(i, best_fitness, curr_fitness, curr_parent))
        _x.append(np.max(fitness(parents)))
        History.append((i, np.max(fitness(parents))))
        if i > 1000:
            break
    ## return best parents
    print('STOP generation {}| best fitness {}| best_parent {}'.format(i, best_fitness, best_parent))
    return best_parent, best_fitness, History





if __name__ == '__main__':
    init_pop = np.linspace(start=-50, stop=50, num=100) ## population range
    parent_, fitness_, history_ = find_best_fit_W(init_pop, fitness, _generate_parents, _mutate)
    print('top parent {}, top fitness {}'.format(parent_, fitness_))
    
    x = np.linspace(start=-20, stop=20, num=100)

    plt.plot(x, fitness(x))
    plt.scatter(parent_, fitness_)
    plt.show()
    
    #a, b = list(zip(*history_))
    #a = np.array(a); b = np.array(b)
    #plt.plot(a, b)
    #plt.ylim(-20, 150)
    #plt.title('MAX FITNESS OVER TIME')
    #plt.show()

    