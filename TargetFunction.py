import abc
import matplotlib.pyplot as plt
import numpy as np

class TargetFunction(abc.ABC):
    @abc.abstractmethod
    def getValue(self, point: tuple, **args): pass

    def draw(self):
        # Создаем сетку значений x и y
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        x, y = np.meshgrid(x, y)

        # Вычисляем значения z для каждой точки сетки
        z = np.array([[self.getValue((xi, yi)) for xi, yi in zip(x_row, y_row)] for x_row, y_row in zip(x, y)])

        # Создаем фигуру и оси
        fig = plt.figure(2)
        ax = fig.add_subplot(111, projection='3d')

        # Строим поверхность
        ax.plot_surface(x, y, z, cmap='viridis')

        # Добавляем подписи
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Целевая функция')


    def getPointFitness(self, point):
        return -self.getValue(point)
