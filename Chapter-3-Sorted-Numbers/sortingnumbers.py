class SortedNumbers:
    
    def __init__(self, totalNumbers):
        self.totalNumbers = totalNumbers
        
    def sort_numbers(self, totalNumbers=None):
        if not totalNumbers:
            totalNumbers = self.totalNumbers
        geneset = [i for i in range(100)]
        startTime =  datetime.now()
        
        def fnDisplay(candidate):
            display(candidate, startTime)
            
        def fnGetFitness(genes):
            return get_fitness(genes)
        
        optimalFitness =  Fitness(totalNumbers, 0)
        best = get_best(fnGetFitness, totalNumbers, optimalFitness, geneset, fnDisplay)  ## targetLen = totalNumbers
        
        return ('not optimalFitness > best.Fitness', not optimalFitness > best.Fitness)


def get_fitness(genes):
    fitness = 1
    gap = 0

    for i in range(1, len(genes)):
        if genes[i] > genes[i - 1]:
            fitness += 1
        else:
            gap += genes[i - 1] - genes[i]
    return Fitness(fitness, gap)


## display
from datetime import datetime

def display(candidate, startTime):
    timeDiff = datetime.now() - startTime
    txt  = ','.join(map(str, candidate.Genes))
    print('{}\t{}\t{}'.format(txt, candidate.Fitness, timeDiff))
    


## genetic.py
import random

class Chromosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness        

def _generate_parent(length, geneSet, get_fitness):
    '''
    Generates a list of initial values to work with
    '''
    random.seed(123)
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    fitness = get_fitness(genes)
    print('initial parents', genes)
    return Chromosome(genes, fitness)


def _mutate(parent, geneSet, get_fitness):
    childGenes = parent.Genes[:]
    #index = random.randrange(0, len(parent.Genes))
    #newGene, alternate = random.sample(geneSet, 2)
    #childGenes[index] = alternate if newGene == childGenes[index] else newGene
    index = range(len(parent.Genes))
    aindex, bindex = random.sample(index, 2)
    a, b = childGenes[aindex], childGenes[bindex]
    childGenes[aindex], childGenes[bindex] = b, a ## reverse
    fitness = get_fitness(childGenes)
    return Chromosome(childGenes, fitness)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    bestParent = _generate_parent(targetLen, geneSet, get_fitness)
    if not optimalFitness > bestParent.Fitness:
        return bestParent
    
    print('Number Set\t Fitness\tTime')
    while True:
        child = _mutate(bestParent, geneSet, get_fitness)
        display(child)
        if not child.Fitness > bestParent.Fitness:
            continue
        display(child)
        if not optimalFitness > child.Fitness:
            return child
        bestParent = child
        
        
class Fitness:
    def __init__(self, numbersInSequenceCount, totalgap):
        self.NumbersInSequence = numbersInSequenceCount
        self.TotalGap = totalgap
        
    def __gt__(self, other):
        if self.NumbersInSequence != other.NumbersInSequence:
            return self.NumbersInSequence > other.NumbersInSequence
        return self.TotalGap < other.TotalGap

    def __str__(self):
        return '({}, {})'.format(self.NumbersInSequence, self.TotalGap)
    
    def __repr__(self):
        return '(Sequence={}, TotalGap={})'.format(self.NumbersInSequence, self.TotalGap)
            
            
if __name__ == '__main__':
    x = SortedNumbers(10)
    x.sort_numbers(totalNumbers=5)