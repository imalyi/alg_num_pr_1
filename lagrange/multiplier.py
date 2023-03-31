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

