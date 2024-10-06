from TargetFunction import TargetFunction
from math import cos, pi


class WeierstrassFunction(TargetFunction):
    '''
    функция Вейерштрасса

    точка минимума:
    point* == 0
    f(point*) == 0
    '''
    def __init__(self, k_max: int = 20, a: float = 0.5, b: int = 3) -> None:
        self.k_max = k_max
        self.a = a
        self.b = b

    def getValue(self, point: tuple):
        n = len(point)
        return sum(sum(self.a**k*cos(2*pi*self.b**k*(i+0.5)) for k in range(0, self.k_max+1)) for i in point) - \
    n*sum(self.a**k*cos(pi*self.b**k) for k in range(0, self.k_max+1))
