# jezeli nie dziala
# pip3 install matplotlib
# jezeli nie dziala pip3 install matplotlib na sigmie
# musisz utworzyc virtualenv w pycharm i instalowac w utworzony virtualenv
import math

import matplotlib.pyplot as plt
import datetime


class Plot:
    def __init__(self, polynome):
        self.polynome = polynome
        self.__filename = None

    @property
    def filename(self):
        if not self.__filename:
            self.__filename = str(datetime.datetime.now().timestamp()) + '.png'
        return self.__filename

    def calc_points(self, func):
        end = 25
        x = []
        y = []
        i = 22
        while i < end:
            x.append(i)
            y.append(func(i))
            i += 0.0001
        return x, y

    def plot(self):
        for f in [self.polynome.calc, math.sqrt]:
            x, y = self.calc_points(f)
            plt.plot(x, y, label=f)
            plt.ylabel('Wartosc')
            plt.xlabel('x')

        with open('../reports/' + self.filename, 'wb') as f:
            plt.savefig(f)
