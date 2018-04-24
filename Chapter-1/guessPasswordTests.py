import unittest
import datetime
import genetic


class GuessPasswordTests(unittest.TestCase):
    geneset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!. '
    
    def test_Hello_World(self):
        target = 'Hello World!'
        self.guess_password(target)
    
    def guess_password(self, target):
        
        startTime = datetime.datetime.now()
        
        def fnGetFitness(genes):
            return get_fitness(genes, target)
        
        def fnDisplay(genes):
            display(genes, target, startTime)
        
        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(best, target)
        
def display(genes, target, startTime):
    timeDiff = datetime.datetime.now()
    fitness = get_fitness(genes, target)
    print("{}\t{}\t{}".format(genes, fitness, timeDiff))
    
## fitness
def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)


if __name__ == '__main__':
    test_Hello_World()
    