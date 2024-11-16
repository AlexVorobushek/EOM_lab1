import abc

class lab1GASettings(abc.ABC):
    reproductionPairsCount: int = 4 # сколько пар будет отбираться для размножения в каждой эпохе
