from tkinter import *
import math

# размеры экрана
WIDTH = 700
HEIGHT = 700

# чтение файла вводных данных
f = open('input.txt')
input_str = f.read()
f.close()

# коэффиценты и шаг полученные из входной строки по пробелам
a, b, c, step = list(map(float, input_str.split()))
# заданная функция
func = lambda y: a * math.pow(x, 2) + b * x + c

# инициализация программы
root = Tk()
canv = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canv.pack()

# создание направляющих x y линий
canv.create_line(0, HEIGHT // 2, WIDTH, HEIGHT // 2, fill='red',
                 width=1, arrow=LAST, dash=(1, 1),
                 activefill='red',
                 arrowshape="5 10 5")
canv.create_line(WIDTH // 2, HEIGHT, WIDTH // 2, 0, fill='green',
                 width=1, arrow=LAST, dash=(1, 1),
                 activefill='green',
                 arrowshape="5 10 5")

# генерация точек по функции
_points = []
for x in range(-100, 100):
    try:
        _points.append((x, func(x)))
    except:
        _points.append((x, None))

print(_points)

# рендеринг точек
_last_point = _points[0]
for p in _points[1:]:
    x1, y1 = _last_point
    x2, y2 = p
    clr = 'black'
    if y1 == None or y2 == None:
        clr = 'lightgray'
        if y1 == None:
            y1 = 0
        if y2 == None:
            y2 = 0
    canv.create_line(
        x1 * step + WIDTH // 2, -y1 * step + HEIGHT // 2,
        x2 * step + WIDTH // 2, -y2 * step + HEIGHT // 2,
        fill=clr
    )
    _last_point = p

root.mainloop()