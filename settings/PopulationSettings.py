import abc

class PopulationSettings(abc.ABC):
    populationCount: int = 15
    reproductionPairsCount: int = 4 # сколько пар будет отбираться для размножения в каждой эпохе
    mutateProbability: float = 10e-2
