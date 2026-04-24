from triagle import Triagle
def get_float_parameter(m):
    while(True):
        try:
            n = float(input(m))
            if n <= 0:
                print("Введите отличное от нуля положительное число")
                continue
            return n
        except ValueError:
            print("Ошибка ввода")

def main():
    a = get_float_parameter("Введите основание: ")
    h = get_float_parameter("Введите высоту: ")
    color = input("Введите цвет: ")
    title = input("Введите подпись фигуры: ")
    t = Triagle(a, h, color)
    print(t.get_info())
    t.draw_triagle(title)
main()
