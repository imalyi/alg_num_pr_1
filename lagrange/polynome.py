from data import Data
from report import Report
from lagrange_multipliers import LagrangeMultipliers
from common_formula import CommonPolynomeFormula


class Polynome:
    def __init__(self, data: Data):
        self.data = data
        self.report = Report(self)
        self.common_formula = CommonPolynomeFormula(self.data).policz()
        self.multipliers = LagrangeMultipliers(data)
        self.value = 0
        self.__calc()

    def __calc(self):
        for multiplier, data_ in zip(self.multipliers.multipliers, self.data.data):
            self.value = self.value + multiplier.calc(23) * data_.y
        self.report.generate()

    def __str__(self):
        return f"{self.data} -> {self.value}"


    def __repr__(self):
        return f"{self.data} -> {self.value}"
