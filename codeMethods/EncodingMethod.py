import abc

class EncodingMethod(abc.ABC):
    codeLen: int

    @abc.abstractmethod
    def encode(self, point: tuple[float, ...]) -> str: pass

    @abc.abstractmethod
    def decode(self, line: str) -> tuple[float, ...]: pass

    def __init__(self) -> None:
        line = ''.join(str(i%2) for i in range(self.codeLen))
        assert self.encode(self.decode(line)) == line, "encod-decode методы не обратные"
