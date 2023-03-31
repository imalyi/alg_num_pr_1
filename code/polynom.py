from data import Data, DataSets
from math import sqrt


def main():
    data_raw = [
            [0, 0],
            [1, 1],
            [4, 2],
            [9, 3],
            [16, 4],
            [25, 5],
            [36, 6],
            [49, 7],
            [64, 8],
            [81, 9]
        ]
    d = DataSets(data_raw)
    p = Polynomials(d)
    best = p.find_best()
    print(best)
    best.report.save()








if __name__ == "__main__":
    main()

