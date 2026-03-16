import configparser
import os
import sys
sys.path.append('/app/geometric_lib')

try:
    from circle import area as circle_area, perimeter as circle_perimeter
    from square import area as square_area, perimeter as square_perimeter
except ImportError as e:
    print(f"Ошибка импорта модулей geometric_lib: {e}")
    sys.exit(1)

def main():
    config = configparser.ConfigParser()
    config.read('/app/config.ini')

    print("Расчет геометрических фигур на основе geometric_lib")
    print("-" * 50)

    if 'circle' in config:
        r = float(config['circle']['radius'])
        print(f"Круг (радиус={r}):")
        print(f"  Площадь (πr²): {circle_area(r):.2f}")
        print(f"  Периметр (2πr): {circle_perimeter(r):.2f}")

    if 'square' in config:
        a = float(config['square']['side_a'])
        print(f"\nКвадрат (сторона={a}):")
        print(f"  Площадь (a²): {square_area(a):.2f}")
        print(f"  Периметр (4a): {square_perimeter(a):.2f}")

if __name__ == "__main__":
    main()