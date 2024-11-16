from GeneticAlgorithms.ClassicGA import ClassicGA
from entity.TargetFunction import TargetFunction
from entity.Population import Population
from entity.EncodingMethod import EncodingMethod
from entity.GeneticAlgorithm import GeneticAlgorithm
from random import random
from entity.Agent import Agent
from settings.GASettings.EliteGASettings import EliteGASettings

class EliteGA(ClassicGA, EliteGASettings):
    def __init__(self, population):
        super().__init__(population)

    def getElite(self):
        return sorted(self.population, key=lambda agent: agent.fitness)[-self.eliteCount:]
    
    def newBreed(self) -> list[Agent]:
        newBreed = self.getElite()
        while len(newBreed) < self.population.populationCount:
            newBreed += self.reprodaction(self.getPairForReprodaction())
        return newBreed