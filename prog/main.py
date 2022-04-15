import math
from app import App


def main():
    # Коэффициенты
    a = 5
    b = 3
    # Функция
    func = lambda x: a * math.sin(x) + b

    # Отрисовка
    app = App(func)
    app.create_canvas()
    app.draw()


if __name__ == '__main__':
    main()
