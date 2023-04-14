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

    def __calc(self):
        for multiplier, data_ in zip(self.multipliers.multipliers, self.data.data):
            self.value = self.value + multiplier.calc(23) * data_.y
        self.report.generate()

    def __str__(self):
        return f"{self.data} -> {self.value}"


    def __repr__(self):
        return f"{self.data} -> {self.value}"
