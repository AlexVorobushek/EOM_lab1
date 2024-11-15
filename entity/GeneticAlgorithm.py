import abc
from entity.TargetFunction import TargetFunction
from entity.Population import Population
from entity.EncodingMethod import EncodingMethod

class GeneticAlgorithm(abc.ABC):
    def __init__(self, targetFunction: TargetFunction, population: Population, encodingMethod: EncodingMethod):
        self.TargetFunction: TargetFunction
        self.population = population
        self.encodingMethod = encodingMethod
    
    @abc.abstractmethod
    def runOneEpoch() -> Population: pass