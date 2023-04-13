import itertools


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.x}, {self.y}"


class DataSets:
    def __init__(self, data_raw: list):
        self.data_raw = data_raw
        self.subsets = []

        self.__generate_datasets()
        self._class_size = len(self.subsets)
        self._current_index = 0

    def __len__(self):
        return len(self.subsets)

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < self._class_size - 1:
            self._current_index += 1
            return self.subsets[self._current_index]
        raise StopIteration

    def __generate_datasets(self):
        for i in range(2, len(self.data_raw)):
            subsets = self.__findsubsets(i)
            for subset in subsets:
                self.subsets.append(Data(subset))
        return self.subsets

    def __findsubsets(self, n: int) -> list:
        return list(itertools.combinations(self.data_raw, n))


class Data:
    def __init__(self, data_raw):
        self.data = []
        for x_y in data_raw:
            self.data.append(Pair(x_y[0], x_y[1]))

    def get_data(self, i):
        return self.data[:i] + self.data[i+1:]

    def __str__(self):
        return ', '.join(list(map(lambda row: str(row), self.data)))

    def __repr__(self):
        return '; '.join(list(map(lambda row: str(row), self.data)))

    def to_list(self):
        tmp = []
        for pair in self.data:
            tmp.append((pair.x, pair.y,))
        return tmp