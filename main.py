print("start init")
from TargetFunctions.ShekelFoxholeFunction import ShekelFoxholeFunction
from GeneticAlgorithms.ClassicGA import ClassicGA
from GeneticAlgorithms.EliteGA import EliteGA
from GeneticAlgorithms.Elite2GA import Elite2GA
from GeneticAlgorithms.lab1GA import lab1GA
from GeneticAlgorithms.AreaRankGA import AreaRankGA
from GeneticAlgorithms.CrowdingGA import CrowdingGA
from GeneticAlgorithms.CrowdingGAWithNewRoulette import CrowdingGAWithNewRoulette
from codeMethods.GrayEncoding import GrayEncoding
from codeMethods.ClassicEncoding import ClassicEncoding
from entity.Population import Population
from settings.GlobalSettings import AnswerSettings
from settings.GASettings.globalGASettings import globalGASettings
from Logger import Logger
from progress.bar import IncrementalBar
from TeoryOfProbability import Data

import matplotlib.pyplot as plt

def roulettePresentation(population: Population):
    import matplotlib.pyplot as plt

    classicRouletteXList: list[float] = []
    for _ in range(400): 
        classicRouletteXList.append(population.choise().point[0])
    newRouletteXList: list[float] = []
    for _ in range(100): 
        newRouletteXList.extend(
            map(
                lambda agent: agent.point[0],
                population.choise(4)
            )
        )
    
    # https://github.com/AlexVorobushek/Teory-of-probability
    data = Data(dataList=classicRouletteXList)
    interval_count = 20 # сколько колонок
    ISS = data.getISS(interval_count)
    plt = data.drawGistByISS(
        ISS,
        xLabel="X",
        yLabel="частота встречания X",
        label="распределение X после рулетки",
        title="классическая рулетка"
    )
    plt.show()

    data = Data(dataList=newRouletteXList)
    ISS = data.getISS(interval_count)
    plt = data.drawGistByISS(
        ISS,
        xLabel="X",
        yLabel="частота встречания X",
        label="распределение X после рулетки",
        title="модифицированная рулетка"
    )
    plt.show()

if __name__ == "__main__":
    targetFunction = ShekelFoxholeFunction()
    encodingMethod = GrayEncoding()
    startPopulation = Population(encodingMethod, targetFunction)
    geneticAlgorithm = CrowdingGA(startPopulation)

    # roulettePresentation(startPopulation)

    logger = Logger(targetFunction, AnswerSettings.realTargetFunctionMinimumPoint)

    print("init completed, start algorithm")
    bar = IncrementalBar('epochs', max =globalGASettings.N_EPOCH)

    for epoch in geneticAlgorithm.run(globalGASettings.N_EPOCH):
        bar.next()
        logger.log(epoch)

    bar.finish()
    
    print("completed, drawing")

    logger.draw()
    # targetFunction.draw()
    plt.show()
