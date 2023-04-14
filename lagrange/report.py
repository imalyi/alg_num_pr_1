import os
from datetime import datetime


class Report:
    def __init__(self, polynome):
        self.polynome = polynome

    def save(self):
        now = datetime.now()
        current_datetime = now.strftime("%Y%m%d_%H%M%S")
        filename = f"report_{current_datetime}.tex"
        file_path = os.path.join('../reports/', filename)
        with open(file_path, 'w') as f:
            f.write(self.generate())

    def __generate_multipliers(self):
        multipliers_view = []

        for multiplier in self.polynome.multipliers.multipliers:
            multipliers_view.append(f"${multiplier}$")
        multipliers_view = ' \\\ '.join(multipliers_view)
        return multipliers_view

    def __generate_p(self):
        res = "$P(x)="
        terms = []
        i = 0
        for x_y in self.polynome.data.data:
            terms.append(f"{x_y.y}\cdot l_{i}")
            i += 1
        res += "+".join(terms)
        res += "$"
        return res

    def generate(self):
        self.__generate_multipliers()
        self.polynome.plot.plot()
        content = f"""\documentclass{{article}}
        \\usepackage{{polski}}
        \\usepackage{{graphicx}}
        \\begin{{document}}
        
        Obliczenie najlepszego przybliżenia \sqrt(23):\\\\[0.25cm]
        \\begin{{align*}}
        {self.__generate_multipliers()} \\\\[0.25cm]
        {self.__generate_p()} \\\\[0.25cm]
        \\end{{align*}}\\\\[0.25cm]
        Wzór ogólny wielomianu:\\\\[0.25cm]
        \\begin{{split}}
        $P(x) =${self.polynome.format_common_formula()}
        \\end{{split}}
        
        \includegraphics{{{self.polynome.plot.filename}}}
        
        \\end{{document}}"""
        return content

    def __str__(self):
        return self.generate()
