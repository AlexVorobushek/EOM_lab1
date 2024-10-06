import abc

class EncodingMetod(abc.ABC):
    @abc.abstractmethod
    def encode(self, point: tuple): pass

    @abc.abstractmethod
    def decode(self, line: str): pass