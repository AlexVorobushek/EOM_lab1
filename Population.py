from EncodingMethod import EncodingMethod
from Agent import Agent
from TargetFunction import TargetFunction
from random import random, choice, randint

class Population:
    def __init__(self, encodingMethod: EncodingMethod, targetFunction: TargetFunction, N: int, mutateProbability: float):
        self.agents: list[Agent] = [Agent(encodingMethod, targetFunction) for _ in range(N)]
        self.mutateProbability = mutateProbability
        self.targetFunction = targetFunction
        self.encodingMethod = encodingMethod
        self.N = N
    
    def mutate(self):
        roulette = lambda: random() < self.mutateProbability
        self.agents = list(map(lambda x: x if roulette() else x.mutate(), self.agents))

    def genocide(self):
        self.agents.sort(key=lambda x: x.fitness)
        while len(self.agents) > self.N:
            self.agents.pop(randint(0, len(self.agents)//2))
    
    def __getRandomAgent(self) -> Agent:
        return choice(self.agents)
    
    def reproduction(self, PairsN):
        for i in range(PairsN):
            self.agents += self.__getRandomAgent() + self.__getRandomAgent()

    def getMSE(self, realAnswer: tuple[float, ...]) -> float:
        realAnsAgent = Agent(self.encodingMethod, self.targetFunction, point=realAnswer)
        return sum(map(lambda x: (x.fitness-realAnsAgent.fitness), self.agents))/len(self.agents)
    
    def getBest(self) -> Agent:
        return max(self.agents, key=lambda x: x.fitness)
