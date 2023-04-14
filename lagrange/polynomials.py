from polynome import Polynome
from math import sqrt
from data import DataSets


class Polynomials:

    def __init__(self, datasets: list):
        self.datasets = DataSets(datasets)

    def find_best(self):
        polynomials = []
        for data in self.datasets:
            p = Polynome(data)
            polynomials.append(p)
        best = sorted(polynomials, key=lambda p: abs(p.value - sqrt(23)))
        return best
