from entity.TargetFunction import TargetFunction
from entity.Population import Population
from entity.EncodingMethod import EncodingMethod
from entity.GeneticAlgorithm import GeneticAlgorithm

class ClassicGA(GeneticAlgorithm):
    def runOneEpoch(self) -> Population:
        self.population.reproduction()
        self.population.genocide()
        self.population.mutate()
        return self.population        
