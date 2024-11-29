from entity.EncodingMethod import EncodingMethod
from entity.TargetFunction import TargetFunction
from settings.AgentSettings import AgentSettings
import random

class Agent(AgentSettings):
    def __init__(self, encodingMethod: EncodingMethod, targetFunction: TargetFunction, point: tuple=None, line:str=None) -> None:
        if point:
            self.point = point
            self.line = encodingMethod.encode(point)
            self.fitness = targetFunction.getPointFitness(point)
        elif line:
            self.point = encodingMethod.decode(line)
            self.line = line
            self.fitness = targetFunction.getPointFitness(self.point)
        else:
            line = ''.join(str(random.randint(0, 1)) for i in range(encodingMethod.codeLen))
            self.point = encodingMethod.decode(line)
            self.line: str = line
            self.fitness = targetFunction.getPointFitness(self.point)

        self.encodingMethod = encodingMethod
        self.targetFunction = targetFunction
    
    @staticmethod
    def __binInvert(a: str):
        mask = (1 << len(a)) - 1
        inverted_num = int(a, 2) ^ mask
        return normal_bin(inverted_num, len(a))
    
    @staticmethod
    def __binOr(a: str, b: str):
        return normal_bin(int(a, 2)|int(b, 2), len(a))
    
    @staticmethod
    def __binAnd(a: str, b: str):
        return normal_bin(int(a, 2)&int(b, 2), len(a))
    
    def __generateMasks(self, maskLen: int):
        maskA = "".join([str(int(len(list(filter(lambda x: x < (i/maskLen), self.crossSeparation)))%2)) for i in range(maskLen)])
        maskB = self.__binInvert(maskA)
        return maskA, maskB


    def __add__(self, other: 'Agent') -> list['Agent', 'Agent']:
        P1X = self.encodingMethod.codeCoordinate(self.point[0], 0) # parent 1 x line
        maskA, maskB = self.__generateMasks(len(P1X))
        P1Xa, P1Xb = self.__binAnd(maskA, P1X), self.__binAnd(maskB, P1X)
        print(P1X)
        print(maskA, maskB)
        print(P1Xa, P1Xb)
        print("-------------------")

        P1Y = self.encodingMethod.codeCoordinate(self.point[1], 1) # parent 1 y line
        maskA, maskB = self.__generateMasks(len(P1Y))
        P1Ya, P1Yb = self.__binAnd(maskA, P1Y), self.__binAnd(maskB, P1Y)

        P2X = self.encodingMethod.codeCoordinate(other.point[0], 0) # parent 2 x line
        maskA, maskB = self.__generateMasks(len(P2X))
        P2Xa, P2Xb = self.__binAnd(maskA, P2X), self.__binAnd(maskB, P2X)

        P2Y = self.encodingMethod.codeCoordinate(other.point[1], 1) # parent 2 y line
        maskA, maskB = self.__generateMasks(len(P2Y))
        P2Ya, P2Yb = self.__binAnd(maskA, P2Y), self.__binAnd(maskB, P2Y)

        C1X = self.__binOr(P1Xa, P2Xb) # children 1 x line
        C1Y = self.__binOr(P1Ya, P2Yb) # children 1 y line
        C1 = [self.encodingMethod.decodeCoordinate(C1X, 0), self.encodingMethod.decodeCoordinate(C1Y, 1)]

        C2X = self.__binOr(P1Xb, P2Xa) # children 1 x line
        C2Y = self.__binOr(P1Yb, P2Ya) # children 1 y line
        C2 = [self.encodingMethod.decodeCoordinate(C2X, 0), self.encodingMethod.decodeCoordinate(C2Y, 1)]

        return [Agent(
                    self.encodingMethod,
                    self.targetFunction,
                    point=C1
                ), \
                Agent(
                    self.encodingMethod,
                    self.targetFunction,
                    point=C2
                )]

    def mutate(self) -> 'Agent':
        randomBitIndex = random.randint(0, len(self.line)-1)
        newLineAsList = list(self.line)
        newLineAsList[randomBitIndex] = str(int(not bool(int(newLineAsList[randomBitIndex]))))
        self.__init__(self.encodingMethod, self.targetFunction, line=''.join(newLineAsList))
        return self


def normal_bin(number: int, len: int):
    binary_str = bin(number)[2:]
    padded_binary_str = binary_str.zfill(len)
    return padded_binary_str