import string
import random
import sys


geneSet = string.ascii_letters + ' !'
target = 'something more difficult'  #'Hello World!'
print('Gene Set', geneSet)


## population generation

def generate_parent(length):
    genes = []
    while len(genes) < length:
        n = min(length - len(genes), len(geneSet)) ## sample size
        genes.extend(random.sample(geneSet, n))
    return ''.join(genes)


## fitness

def get_fitness(guess, target=target):
    data = zip(target, guess)
    return sum(1 for expected, actual in data if expected == actual)

## mutation
def mutate(parent):
     index = random.randrange(0, len(parent))
     childGenes = list(parent)
     newGene, alternate = random.sample(geneSet, 2)
     childGenes[index] = alternate if newGene == childGenes[index] else newGene
     return ''.join(childGenes)


import datetime as dt

startTime = dt.datetime.now()

def display(guess):
    timeDiff = dt.datetime.now() - startTime
    fitness = get_fitness(guess)
    print('{}\t{}\t{}'.format(guess, fitness, timeDiff))
    return None

if __name__ == '__main__':
    #random.seed(123)
    startTime = dt.datetime.now()
    bestParent = generate_parent(len(target))
    bestFitness = get_fitness(bestParent)
    display(bestParent)

    while True:
        child = mutate(bestParent)
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child
