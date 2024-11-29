from GeneticAlgorithms.CrowdingGA import CrowdingGA
from entity.Agent import Agent
from random import choice

class CrowdingGAWithNewRoulette(CrowdingGA):
    def getMChildrens(self, M: int) -> list[Agent]:
        res = []
        while len(res) < M:
            parents = self.population.choise(4)
            res += self.reprodaction(choice(parents, 2))
            res += self.reprodaction(choice(parents, 2))
        return res[:M]    
