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
    
    def choise(self, count: int = 1) -> Agent | list[Agent]:
        self.agents.sort(key=lambda agent: agent.fitness)
        sumFitness = sum(agent.fitness for agent in self)
        probabilityList = [agent.fitness/sumFitness for agent in self]
        scroll = random()
        def rouletteChoiseAgentByScroll(scroll: float) -> Agent:
            resultAgentIndex = 0;
            integrator = probabilityList[0]
            while scroll > integrator+probabilityList[resultAgentIndex+1]:
                resultAgentIndex+=1
                integrator += probabilityList[resultAgentIndex]
            return self.agents[resultAgentIndex]
        if count == 1: return rouletteChoiseAgentByScroll(scroll)
        else: return map(rouletteChoiseAgentByScroll, [(n*(1/count)+scroll)%1 for n in range(count)])
