from GeneticAlgorithms.EliteGA import EliteGA
from entity.Agent import Agent

class Elite2GA(EliteGA):
    def newBreed(self) -> list[Agent]:
        newBreed = self.getElite()
        while len(newBreed) < self.population.populationCount + self.eliteCount:
            newBreed += self.reprodaction(self.getPairForReprodaction())        
        newBreed = sorted(newBreed, key=lambda agent: agent.fitness)[-self.population.populationCount:]
        return newBreed
