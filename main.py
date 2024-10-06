from WeierstrassFunction import WeierstrassFunction
from ClassicEncoding import ClassicEncoding

if __name__ == "__main__":
    N_ITER, N_POP = 12, 12

    targetFunction = WeierstrassFunction()
    encodingMetod = ClassicEncoding(((-5., 5.), (-5., 5.)), (0.1, 0.1))

    print(encodingMetod.decode(encodingMetod.encode((-0.3, 0.3))))

    # targetFunction.draw()
