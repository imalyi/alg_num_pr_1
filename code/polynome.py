from data import Data
from report import Report
from lagrange_multipliers import LagrangeMultipliers

class Polynome:
    def __init__(self, data: Data):
        self.data = data
        self.report = Report(data)
        self.__multipliers = LagrangeMultipliers(data)
        self.report.add_multipliers(self.__multipliers)
        self.value = 0
        self.__calc()

    def __calc(self):
        for multiplier, data_ in zip(self.__multipliers.multipliers, self.data.data):
            self.value = self.value + multiplier.calc(23) * data_.y
        self.report.generate()

    def __str__(self):
        return f"{self.data} -> {self.value}"
