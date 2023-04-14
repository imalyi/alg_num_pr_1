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

    def format_common_formula(self):
        formatted_terms = []
        for term in self.common_formula.split():
            if 'e' in term:
                coeff, exp = term.split('e')
                formatted_term = f'{coeff} \\times 10^{{{exp}}}'
            else:
                formatted_term = term
            formatted_terms.append(formatted_term)

        formatted_formula = ''
        for i, term in enumerate(formatted_terms):
            formatted_formula += term
            if formatted_formula.endswith(('+', '-')):
                formatted_formula += '\\\\\\indent'
        return formatted_formula

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
