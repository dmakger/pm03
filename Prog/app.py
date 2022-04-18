import math
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb


class App:
    WIDTH = 800
    HEIGHT = 800
    BG = 'white'
    ARROWSHAPE = "6 7 6"
    STEP = 15

    def __init__(self):
        self.root = Tk()
        self.func = None

        self.filename = None
        self.step = self.STEP

        self.frame = self.get_frame()
        self.canvas = None
        self.lines = list()

        self.create_canvas()
        self.create_window()

    def get_frame(self):
        frame = Frame(self.root, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        return frame

    def create_window(self):
        Button(self.root, text="Выйти из программы", command=self.close).pack(side=LEFT)
        Button(self.root, text="Загрузить текстовый файл", command=self.download_file).pack(side=LEFT)

    def download_file(self):
        self.choose_file()
        self.read_file()
        self.download_canvas()

    def choose_file(self):
        filetypes = (("Текстовый файл", "*.txt"),)
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
        if filename:
            print(filename)
            self.filename = filename

    def read_file(self):
        input_str = open(self.filename).read()
        print(input_str)
        try:
            a, b, self.step = list(map(float, input_str.split()))
        except Exception:
            mb.showerror("Ошибка!", "Входные данные некорректны!")

        self.func = lambda x: a * math.log(x) + b

    def create_canvas(self):
        self.canvas = Canvas(self.root, width=self.WIDTH, height=self.HEIGHT, bg=self.BG)
        self.canvas.pack()
        self.set_guide_lines()

    def download_canvas(self):
        points = self.get_points(self.func)
        self.rendering_points(points)

    def set_guide_lines(self):
        self.canvas.create_line(0, self.HEIGHT // 2, self.WIDTH, self.HEIGHT // 2, fill='red', width=1, arrow=LAST, dash=(1, 1), activefill='red4', arrowshape=self.ARROWSHAPE)
        self.canvas.create_line(self.WIDTH // 2, self.HEIGHT, self.WIDTH // 2, 0, fill='green', width=1, arrow=LAST, dash=(1, 1), activefill='darkgreen', arrowshape=self.ARROWSHAPE)

    @staticmethod
    def get_points(func):
        points = list()
        for x in range(1, 100):
            try:
                points.append((x, func(x)))
            except Exception:
                points.append((x, None))
        return points

    def rendering_points(self, points):
        last_point = points[0]
        for line in self.lines:
            self.canvas.delete(line)

        for i in range(1, len(points)):
            x1, y1 = last_point
            x2, y2 = points[i]
            clr = 'black'
            if y1 is None or y2 is None:
                last_point = points[i]
                continue
            pk = self.canvas.create_line(
                x1 * self.step + self.WIDTH // 2, -y1 * self.step + self.HEIGHT // 2,
                x2 * self.step + self.WIDTH // 2, -y2 * self.step + self.HEIGHT // 2,
                fill=clr
            )
            self.lines.append(pk)
            last_point = points[i]

    def draw(self):
        self.root.mainloop()

    def close(self):
        self.root.quit()
