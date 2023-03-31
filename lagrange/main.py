# TODO: print sqrt
# TODO: add data input
# TODO: plot graphs
# TODO: fix latex report
# TODO: add common formula

from polynomials import Polynomials
from getData import GetData


def main():
    data = GetData()
    p = Polynomials(data.getData())
    best = p.find_best()
    for b in best:
        print(b)
#     best.report.save()


if __name__ == "__main__":
    main()
