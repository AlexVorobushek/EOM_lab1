from TargetFunctions.ShekelFoxholeFunction import ShekelFoxholeFunction
from GeneticAlgorithms.ClassicGA import ClassicGA
from GeneticAlgorithms.EliteGA import EliteGA
from GeneticAlgorithms.lab1GA import lab1GA
from codeMethods.GrayEncoding import GrayEncoding
from entity.Population import Population
from settings.GlobalSettings import GlobalSettings
from settings.GASettings.globalGASettings import globalGASettings
from Logger import Logger

import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("init")
    targetFunction = ShekelFoxholeFunction()
    encodingMethod = GrayEncoding()
    startPopulation = Population(encodingMethod, targetFunction)

    geneticAlgorithm = EliteGA(startPopulation)

    logger = Logger(targetFunction, GlobalSettings.realTargetFunctionMinimumPoint)

    print("init completed, start algorithm")

    for epoch in geneticAlgorithm.run(globalGASettings.N_EPOCH):
        logger.log(epoch)
    
    print("completed, drawing")

    logger.draw()
    targetFunction.draw()
    plt.show()
