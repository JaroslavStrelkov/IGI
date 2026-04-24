import matplotlib.pyplot as plt
class TriagleDraw:
    def draw(self, x, y, title, filename):
        plt.figure(figsize=(5, 5))
        plt.fill(x, y, color = self.color)
        plt.plot(x + [x[0]], y + [y[0]])
        plt.title(title)
        plt.grid(True)
        plt.savefig(filename)
        plt.show()

