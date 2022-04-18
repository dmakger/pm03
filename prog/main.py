import math
from app import App


def main():
    # Коэффициенты
    input_str = open('input.txt').read()
    a, b, step = list(map(float, input_str.split()))
    # Функция
    func = lambda x: a * math.sin(x) + b

    # Отрисовка
    app = App(func)
    # app.create_canvas(step)
    app.draw()


if __name__ == '__main__':
    main()