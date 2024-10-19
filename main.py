from WeierstrassFunction import WeierstrassFunction
from codeMethods.ClassicEncoding import ClassicEncoding
from codeMethods.GrayEncoding import GrayEncoding
from Population import Population
from Logger import Logger

import matplotlib.pyplot as plt

if __name__ == "__main__":
    N_ITER = 150

    targetFunction = WeierstrassFunction()
    encodingMethod = GrayEncoding(((-5., 5.), (-5., 5.)), (10e-4, 10e-4))
    population = Population(encodingMethod, targetFunction)

    logger = Logger(targetFunction, (0., 0.))

    for _ in range(N_ITER):
        population.reproduction()
        population.genocide()
        population.mutate()

        logger.log(population)
    
    logger.draw()
    targetFunction.draw()
    plt.show()
