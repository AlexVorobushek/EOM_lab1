from entity.EncodingMethod import EncodingMethod
from entity.Agent import Agent
from entity.TargetFunction import TargetFunction
from settings.populationSettings import PopulationSettings
from settings.TargetSettings import TargetSettings
from random import random, choice, randint

class Population(PopulationSettings, TargetSettings):
    def __init__(self, encodingMethod: EncodingMethod, targetFunction: TargetFunction):
        self.agents: list[Agent] = [Agent(encodingMethod, targetFunction) for _ in range(self.populationCount)]
        self.targetFunction = targetFunction
        self.encodingMethod = encodingMethod

    def getMSE(self, realAnswer: tuple[float, ...]) -> float:
        realAnsAgent = Agent(self.encodingMethod, self.targetFunction, point=realAnswer)
        return sum(map(lambda x: (x.fitness-realAnsAgent.fitness), self.agents))/len(self.agents)
    
    def getBest(self) -> Agent:
        return max(self.agents, key=lambda x: x.fitness)
    
    def __iter__(self):
        return iter(self.agents)
    
    def __getitem__(self, key) -> Agent:
        return self.agents[key]
