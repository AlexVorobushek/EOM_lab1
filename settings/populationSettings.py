import abc

class PopulationSettings(abc.ABC):
    populationCount: int = 15
    mutateProbability: float = 10e-2
