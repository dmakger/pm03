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

    def create_canvas(self):
        """Создание canvas'a. В ней отрисовывается функция"""
        self.canvas = Canvas(self.root, width=self.WIDTH, height=self.HEIGHT, bg=self.BG)
        self.canvas.pack()
        # Отрисовка точек
        points = self.get_points(self.func)
        self.rendering_points(points)

    def set_guide_lines(self):
        """Создание направляющих (x, y) линий"""
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
            except ZeroDivisionError as ex:
                points.append((x, None))
        return points

    def rendering_points(self, points):
        """Вернет отрисует points"""
        last_point = points[0]
        for point in points[1:]:
            x1, y1 = last_point
            x2, y2 = point
            color = 'black'

            if y1 is None or y2 is None:
                color = 'lightgray'
                if y1 is None:
                    y1 = 0
                if y2 is None:
                    y2 = 0

            self.canvas.create_line(
                x1 * self.STEP + self.WIDTH // 2, -y1 * self.STEP + self.HEIGHT // 2,
                x2 * self.STEP + self.WIDTH // 2, -y2 * self.STEP + self.HEIGHT // 2,
                fill=color
            )
            last_point = point

    def draw(self):
        """Запуск приложения"""
        self.root.mainloop()
