import math
import tkinter.filedialog as fd
import tkinter.messagebox as mb


class FileManager:

    def __init__(self, root):
        self.root = root
        self.filename = None
        self.result = None

    def download_file(self):
        """Загрузка файла и его парсинг"""
        self.choose_file()
        self.read_file()

    def choose_file(self):
        """Выбирает файл и записывает имя файла"""
        filetypes = (("Текстовый файл", "*.txt"),)
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
        if filename:
            print(filename)
            self.filename = filename

    def read_file(self):
        """Парсит данные из файла"""
        input_str = open(self.filename).read()
        self.result = input_str.split()

    def write_file(self, text=None):
        """Записывет данные в файл"""
        if text is None:
            text = self.result
        with open(self.filename, 'a') as file:
            file.write(str(text) + "\n")
