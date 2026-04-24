import matplotlib.pyplot as plt
import numpy as np
from math import asin

from function import Function


class Plotter:

    @staticmethod
    def draw(eps):
        x_values = np.linspace(-0.99, 0.99, 100)
        series_values = []
        math_values = []

        for x in x_values:
            function = Function(x, eps)
            result = (function.calculate())
            series_values.append(result["series_result"])
            math_values.append(asin(x))

        plt.figure(figsize=(12, 6))
        plt.plot(x_values, series_values, label="Series expansion")
        plt.plot(x_values, math_values, label="math.asin(x)", linestyle="dashed")
        plt.axhline(0, linewidth=0.7)
        plt.axvline(0, linewidth=0.7)
        plt.xlabel("x")
        plt.ylabel("F(x)")
        plt.title("Comparison of asin(x)")
        plt.legend()
        plt.grid(True)
        plt.annotate("asin(x)", xy=(0.5, asin(0.5)))
        plt.savefig("asin_plot.png", dpi=150, bbox_inches="tight")
        plt.show()