from figure import Figure
from figureAussehen import FigureColor
from figureDraw import TriagleDraw
class Triagle(Figure, FigureColor, TriagleDraw):
    name = "Равнобедренный треугольник"
    def __init__(self, width, height, color):
        super().__init__(color)
        if width <= 0:
            raise ValueError("Основание должно быть больше нуля")
        if height <= 0:
            raise ValueError("Высота должна быть больше нуля")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height / 2
    def get_info(self):
        return ("Фигура {}\n" "Основание {}\n" "Высота {}\n" "Цвет {}\n" "Площадь {:.2f}\n").format(self.name, self.width, self.height, self.color, self.area())
    def draw_triagle(self, title):
        x = [-self.width / 2, self.width / 2, 0]
        y = [0,0,self.height]
        self.draw(x,y,title,"triagle.png")
