from polynomials import Polynomials
from getData import import_data


def main():
    p = Polynomials(import_data())
    best = p.find_best()
    for b in best:
        print(b)
    best[0].report.save()


if __name__ == "__main__":
    main()
