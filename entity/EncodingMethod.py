import abc
from math import log2, ceil


class EncodingMethod(abc.ABC):
    codeLen: int

    @abc.abstractmethod
    def encode(self, point: tuple[float, ...]) -> str: pass

    @abc.abstractmethod
    def decode(self, line: str) -> tuple[float, ...]: pass

    @abc.abstractmethod
    def decodeCoordinate(self, coorValue: str, coorIndex: int): pass

    @abc.abstractmethod
    def codeCoordinate(self, coorValue: float, coorIndex: int): pass

    def __init__(self) -> None:
        line = ''.join(str(i%2) for i in range(self.codeLen))
        assert self.encode(self.decode(line)) == line, "encod-decode методы не обратные"
    
    def decode(self, line: str) -> tuple[float, ...]:
        point = []
        index = 0
        for i in range(len(self.steps)):
            abscissaLineLen = ceil(log2((self.restrictions[i][1] - self.restrictions[i][0]) / self.steps[i]))
            code_segment = line[index:index + abscissaLineLen]
            index += abscissaLineLen
            point.append(self.decodeCoordinate(code_segment, i))
        
        return tuple(point)
    
    def encode(self, point: tuple) -> str:
        gray_code = []
        for i in range(len(point)):
            gray_code.append(self.codeCoordinate(point[i], i))
        return ''.join(gray_code)
    
