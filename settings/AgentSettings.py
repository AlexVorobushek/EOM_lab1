import abc

class AgentSettings(abc.ABC):
    crossSeparation: list[float] = [0.33, 0.66]
