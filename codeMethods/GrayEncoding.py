from entity.EncodingMethod import EncodingMethod
from settings.TargetSettings import TargetSettings
from math import log2, ceil
from numpy import binary_repr

class GrayEncoding(EncodingMethod, TargetSettings):
    def __init__(self) -> None:
        self.steps = [
            (self.restrictions[i][1] - self.restrictions[i][0]) / 2**ceil(log2((self.restrictions[i][1] - self.restrictions[i][0]) / self.steps[i]))
            for i in range(len(self.steps))
        ]
        self.codeLen = sum(ceil(log2((self.restrictions[i][1]-self.restrictions[i][0])/self.steps[i])) for i in range(len(self.steps)))
        super().__init__()
    
    def codeCoordinate(self, coorValue: float, coorIndex: int):
        value = round((coorValue - self.restrictions[coorIndex][0]) / self.steps[coorIndex])
        abscissaLineLen = ceil(log2((self.restrictions[coorIndex][1] - self.restrictions[coorIndex][0]) / self.steps[coorIndex]))
        gray_value = self.to_gray(value)
        return binary_repr(gray_value, width=abscissaLineLen)
    
    def decodeCoordinate(self, coorValue: str, coorIndex: int):            
        gray_value = int(coorValue, 2)
        value = self.from_gray(gray_value)
        return self.steps[coorIndex] * value + self.restrictions[coorIndex][0]

    def to_gray(self, num: int) -> int:
        return num ^ (num >> 1)

    def from_gray(self, gray: int) -> int:
        num = gray
        shift = 1
        while (gray >> shift) > 0:
            num ^= (gray >> shift)
            shift += 1
        return num
