from codeMethods.EncodingMethod import EncodingMethod
from math import log2, ceil
from numpy import binary_repr

class ClassicEncoding(EncodingMethod):
    def __init__(self, restrictions: tuple[tuple[float, float], ...], steps: tuple[float, ...]) -> None:
        self.restrictions = restrictions
        self.steps = steps
        self.codeLen = sum(ceil(log2((self.restrictions[i][1]-self.restrictions[i][0])/self.steps[i])) for i in range(len(steps)))
        super().__init__()
    
    def encode(self, point: tuple[float, ...]) -> str:
        return ''.join(
            binary_repr(
                round((point[i]-self.restrictions[i][0])/self.steps[i]),
                ceil(log2((self.restrictions[i][1]-self.restrictions[i][0])/self.steps[i]))
            ) for i in range(len(point))
        )
    
    def decode(self, line: str) -> tuple[float, ...]:
        point = []
        for i in range(len(self.steps)):
            abscissaLineLen = ceil(log2((self.restrictions[i][1]-self.restrictions[i][0])/self.steps[i]))
            abscissaLine, line = line[:abscissaLineLen], line[abscissaLineLen:]
            point.append(self.steps[i]*int(abscissaLine, 2)+self.restrictions[i][0])
        return tuple(point)
