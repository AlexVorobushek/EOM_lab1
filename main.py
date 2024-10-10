from WeierstrassFunction import WeierstrassFunction
from ClassicEncoding import ClassicEncoding
from Population import Population

import matplotlib.pyplot as plt

def draw(MSEHistory, BFHistory):
    import numpy as np

    x = np.linspace(0, len(MSEHistory), len(MSEHistory))

    plt.figure(1, figsize=(10, 5))
    plt.plot(x, MSEHistory, label='MSE', color='blue')
    plt.plot(x, BFHistory, label='BF', color='red')

    plt.title('Графики MSE и BF')
    plt.xlabel('iteration')
    plt.legend()

if __name__ == "__main__":
    N_ITER, N_POP = 140, 200

    targetFunction = WeierstrassFunction()
    encodingMethod = ClassicEncoding(((-5., 5.), (-5., 5.)), (0.001, 0.001))
    population = Population(encodingMethod, targetFunction, N_POP, .01)

    bestFitness = 10e-8

    MSEHistory = []
    BFHistory = []

    for _ in range(N_ITER):
        population.reproduction(N_POP//4)
        population.genocide()
        population.mutate()

        MSEHistory.append(population.getMSE((0, 0)))
        BFHistory.append(population.getBest().fitness)
    
    draw(MSEHistory, BFHistory)
    targetFunction.draw()
    plt.show()
