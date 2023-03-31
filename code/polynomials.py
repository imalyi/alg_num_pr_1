from data import DataSets
from polynome import Polynome
from math import sqrt
class Polynomials:
    """
    A class that represents a collection of polynomial objects that can be used to find the best polynomial
    approximation for a given set of data.
    """

    def __init__(self, datasets: DataSets):
        """
        Initializes an object of the Polynomials class with a single parameter - datasets.

        :param datasets: A DataSets object containing a list of data points.
        """
        self.datasets = datasets

    def find_best(self):
        """
        Computes a set of polynomial objects for each dataset in the Polynomials object and returns the best
        polynomial approximation for the dataset.

        :return: A polynomial object that best approximates the dataset.
        """
        polynomials = []
        for data in self.datasets:
            p = Polynome(data)
            polynomials.append(p)
        best = min(polynomials, key=lambda p: abs(p.value - sqrt(23)))
        return best
