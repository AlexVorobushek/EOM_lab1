from GeneticAlgorithms.ClassicGA import ClassicGA
from settings.GASettings.CrowdingGASettings import CrowdingGASettings
from random import shuffle
from entity.Agent import Agent

class CrowdingGA(ClassicGA, CrowdingGASettings):
    def getMChildrens(self, M: int) -> list[Agent]:
        res = []
        while len(res) < M:
            res += self.reprodaction(self.getPairForReprodaction())
        return res[:M]

    def newBreed(self) -> list[Agent]:
        newBreed = self.population.agents
        MChildrens = self.getMChildrens(M = self.M)
        dist = lambda agent1, agent2: ((agent1.point[0] - agent2.point[0])**2 + (agent1.point[1] - agent2.point[1])**2)**0.5
        for children in MChildrens:
            distToChildren = lambda agent1: dist(agent1, children)
            shuffle(newBreed)
            RandomCfParrents = newBreed[:self.Cf]
            parrentToReplase = min(RandomCfParrents, key=distToChildren)
            if parrentToReplase.fitness < children.fitness:
                newBreed[newBreed.index(parrentToReplase)] = children
        return newBreed
        

