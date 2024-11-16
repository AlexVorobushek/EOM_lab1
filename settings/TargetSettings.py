import abc

class TargetSettings(abc.ABC):
    restrictions: tuple[tuple[float, float], ...] = ((-50., 50.),
                                                     (-50., 50.))
    steps:  tuple[float, float] = (10e-1, 10e-1)