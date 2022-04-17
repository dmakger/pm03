import math
from app import App


def main():
    input_str = open('input.txt').read()
    a, b, step = list(map(float, input_str.split()))

    func = lambda x: a ** x + b

    app = App(func)
    app.create_canvas(step)
    app.draw()


if __name__ == '__main__':
    main()
