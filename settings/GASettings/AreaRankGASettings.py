import abc

class AreaRankGASettings(abc.ABC):
    R: int = 2  # число особей, которые должны выжить после геноцида
    areaRadius: float = 5.;
    
