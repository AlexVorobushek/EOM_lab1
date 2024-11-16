from entity import TargetFunction
from entity import Population
from entity import EncodingMethod
from entity.GeneticAlgorithm import GeneticAlgorithm
from random import choice, random, randint
from settings.GASettings.lab1GASettings import lab1GASettings
from entity import Agent

class lab1GA(GeneticAlgorithm, lab1GASettings):
    def mutate(self):
        roulette = lambda: random() < self.population.mutateProbability
        self.population.agents = list(map(lambda x: x if not roulette() else x.mutate(), self.population))

    def genocide(self):
        self.population.agents.sort(key=lambda x: x.fitness)
        # self.agents = sorted(self.agents, key=lambda x: x.fitness)
        while len(self.population.agents) > self.population.populationCount:
            self.population.agents.pop(randint(0, len(self.population.agents)//2))
    
    def __getRandomAgent(self) -> Agent:
        return choice(self.population.agents)
    
    def reproduction(self):
        for i in range(self.reproductionPairsCount):
            self.population.agents += self.__getRandomAgent() + self.__getRandomAgent()

    def runOneEpoch(self) -> Population:
        self.reproduction()
        self.genocide()
        self.mutate()
        return self.population        
