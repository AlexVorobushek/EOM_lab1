from entity.Population import Population
import matplotlib.pyplot as plt
import numpy as np
from entity.TargetFunction import TargetFunction

class Logger:
    avgF = []
    avgX = []
    avgY = []

    MSEF = []
    MSEX = []
    MSEY = []
    
    bestF = []
    avgR = []

    def __init__(self, targetFunction: TargetFunction, realTargetFunctionMin: tuple[float, ...] = None) -> None:
        self.realTargetFunctionMin = realTargetFunctionMin
        self.isTest = bool(realTargetFunctionMin)
        self.targetFunction = targetFunction
    
    def log(self, population: Population) -> None:
        self.avgF.append(np.mean(list(map(lambda agent: self.targetFunction.getValue(agent.point), population.agents))))
        self.avgX.append(np.mean(list(map(lambda agent: agent.point[0], population.agents))))
        self.avgY.append(np.mean(list(map(lambda agent: agent.point[1], population.agents))))
        
        self.MSEF.append(np.mean(list(map(
            lambda agent: (self.targetFunction.getValue(agent.point) - self.targetFunction.getValue(self.realTargetFunctionMin))**2,
            population.agents
        ))))
        self.MSEX.append(np.mean(list(map(
            lambda agent: (agent.point[0] - self.realTargetFunctionMin[0])**2,
            population.agents
        ))))
        self.MSEY.append(np.mean(list(map(
            lambda agent: (agent.point[1] - self.realTargetFunctionMin[1])**2,
            population.agents
        ))))

        self.bestF.append(self.targetFunction.getValue(population.getBest().point))
        self.avgR.append(self.getAvgR(population))

    def draw(self) -> None:
        plt.figure(1, figsize=(10, 5))

        ### avg

        plt.subplot(3, 2, 1)
        plt.plot(self.avgF, label='avg of target function', color='blue')
        plt.title('avg of target function, best agent function value')
        plt.xlabel('iteration')
        plt.ylabel('F(iteration)')
        plt.plot(self.bestF, label='best agent function value', color='red')
        plt.legend()

        plt.subplot(3, 2, 3)
        plt.plot(self.avgX)
        plt.title('avg of x')
        plt.xlabel('iteration')
        plt.ylabel('avgX(iteration)')

        plt.subplot(3, 2, 5)
        plt.plot(self.avgY)
        plt.title('avg of y')
        plt.xlabel('iteration')
        plt.ylabel('avgY(iteration)')

        ### MSE

        plt.subplot(3, 2, 2)
        plt.plot(self.MSEF)
        plt.title('MSE of target function')
        plt.xlabel('iteration')
        plt.ylabel('MSEF(iteration)')

        plt.subplot(3, 2, 4)
        plt.plot(self.MSEX)
        plt.title('MSE of x')
        plt.xlabel('iteration')
        plt.ylabel('MSEX(iteration)')

        plt.subplot(3, 2, 6)
        plt.plot(self.MSEY)
        plt.title('MSE of y')
        plt.xlabel('iteration')
        plt.ylabel('MSEY(iteration)')

        plt.tight_layout()

        # plt.figure(3, figsize=(10, 5))
        # plt.subplot()
        # plt.plot(self.avgR)
        # plt.title('среднее расстояние между агентами')
        # plt.xlabel('iteration')
        # plt.ylabel('avgR(iteration)')

    def getAvgR(self, population: Population):
        sumR = 0
        for i in population:
            for j in population:
                if i!=j: sumR += ((i.point[0]-j.point[0])**2 + (i.point[1]-j.point[1])**2)**0.5
        return sumR/population.populationCount