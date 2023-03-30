from data import Pair, Data
from view import PolynomialView, MultiplierView, Report

def main():
#    x = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#    y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    x = [-1, 0, 1, 2]
    y = [0, 1, 2, 9]
    d = Data(x, y)
    p = Polynomial(data=d)
    p.calc()


class Polynomial:
    def __init__(self, data):
        self.data = data
        self.report = Report()

    def __calc_multipliers(self):
        self.__multipliers = []

        for i in range(len(self.data.data)):
            self.__multipliers.append(Multiplier(i, self.data))
        self.report.add_multipliers(self.__multipliers)

    def calc(self):
        self.__calc_multipliers()
        res = 0
        for multiplier, data_ in zip(self.__multipliers, self.data.data):
            try:
                res = multiplier.calc(23) * data_.y
            except ZeroDivisionError:
                print('ERR DIV BY 0')
        print(res)
        self.report.generate()


class Multiplier:
    def __init__(self, i, data):
        self.multipliers = []
        self.multipliers_view = []
        self.i = i

        j = 0
        for pair in data.data:
            j += 1
            if j == i:
                continue
            self.multipliers.append(lambda x: (x - pair.x) / (data.data[i].x - pair.x))
            self.multipliers_view.append(MultiplierView(i, pair.x, data.data[i].x))

    def calc(self, x):
        res = 0
        for multiplier in self.multipliers:
            res = res * multiplier(x)
        return res

    def __str__(self):
        mult = list(map(lambda m: str(m), self.multipliers_view))
        return f"l_{self.i}(x)={'*'.join(mult)}"

    def __repr__(self):
        mult = list(map(lambda m: str(m), self.multipliers_view))
        return f"l_{self.i}={'*'.join(mult)}"


if __name__ == "__main__":
    main()
