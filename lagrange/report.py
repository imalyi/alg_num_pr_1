import os
from datetime import datetime
from data import Data
from lagrange_multipliers import LagrangeMultipliers


class Report:
    def __init__(self, data: Data):
        self.data = data

    def save(self):
        now = datetime.now()
        current_datetime = now.strftime("%Y%m%d_%H%M%S")
        filename = f"report_{current_datetime}.tex"
        file_path = os.path.join('../reports/', filename)
        with open(file_path, 'w') as f:
            f.write(self.generate())

    def add_multipliers(self, multipliers: LagrangeMultipliers):
        self.multipliers = multipliers
        self.__multipliers_view = []

        for multiplier in self.multipliers.multipliers:
            self.__multipliers_view.append(f"${multiplier}$")
        self.__multipliers_view = ' \\\ '.join(self.__multipliers_view)

    def __generate_p(self):
        res = "$P(x)="
        terms = []
        i = 0
        for x_y in self.data.data:
            terms.append(f"{x_y.y}*l_{i}")
            i += 1
        res += "+".join(terms)
        res += "$"
        return res

    def generate(self):
        content = f"""\documentclass{{article}}
        \\begin{{document}}
        Obliczenie najlepszego przybliżenia \sqrt(23):\\\\[0.25cm]
        \\begin{{align*}}
        {self.__multipliers_view}
        \\end{{align*}}\\\\[0.25cm]
        {self.__generate_p()}
        \\end{{document}}"""
        return content

    def __str__(self):
        return self.generate()
