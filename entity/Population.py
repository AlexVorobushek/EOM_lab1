from entity.EncodingMethod import EncodingMethod
from entity.Agent import Agent
from entity.TargetFunction import TargetFunction
from settings import PopulationSettings
from settings import TargetSettings
from random import random, choice, randint

class Population(PopulationSettings, TargetSettings):
    def __init__(self, encodingMethod: EncodingMethod, targetFunction: TargetFunction):
        self.agents: list[Agent] = [Agent(encodingMethod, targetFunction) for _ in range(self.populationCount)]
        self.targetFunction = targetFunction
        self.encodingMethod = encodingMethod
    
    def mutate(self):
        roulette = lambda: random() < self.mutateProbability
        self.agents = list(map(lambda x: x if not roulette() else x.mutate(), self.agents))

    def genocide(self):
        self.agents.sort(key=lambda x: x.fitness)
        # self.agents = sorted(self.agents, key=lambda x: x.fitness)
        while len(self.agents) > self.populationCount:
            self.agents.pop(randint(0, len(self.agents)//2))
    
    def __getRandomAgent(self) -> Agent:
        return choice(self.agents)
    
    def reproduction(self):
        for i in range(self.reproductionPairsCount):
            self.agents += self.__getRandomAgent() + self.__getRandomAgent()

    def getMSE(self, realAnswer: tuple[float, ...]) -> float:
        realAnsAgent = Agent(self.encodingMethod, self.targetFunction, point=realAnswer)
        return sum(map(lambda x: (x.fitness-realAnsAgent.fitness), self.agents))/len(self.agents)
    
    def getBest(self) -> Agent:
        return max(self.agents, key=lambda x: x.fitness)
