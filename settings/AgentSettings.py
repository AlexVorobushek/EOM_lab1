import abc

class AgentSettings(abc.ABC):
    crossSeparation: int = None # None, чтобы делить пополам. В ином случае отсчитывать кол-во битов
