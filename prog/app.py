from tkinter import *


class App:
    # Размеры экрана
    WIDTH = 700
    HEIGHT = 700
    # Цвет фона
    BG = 'white'
    ARROWSHAPE = "5 10 5"
    # Шаг
    STEP = 20

    def __init__(self, func):
        self.root = Tk()
        self.func = func

        self.canvas = None

    def create_canvas(self, step=None):
        """Создание canvas'a. В ней отрисовывается функция"""
        if step is None:
            step = self.STEP

        self.canvas = Canvas(self.root, width=self.WIDTH, height=self.HEIGHT, bg=self.BG)
        self.canvas.pack()
        self.set_guide_lines()
        # Отрисовка точек
        points = self.get_points(self.func)
        self.rendering_points(points, step)

    def set_guide_lines(self):
        """Создание направляющих (x, y) линий"""
        # создание направляющих x y линий
        self.canvas.create_line(0, self.HEIGHT // 2, self.WIDTH, self.HEIGHT // 2, fill='red',
                                width=1, arrow=LAST, dash=(1, 1),
                                activefill='red4',
                                arrowshape=self.ARROWSHAPE)
        self.canvas.create_line(self.WIDTH // 2, self.HEIGHT, self.WIDTH // 2, 0, fill='green',
                                width=1, arrow=LAST, dash=(1, 1),
                                activefill='darkgreen',
                                arrowshape=self.ARROWSHAPE)

    @staticmethod
    def get_points(func):
        """Вернет points для отрисовки"""
        points = list()
        for x in range(-100, 100):
            try:
                points.append((x, func(x)))
            except Exception:
                points.append((x, None))
        return points

    def rendering_points(self, points, step=None):
        """Вернет отрисует points"""
        if step is None:
            step = self.STEP
        last_point = points[0]

        for i in range(len(points)):
            x1, y1 = last_point
            x2, y2 = points[i]
            clr = 'black'
            if y1 is None or y2 is None:
                last_point = points[i]
                continue
            self.canvas.create_line(
                x1 * step + self.WIDTH // 2, -y1 * step + self.HEIGHT // 2,
                x2 * step + self.WIDTH // 2, -y2 * step + self.HEIGHT // 2,
                fill=clr
            )
            last_point = points[i]

    def draw(self):
        """Запуск приложения"""
        self.root.mainloop()
