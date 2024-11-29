import abc

class PopulationSettings(abc.ABC):
    populationCount: int = 100
    mutateProbability: float = 0
