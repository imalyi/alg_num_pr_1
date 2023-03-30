
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x};{self.y}"

    def __repr__(self):
        return f"{self.x};{self.y}"


class Data:
    def __init__(self, x_set, y_set):
        self.data = []
        for x, y in zip(x_set, y_set):
            self.data.append(Pair(x, y))

    def get_data(self, i):
        return self.data[:i] + self.data[i+1:]