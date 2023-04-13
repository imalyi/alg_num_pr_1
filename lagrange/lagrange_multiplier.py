from data import Data
from multiplier import Multilplier


class LagrangeMultiplier:
    def __init__(self, i: int, data: Data):
        self.multipliers = []
        self.i = i
        for pair in data.get_data(i):
            x_i = data.data[i].x
            self.multipliers.append(Multilplier(pair.x, x_i))

    def calc(self, x: int):
        res = 1
        for multiplier in self.multipliers:
            res = res * multiplier.calc(x)
        return res

    def __to_str(self):
        mult = list(map(lambda m: str(m), self.multipliers))
        res = "\cdot".join(mult)
        res = f"l_{self.i}(x)={res}"
        res = res.replace('--', '+')
        return res

    def __str__(self):
        return self.__to_str()

    def __repr__(self):
        return self.__to_str()
