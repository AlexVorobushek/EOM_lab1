from entity.EncodingMethod import EncodingMethod
from settings.TargetSettings import TargetSettings
from math import log2, ceil
from numpy import binary_repr

class ClassicEncoding(EncodingMethod, TargetSettings):
    def __init__(self) -> None:
        self.steps = [
            (self.restrictions[i][1] - self.restrictions[i][0]) / 2**ceil(log2((self.restrictions[i][1] - self.restrictions[i][0]) / self.steps[i]))
            for i in range(len(self.steps))
        ]
        self.codeLen = sum(ceil(log2((self.restrictions[i][1]-self.restrictions[i][0])/self.steps[i])) for i in range(len(self.steps)))
        super().__init__()
    
    def encode(self, point: tuple[float, ...]) -> str:
        return ''.join(
            binary_repr(
                round((point[i]-self.restrictions[i][0])/self.steps[i]),
                ceil(log2((self.restrictions[i][1]-self.restrictions[i][0])/self.steps[i]))
            ) for i in range(len(point))
        )

    def codeCoordinate(self, coorValue: float, coorIndex: int):
        return binary_repr(
                round((coorValue-self.restrictions[coorIndex][0])/self.steps[coorIndex]),
                ceil(log2((self.restrictions[coorIndex][1]-self.restrictions[coorIndex][0])/self.steps[coorIndex]))
            )
    
    def decodeCoordinate(self, coorValue: str, coorIndex: int):
        return self.steps[coorIndex]*int(coorValue, 2)+self.restrictions[coorIndex][0]