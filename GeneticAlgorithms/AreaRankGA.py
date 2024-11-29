from GeneticAlgorithms.ClassicGA import ClassicGA
from entity.TargetFunction import TargetFunction
from entity.Population import Population
from entity.EncodingMethod import EncodingMethod
from entity.GeneticAlgorithm import GeneticAlgorithm
from random import random
from entity.Agent import Agent
from settings.GASettings.AreaRankGASettings import AreaRankGASettings

class AreaRankGA(ClassicGA, AreaRankGASettings):
    def __getAreasAgents(self) -> list[list[Agent]]:
        distance = lambda agent1, agent2: ((agent1.point[0]-agent2.point[0])**2+(agent1.point[1]-agent2.point[1])**2)**0.5
        result = [
            list(filter(
                lambda agent: distance(agent, centerAgent) < self.areaRadius,
                self.population
            ))
            for centerAgent in self.population
        ]
        return result

    def __genocide(self) -> dict[str, list[Agent]]:
        agentsToDelete = set()
        for areasAgents in self.__getAreasAgents():
            areasAgents.sort(key=lambda agent: agent.fitness, reverse=True)
            agentsToDelete |= set(areasAgents[self.R:])
        result = {
            True: list(set(self.population.agents)-agentsToDelete),
            False: list(agentsToDelete)
        }
        return result
    
    def runOneEpoch(self) -> Population:
        filtered = self.__genocide()
        self.population.agents = filtered[True]
        self.population.agents = self.newBreed()
        self.mutate()
        return self.population
    
    def run(self, epochCount):
        self.__drawFiltration(self.__genocide())
        return super().run(epochCount)
    
    def __drawFiltration(self, filtration: dict[bool, Agent]):
        import numpy as np
        import matplotlib.pyplot as plt

        plt.figure(4, figsize=(10, 10))

        # Создаем сетку значений x и y
        targetFunction = self.population.targetFunction
        xRange, yRange = targetFunction.restrictions
        x = np.linspace(*xRange, int((xRange[1]-xRange[0])/targetFunction.steps[0]))
        y = np.linspace(*yRange, int((yRange[1]-yRange[0])/targetFunction.steps[1]))
        x, y = np.meshgrid(x, y)

        # Вычисляем значения z для каждой точки сетки
        z = np.array([[targetFunction.getValue((xi, yi)) for xi, yi in zip(x_row, y_row)] for x_row, y_row in zip(x, y)])

        cont = plt.contour(x, y, z, levels=3, cmap='viridis')
        plt.clabel(cont)

        px = [agent.point[0] for agent in filtration[True]]
        py = [agent.point[1] for agent in filtration[True]]
        plt.scatter(px, py, color='blue', label='Initial Population', s=20)

        px = [agent.point[0] for agent in filtration[False]]
        py = [agent.point[1] for agent in filtration[False]]
        plt.scatter(px, py, color='black', label='Cleaned Population', s=30)


        plt.grid()
        # plt.plot(self.avgR)
        # plt.xlabel('iteration')
        # plt.ylabel('avgR(iteration)')

