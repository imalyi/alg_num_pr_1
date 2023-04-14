from data import Data
from report import Report
from lagrange_multipliers import LagrangeMultipliers
from common_formula import CommonPolynomeFormula
from plot import Plot


class Polynome:
    def __init__(self, data: Data):
        self.data = data
        self.report = Report(self)
        self.common_formula = CommonPolynomeFormula(self.data).policz()
        self.multipliers = LagrangeMultipliers(data)
        self.plot = Plot(self)

    def calc(self, x):
        tmp = 0
        for multiplier, data_ in zip(self.multipliers.multipliers, self.data.data):
            tmp = tmp + multiplier.calc(x) * data_.y
        return tmp

    @property
    def value(self):
        return self.calc(23)

    def __str__(self):
        return f"{self.data} -> {self.value}"

    def __repr__(self):
        return f"{self.data} -> {self.value}"
