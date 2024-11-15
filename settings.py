import abc

class AgentSettings(abc.ABC):
    crossSeparation: int = None # None, чтобы делить пополам. В ином случае отсчитывать кол-во битов

class PopulationSettings(abc.ABC):
    populationCount: int = 15
    reproductionPairsCount: int = 4 # сколько пар будет отбираться для размножения в каждой эпохе
    mutateProbability: float = 10e-2

class TargetSettings(abc.ABC):
    restrictions: tuple[tuple[float, float], ...] = ((-50., 50.),
                                                     (-50., 50.))
    steps:  tuple[float, float] = (10e-1, 10e-1)
