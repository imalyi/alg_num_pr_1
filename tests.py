import unittest
from polynom import LagrangeMultiplier, Multilplier
from data import Data


class TestMultipliers(unittest.TestCase):
    def setUp(self):
        x = [-1, 0, 1, 2]
        y = [-1, 0, 1, 2]

        self.data = Data(x, y)
        self.multipliers = []

        for i in range(len(x) - 1):
            self.multipliers.append(LagrangeMultiplier(i, self.data))

        self.x = 10
        self.true_answ = [-120, 396, -440, 165]

    def test_multipliers(self):
        i = 0
        for m in self.multipliers:
            self.assertEqual(self.true_answ[i], m.calc(self.x))
            i += 1

class TestMultiplier(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_multiplier(self):
        self.multiplier = (Multilplier(0, -1))
        self.x = 10
        self.true_answ = -10
        self.assertEqual(self.multiplier.calc(self.x), self.true_answ)


if __name__ == '__main__':
    unittest.main()
