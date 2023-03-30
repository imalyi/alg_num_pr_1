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
    p = Polinomials(d)
    print(p.find_best())


class Polinomials:
    def __init__(self, datasets: DataSets):
        self.datasets = datasets

    def find_best(self):
        polinomials = []
        for data in self.datasets:
            p = Polynome(data)
            polinomials.append(p)
        best = min(polinomials, key=lambda p: abs(p.value - sqrt(23)))
        return best


class Polynome:
    def __init__(self, data: Data):
        self.data = data
        self.report = Report(data)
        self.__multipliers = LagrangeMultipliers(data)
        self.report.add_multipliers(self.__multipliers)
        self.value = 0
        self.__calc()

    def __calc(self):
        for multiplier, data_ in zip(self.__multipliers.multipliers, self.data.data):
            self.value = self.value + multiplier.calc(23) * data_.y
        self.report.generate()

    def __str__(self):
        return f"{self.data} -> {self.value}"


class LagrangeMultiplier:
    def __init__(self, i: int, data: Data):
        self.multipliers = []
        self.i = i
        for pair in data.get_data(i):
            x_i = data.data[i].x
            self.multipliers.append(Multilplier(pair.x, x_i))

    def calc(self, x: int):
        res = 1
        for multiplier in self.multipliers:
            res = res * multiplier.calc(x)
        return res

    def __to_str(self):
        mult = list(map(lambda m: str(m), self.multipliers))
        res = f"l_{self.i}(x)={'*'.join(mult)}"
        res = res.replace('--', '+')
        return res

    def __str__(self):
        return self.__to_str()

    def __repr__(self):
        return self.__to_str()


class LagrangeMultipliers:
    def __init__(self, data: Data):
        self.multipliers = []
        for i in range(len(data.data)):
            self.multipliers.append(LagrangeMultiplier(i, data))


class Multilplier:
    def __init__(self, x_k, x_i):
        self.x_k = x_k
        self.x_i = x_i
        self.value = None

    def calc(self, x):
        self.value = (x - self.x_k) / (self.x_i - self.x_k)
        return self.value

    def __str__(self):
        return f"\\frac{{x-{self.x_k}}}{{ {self.x_i}-{self.x_k}}}"

    def __repr__(self):
        return f"\\frac{{x-{self.x_k}}}{{ {self.x_i}-{self.x_k}}}"


class Report:
    def __init__(self, data: Data):
        self.data = data

    def add_multipliers(self, multipliers: LagrangeMultipliers):
        self.multipliers = multipliers
        self.__multipliers_view = []

        for multiplier in self.multipliers.multipliers:
            self.__multipliers_view.append(f"${multiplier}$")
        self.__multipliers_view = ' \\\ '.join(self.__multipliers_view)

    def __generate_p(self):
        res = "$P(x)="
        i = 0
        for x_y in self.data.data:
            res = res + f"{x_y.y}*l_{i}+"
            i += 1
        res = res + '$'
        return res

    def generate(self):
        content = f""""\documentclass{{article}}
        \\begin{{document}}
        {self.__multipliers_view}
        {self.__generate_p()}
        \end{{document}}"""
        return content


if __name__ == "__main__":
    main()

