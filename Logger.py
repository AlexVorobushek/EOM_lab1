from Population import Population
import matplotlib.pyplot as plt
import numpy as np

class Logger:
    MSEHistory = []
    BFHistory = []

    def __init__(self, population: Population, realTargetFunctionMin: tuple[float, ...] = None) -> None:
        self.population = population
        self.isTest = bool(realTargetFunctionMin)
        self.realTargetFunctionMin = realTargetFunctionMin
    
    def log(self) -> None:
        if self.isTest: self.MSEHistory.append(self.population.getMSE((0, 0)))
        self.BFHistory.append(self.population.getBest().fitness)
    
    def draw(self) -> None:
        x = np.linspace(0, len(self.BFHistory), len(self.BFHistory))

        plt.figure(1, figsize=(10, 5))
        if self.isTest: plt.plot(x, self.MSEHistory, label='MSE', color='blue')
        plt.plot(x, self.BFHistory, label='BF', color='red')

        plt.title('Графики MSE и BF' if self.isTest else 'График BF')
        plt.xlabel('iteration')
        plt.legend()