

class Accumulator:
    def __init__(self, seed):
        self.seed = seed

    def __add__(self, other):
        x = Accumulator(self.seed)
        x.seed += other.seed
        return x

    def __sub__(self, other):
        x = Accumulator(self.seed)
        x.seed -= other.seed
        return x

    def __repr__(self):
        return '<{}>'.format(self.seed)

if (__name__ == "__main__"):
    a = Accumulator(45234)
    b = Accumulator(25984)

    x = a + b
    y = a - b
    print('{} + {} = {}'.format(a, b, x))
    print('{} - {} = {}'.format(a, b, y))
