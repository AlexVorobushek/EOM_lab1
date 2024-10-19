from codeMethods.EncodingMethod import EncodingMethod
from TargetFunction import TargetFunction
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

        self.crossSeparation = self.crossSeparation if self.crossSeparation != None else len(self.line)//2
        self.encodingMethod = encodingMethod
        self.targetFunction = targetFunction

    def __add__(self, other: 'Agent') -> list['Agent', 'Agent']:
        return [Agent(
                    self.encodingMethod,
                    self.targetFunction,
                    line=self.line[:self.crossSeparation]+other.line[self.crossSeparation:]
                ), \
                Agent(
                    self.encodingMethod,
                    self.targetFunction,
                    line=other.line[:self.crossSeparation]+self.line[self.crossSeparation:]
                )]

    def mutate(self) -> 'Agent':
        randomBitIndex = random.randint(0, len(self.line)-1)
        newLineAsList = list(self.line)
        newLineAsList[randomBitIndex] = str(int(not bool(int(newLineAsList[randomBitIndex]))))
        self.__init__(self.encodingMethod, self.targetFunction, line=''.join(newLineAsList))
        return self
