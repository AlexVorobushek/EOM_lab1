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
    
    def encode(self, point: tuple) -> str:
        gray_code = []
        for i in range(len(point)):
            value = round((point[i] - self.restrictions[i][0]) / self.steps[i])
            abscissaLineLen = ceil(log2((self.restrictions[i][1] - self.restrictions[i][0]) / self.steps[i]))
            gray_value = self.to_gray(value)
            gray_code.append(binary_repr(gray_value, width=abscissaLineLen))
        return ''.join(gray_code)
    
    def decode(self, line: str) -> tuple[float, ...]:
        point = []
        index = 0
        for i in range(len(self.steps)):
            abscissaLineLen = ceil(log2((self.restrictions[i][1] - self.restrictions[i][0]) / self.steps[i]))
            gray_code_segment = line[index:index + abscissaLineLen]
            index += abscissaLineLen
            
            gray_value = int(gray_code_segment, 2)
            value = self.from_gray(gray_value)
            point.append(self.steps[i] * value + self.restrictions[i][0])
        
        return tuple(point)

    def to_gray(self, num: int) -> int:
        return num ^ (num >> 1)

    def from_gray(self, gray: int) -> int:
        num = gray
        shift = 1
        while (gray >> shift) > 0:
            num ^= (gray >> shift)
            shift += 1
        return num
