import random
import datetime

class Chromosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness
        
def _mutate(parent, geneSet, get_fitness):
    index = random.randrange(start=0, stop=len(parent.Genes))
    childGenes = list(parent.Genes)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    genes = ''.join(childGenes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _generate_parent(length, geneSet, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    genes = ''.join(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed(123)
    bestParent = _generate_parent(targetLen, geneSet, get_fitness)
    display(bestParent)
    if bestParent.Fitness >= optimalFitness:
        return bestParent
    
    while True:
        child = _mutate(bestParent, geneSet, get_fitness)
        
        if bestParent.Fitness >= child.Fitness:
            continue
        display(child)
        if child.Fitness >= optimalFitness:
            return child
        bestParent = child
    

def display(candidate, startTime):
    timeDiff = datetime.datetime.now()
    print('{}\t{}\t{}'.format(candidate.Genes, candidate.Fitness, timeDiff))
    
    
def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)



import unittest

class GuessPasswordTests(unittest.TestCase):
    geneset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!. '
    
    def test_Hello_World(self):
        target = 'Hello World!'
        self.guess_password(target)
    
    def guess_password(self, target):
        
        startTime = datetime.datetime.now()
        
        def fnGetFitness(genes):
            return get_fitness(genes, target)
        
        def fnDisplay(candidate):
            display(candidate, startTime)
        
        optimalFitness = len(target)
        best = get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(best.Genes, target)
