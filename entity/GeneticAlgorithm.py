import abc
from entity.TargetFunction import TargetFunction
from entity.Population import Population
from entity.EncodingMethod import EncodingMethod

class GeneticAlgorithm(abc.ABC):
    def __init__(self, population: Population):
        self.population = population
    
    @abc.abstractmethod
    def runOneEpoch() -> Population: pass

    def run(self, epochCount: int):
        for _ in range(epochCount): yield self.runOneEpoch()