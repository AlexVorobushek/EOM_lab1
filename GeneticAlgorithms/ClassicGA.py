from entity.TargetFunction import TargetFunction
from entity.Population import Population
from entity.EncodingMethod import EncodingMethod
from entity.GeneticAlgorithm import GeneticAlgorithm
from random import random
from entity.Agent import Agent

class ClassicGA(GeneticAlgorithm):
    def __init__(self, population):
        super().__init__(population)

    def getPairForReprodaction(self) -> tuple[Agent, Agent]:        
        return self.population.choise(), self.population.choise()

    def reprodaction(self, pair: tuple[Agent, Agent]):
        return pair[0] + pair[1]
    
    def newBreed(self) -> list[Agent]:
        newBreed = []
        while len(newBreed) < self.population.populationCount:
            newBreed += self.reprodaction(self.getPairForReprodaction())
        return newBreed
    
    def mutate(self):
        roulette = lambda: random() < self.population.mutateProbability
        self.population.agents = list(map(lambda x: x if not roulette() else x.mutate(), self.population))


    def runOneEpoch(self) -> Population:
        self.population.agents = self.newBreed()
        self.mutate()
        return self.population