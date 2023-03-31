from data import Data
from data import Data
from lagrange_multiplier import LagrangeMultiplier


class LagrangeMultipliers:
    def __init__(self, data: Data):
        self.multipliers = []
        for i in range(len(data.data)):
            self.multipliers.append(LagrangeMultiplier(i, data))

