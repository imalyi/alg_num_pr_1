# jezeli nie dziala
# pip3 install matplotlib
# jezeli nie dziala pip3 install matplotlib na sigmie
# musisz utworzyc virtualenv w pycharm i instalowac w utworzony virtualenv

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

    def __calc_points(self, func):
        end = 30
        x = []
        y = []
        i = 5
        while i < end:
            x.append(i)
            y.append(func(i))
            i += 0.01
        return x, y

    def plot(self):
        plt.plot(*self.__calc_points(lambda i: self.polynome.calc(i)))
        plt.ylabel('Wartosc')
        plt.xlabel('x')
        with open('../reports/' + self.filename, 'wb') as f:
            plt.savefig(f)
