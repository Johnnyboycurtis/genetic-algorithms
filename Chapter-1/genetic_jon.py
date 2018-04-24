import random
import string
import datetime as dt



class Genetic():
    def __init__(self, geneSet, _generate_parent, _mutate, _get_fitness):
        self.geneSet = geneSet
        self._generate_parent = _generate_parent
        self._mutate = _mutate
        self._get_fitness = _get_fitness
    
    def get_best(self, targetLen, optimalFitness, startTime, seed=None):
        self.startTime = startTime
        geneSet = self.geneSet
        if seed:
            random.seed(seed)
        bestParent = self._generate_parent(targetLen, geneSet)
        bestFitness = self._get_fitness(bestParent)
        _display(bestParent, bestFitness, startTime)
        if bestFitness >= optimalFitness:
            return bestParent
        
        while True:
            child = self._mutate(bestParent, geneSet)
            childFitness = self._get_fitness(child)
            if bestFitness >= childFitness:
                continue
            _display(child, bestFitness, startTime)
            if childFitness >= optimalFitness:
                return child
            bestFitness = childFitness
            bestParent = child
        








class PWGenetic():
    def __init__(self, geneSet, startTime):
        self.geneSet = geneSet
        self.startTime = startTime

    def _generate_parent(self, length):
        geneSet=self.geneSet
        genes = []
        while len(genes) < length:
            sampleSize = min(length - len(genes), len(geneSet))
            genes.extend(random.sample(geneSet, sampleSize))
        return ''.join(genes)

    def _mutate(self, parent):
        geneSet=self.geneSet
        index = random.randrange(0, len(parent))
        childGenes = list(parent)
        newGene, alternate = random.sample(geneSet, 2)
        childGenes[index] = alternate if newGene == childGenes[index] else newGene
        return ''.join(childGenes)

    def get_fitness(self, guess):
        data = zip(target, guess)
        return sum(1 for expected, actual in data if expected == actual)
    

    
    def get_best(self, targetLen, optimalFitness, geneSet, seed=None):
        if seed:
            random.seed(seed)
        bestParent = self._generate_parent(targetLen)
        bestFitness = self.get_fitness(bestParent)
        _display(bestParent, bestFitness, self.startTime)
        if bestFitness >= optimalFitness:
            return bestParent
        
        while True:
            child = self._mutate(bestParent)
            childFitness = self.get_fitness(child)
            if bestFitness >= childFitness:
                continue
            _display(child, bestFitness, self.startTime)
            if childFitness >= optimalFitness:
                return child
            bestFitness = childFitness
            bestParent = child
        

def _display(guess, fitness, startTime):
    timeDiff = dt.datetime.now() - startTime
    print('{}\t{}\t{}'.format(guess, fitness, timeDiff))
    return None




if __name__ == '__main__':
    geneSet = string.ascii_letters + ' !'
    #target = 'Genetic Algorithms with Python'  
    target='Hello World!'
    print('Gene Set', geneSet)
    startTime = dt.datetime.now()
    test = PWGenetic(geneSet, startTime)
    test.get_best(targetLen=len(target), optimalFitness=len(target), geneSet=geneSet, seed=random.randint(1,100))


    def _generate_parent(length, geneSet):
        genes = []
        while len(genes) < length:
            sampleSize = min(length - len(genes), len(geneSet))
            genes.extend(random.sample(geneSet, sampleSize))
        return ''.join(genes)

    def _mutate(parent, geneSet):
        index = random.randrange(0, len(parent))
        childGenes = list(parent)
        newGene, alternate = random.sample(geneSet, 2)
        childGenes[index] = alternate if newGene == childGenes[index] else newGene
        return ''.join(childGenes)

    def _get_fitness(guess):
        data = zip(target, guess)
        return sum(1 for expected, actual in data if expected == actual)

    gptest = Genetic(geneSet, _mutate=_mutate, _get_fitness=_get_fitness, _generate_parent=_generate_parent)
    gptest.get_best(targetLen=len(target), optimalFitness=len(target), startTime=dt.datetime.now())


