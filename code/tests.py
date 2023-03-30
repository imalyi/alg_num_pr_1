import unittest
from code.polynom import LagrangeMultiplier, Multilplier
from code.data import Data, DataSets


class TestMultipliers(unittest.TestCase):
    def setUp(self):
        data_raw = [
            [-1, -1],
            [0, 0],
            [1, 1],
            [2, 2]
        ]

        self.data = Data(data_raw)
        self.multipliers = []

        for i in range(len(data_raw) - 1):
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


class TestDataSets(unittest.TestCase):
    def setUp(self) -> None:
        self.data_raw = [
            [-1, -1],
            [0, 0],
            [1, 1],
            [2, 2]
        ]
        self.data_sets = DataSets(self.data_raw)

    def test_subsets(self):
        self.assertEqual(len(self.data_sets), 10)


if __name__ == '__main__':
    unittest.main()
