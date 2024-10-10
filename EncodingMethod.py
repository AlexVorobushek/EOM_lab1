import abc

class EncodingMethod(abc.ABC):
    codeLen: int

    @abc.abstractmethod
    def encode(self, point: tuple): pass

    @abc.abstractmethod
    def decode(self, line: str): pass