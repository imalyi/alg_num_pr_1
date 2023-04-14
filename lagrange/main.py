import math

from polynomials import Polynomials
from getData import import_data
from math import sqrt
from plot import Plot


def main():
    p = Polynomials(import_data())
    best = p.find_best()
    print(f"sqrt(23) = {math.sqrt(23)}")
    for b in best:
        print(b)
    best[0].report.generate()
    best[0].report.save()


if __name__ == "__main__":
    main()
