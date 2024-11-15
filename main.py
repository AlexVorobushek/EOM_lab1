from TargetFunctions.ShekelFoxholeFunction import ShekelFoxholeFunction
from GeneticAlgorithms.ClassicGA import ClassicGA
from codeMethods.GrayEncoding import GrayEncoding
from entity.Population import Population
from Logger import Logger

import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("start init")

    N_EPOCH = 150

    targetFunction = ShekelFoxholeFunction()
    encodingMethod = GrayEncoding()
    startPopulation = Population(encodingMethod, targetFunction)

    geneticAlgorithm = ClassicGA(targetFunction, startPopulation, encodingMethod)

    logger = Logger(targetFunction, (0., 0.))

    print("init completed, start algorithm")

    for epoch in range(N_EPOCH):
        logger.log(
            geneticAlgorithm.runOneEpoch()
        )
    
    print("completed, drawing")

    logger.draw()
    targetFunction.draw()
    plt.show()
