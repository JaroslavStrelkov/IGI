class FigureColor:
    valid_colors = ['blue', 'red', 'green', 'yellow', 'black', 'white']

    def __init__(self, color):
        self.set_color(color)

    def set_color(self, color):
        if color.lower() not in self.valid_colors:
            raise ValueError("Данного цвета нет в системе")
        self._color = color

    @property
    def color(self):
        return self._color