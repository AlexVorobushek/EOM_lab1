from EncodingMetod import EncodingMetod
from TargetFunction import TargetFunction

class Agent:
    def __init__(self, encodingMethod: EncodingMetod, targetFunction: TargetFunction, point: tuple, crossSeparation: int = None) -> None:
        self.point = point
        self.line = encodingMethod.encode(point)
        self.fitness = targetFunction.getPointFitness(point)

        self.crossSeparation = crossSeparation if crossSeparation != None else (line)//2 
        self.encodingMetod = encodingMethod
        self.targetFunction = targetFunction

    def __init__(self, encodingMethod: EncodingMetod, targetFunction: TargetFunction, line: str, crossSeparation: int = None) -> None:
        self.point = encodingMethod.decode(line)
        self.line = line
        self.fitness = targetFunction.getPointFitness(self.point)

        self.crossSeparation = crossSeparation if crossSeparation != None else (line)//2
        self.encodingMetod = encodingMethod
        self.targetFunction = targetFunction

    def __add__(self, other: 'Agent') -> tuple['Agent', 'Agent']:
        return Agent(
                    self.encodingMetod,
                    self.targetFunction,
                    self.line[:self.crossSeparation]+other.line[self.crossSeparation:]
                ), \
                Agent(
                    self.encodingMetod,
                    self.targetFunction,
                    self.line[self.crossSeparation:]+other.line[:self.crossSeparation]
                )
