from math import factorial, asin


class Function:

    total_calculations = 0

    def __init__(self, x, eps):

        self.x = x
        self.eps = eps

        Function.total_calculations += 1

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):

        if not (-1 < value < 1):
            raise ValueError("x must be in range (-1, 1)")
        self._x = value

    @property
    def eps(self):
        return self._eps

    @eps.setter
    def eps(self, value):

        if value <= 0:
            raise ValueError("eps must be greater than 0")

        self._eps = value

    def calculate(self):

        result = 0
        n = 0

        values = []

        while True:
            term = (factorial(2 * n) / ((4 ** n) * (factorial(n) ** 2) * (2 * n + 1))) * (self.x ** (2 * n + 1))
            result += term
            values.append(result)
            if abs(term) < self.eps:
                break
            n += 1
        return {"series_result": result, "math_result": asin(self.x), "iterations": n, "values": values}

    def __str__(self):
        return (f"Function(x={self.x}, " f"eps={self.eps})")