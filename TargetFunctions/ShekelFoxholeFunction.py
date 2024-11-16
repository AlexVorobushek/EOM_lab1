from entity.TargetFunction import TargetFunction
from settings.TargetSettings import TargetSettings
import numpy as np

class ShekelFoxholeFunction(TargetFunction, TargetSettings):
    '''
    Функция лисьей норы Шекеля

    Точка минимума:
    x* = [-32, ..., -32]
    f(x*) ≈ 1
    '''
    def __init__(self, K: int = 500, a: np.ndarray = np.array([
        [-32, -16, 0, 16, 32]*5,
        [-32]*5 + [-16]*5 + [0]*5 + [16]*5 + [32]*5
    ])) -> None:
        # Матрица a определяет параметры функции
        self.K = K
        self.a = a
        self.m = a.shape[1]  # количество столбцов в a, обычно 5

    def getValue(self, point: tuple) -> float:
        S = sum((1 / (j + (point[0]-self.a[0, j-1])**6 + (point[1]-self.a[1, j-1])**6)) for j in range(1, 25+1))
        return 1/(1/self.K + S)
    
    def draw(self):
        return super().draw(self.restrictions, self.steps)
