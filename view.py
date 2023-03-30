
class Report:
    def __init__(self):
        pass

    def add_multipliers(self, multipliers):
        self.multipliers = multipliers
        self.__multipliers_view = []

        for multiplier in self.multipliers:
            self.__multipliers_view.append(f"${multiplier}$")

        self.__multipliers_view = ' \\\ '.join(self.__multipliers_view)

    def generate(self):
        content = f""""\documentclass{{article}}
        \\begin{{document}}
        {self.__multipliers_view}
        \end{{document}}"""
        print(content)
        return content




class PolynomialView:
    def __init__(self, multipliers_view):
        self._multipliers_view = multipliers_view

    def __str__(self):
        res = 'P(x)=' + self._multipliers_view



class MultiplierView:
    def __init__(self, i, x_k, x_i):
        self.__view = f"\\frac{{x-{x_k}}}{{{x_k}-{x_i}}}"

    def __str__(self):
        return self.__view

    def __repr__(self):
        return self.__view

