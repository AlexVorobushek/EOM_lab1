import matplotlib.pyplot as plt
from pprint import pprint
from math import ceil
import numpy as np


class Data:
    def __init__(self, dataFileName="data.txt", dataList=False) -> None:
        self.TYPE = "int"
        if not dataList: self.loadFromFile(dataFileName)  # self.data - вариационный ряд
        else: self.data = sorted(dataList)
        self.N = len(self.data)
        
    def loadFromFile(self, dataFileName):
        with open(dataFileName, "r") as file:
            match self.TYPE:
                case "int":
                    self.data = sorted(map(int, file.read().split()))
                case "float":
                    self.data = sorted([x[0]+x[1]/100 for x in map(lambda i: list(map(int, i.split("."))), file.read().split())])
            
    def getSS(self) -> dict:  # статистический ряд
        res = dict()
        for item in self.data:
            res[item] = res.get(item, 0) + 1
        return res
    
    def getISS(self, interval_count: int) -> dict:  # интервальный статистический ряд
        delta = self.__getDelta(interval_count)
        def getKey(item) -> tuple:
            return (item-(item-self.data[0])%delta, item-(item-self.data[0])%delta+delta)
        
        # res = dict.fromkeys([getKey(item) for item in range(self.data[0], self.data[-1], delta)], 0)
        res=dict()
            
        for item in self.data:
            key = getKey(item)
            res[key] = res.get(key, 0) + 1
        return res

    def getM(self) -> float:  # математическое ожидание
        return sum(self.data)/len(self.data)
    
    def getD(self) -> float: # дисперсия
        M = self.getM()
        return sum([(M-val)**2 for val in self.data])/len(self.data)
    
    def drawGistByISS(self, ISS: dict, xLabel=None, yLabel=None, title=None, label=None):
        X, Y = reformingSSToXY(ISS).values()
        
        delta = X[0][1]-X[0][0]
        X = list(map(str, X))
        Y = list(map(lambda item: item/(self.N*delta), Y))
        
        plt.delaxes()
        plt.bar(X, Y)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(title)
        plt.legend()
        
        return plt
    
    def __getDelta(self, interval_count: int):
        match self.TYPE:
            case "int":
                return ceil((self.data[-1] - self.data[0] + 1)/interval_count)
            case "float":
                return ceil((self.data[-1]*100 - self.data[0]*100 + 1)/interval_count)/100
        
        
def reformingSSToXY(result : dict) -> dict:
        res = {"X": [], "Y": []}
        for x, y in result.items():
            res["X"].append(x)
            res["Y"].append(y)
        return res


def draw(x : list, y : list, fileName : str, xLabel=None, yLabel=None, title=None, label=None) -> None:
        plt.delaxes()
        plt.bar(x, y, label=label)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(title)
        plt.legend()
        plt.savefig(fileName)


if __name__ == "__main__":
    datal = Data(dataList=[-24.21875, -45.3125, -2.34375, 10.9375, -49.21875, 12.5, 15.625, -13.28125, 10.15625, 27.34375, 7.03125, 17.1875, -28.125, 26.5625, -31.25, -42.1875, 9.375, -14.0625, -20.3125, -20.3125, 43.75, -17.96875, -42.1875, -19.53125, -48.4375, 17.1875, -20.3125, -41.40625, -23.4375, 12.5, -17.1875, -2.34375, 2.34375, 43.75, -35.9375, -46.875, 25.0, 12.5, 21.09375, -18.75, 2.34375, 21.09375, -30.46875, -29.6875, -14.0625, -13.28125, -23.4375, 26.5625, -50.0, -2.34375, 47.65625, -49.21875, -45.3125, 15.625, -34.375, 39.84375, 26.5625, -10.15625, -42.1875, 14.0625, -44.53125, 39.0625, -29.6875, -34.375, -14.0625, 27.34375, 24.21875, -50.0, -35.9375, -13.28125, 10.15625, 24.21875, 36.71875, -41.40625, -46.875, 2.34375, -17.96875, 11.71875, 39.84375, -8.59375, -2.34375, -7.8125, -8.59375, -32.03125, -19.53125, 21.09375, -14.0625, 7.8125, 15.625, -28.125, -2.34375, -14.0625, 39.0625, -19.53125, 14.0625, -38.28125, -7.8125, -18.75, 39.0625, 36.71875])
    
    # 1
    interval_count = 30
    
    
    SS = datal.getSS()
    ISS = datal.getISS(interval_count)
    pprint(SS)
    pprint(ISS)
        
    # 2
    
    M = datal.getM()
    D = datal.getD()
    print(f"{M=}")
    print(f"{D=}")
    
    # 3
    
    plt = datal.drawGistByISS(
        ISS,
        xLabel="результат измерения, см.",
        yLabel="кол-во участников",
        label="обхват грудной клетки",
        title="Вариант. 5, Результаты измерения обхвата грудной клетки 120 женщин"
        )
    plt.show()
    
    # 4
    
    def normal_dist(x, mean = 2.1, sd=1.5):
        prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
        return prob_density/50
    x = np.linspace(-1,interval_count,70)
    pdf = normal_dist(x)
    plt.plot(x,pdf , color = 'red')
    # plt.show()
    
    print("нормальное распределение")