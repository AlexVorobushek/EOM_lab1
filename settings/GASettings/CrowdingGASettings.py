import abc
from settings.populationSettings import PopulationSettings as ps

class CrowdingGASettings(abc.ABC):
    Cf = 3 # число отобранных родителей
    M = ps.populationCount // 10 # число отобранных детей   
