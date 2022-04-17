from tkinter import *
import math

# размеры экрана
WIDTH = 700
HEIGHT = 700

# чтение файла вводных данных
f = open('open.txt')
input_str = f.read()

# коэффиценты и шаг полученные из парсинга входной строки по пробелам
a, b, c, step = list(map(float, input_str.split()))
# ваша функция
func = lambda x: a * math.atan(b * x) + c

# сама программа
# инициализация программы
root = Tk()
canv = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canv.pack()

# создание направляющих x y линий
canv.create_line(0, HEIGHT // 2, WIDTH, HEIGHT // 2, fill='red',
                 width=1, arrow=LAST, dash=(1, 1),
                 activefill='red4',
                 arrowshape="5 10 5")
canv.create_line(WIDTH // 2, HEIGHT, WIDTH // 2, 0, fill='green',
                 width=1, arrow=LAST, dash=(1, 1),
                 activefill='darkgreen',
                 arrowshape="5 10 5")
# линия на сотом пикселе
# canv.create_line(WIDTH//2+100, HEIGHT, WIDTH//2+100, 0, fill='gray',
#                 width=1, dash=(1,1))

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
for i in range(len(_points)):
    x1, y1 = _last_point
    x2, y2 = _points[i]
    clr = 'black'
    if y1 is None or y2 is None:
        _last_point = _points[i]
        continue
    canv.create_line(
        x1*step+WIDTH//2, -y1*step+HEIGHT//2,
        x2*step+WIDTH//2, -y2*step+HEIGHT//2,
        fill=clr
    )
    _last_point = _points[i]

root.mainloop()