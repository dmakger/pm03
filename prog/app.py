import tkinter.messagebox as mb
from tkinter import *

from manager import FileManager
from vector import VectorManager


class App:

    def __init__(self):
        self.root = Tk()
        self.file_manager = FileManager(self.root)
        self.vector_manager = VectorManager(self.root)

        self.create_window()

    def create_window(self):
        """Создание навигации"""
        Frame(self.root, relief=RAISED, borderwidth=1).pack(fill=BOTH, expand=True)
        Button(self.root, text="Закрыть", command=self.close).pack(side=BOTTOM)
        Button(self.root, text="Очистить", command=self.clear).pack(side=BOTTOM)
        Button(self.root, text="Вывести сумму в файл", command=self.write_file).pack(side=BOTTOM)
        Button(self.root, text="Вывести сумму", command=self.sum).pack(side=BOTTOM)
        Button(self.root, text="Загрузить вектор", command=self.download_vector).pack(side=BOTTOM)

    def download_vector(self):
        """Загрузка векторов"""
        self.file_manager.download_file()
        vector = self.file_manager.result
        self.vector_manager.add(vector)
        print("Добавлен вектор: ", vector)

    def chek_result(self, result):
        if result['info'] == self.vector_manager.EMPTY_ERROR:
            mb.showerror("Ошибка", "Вы не передали ни одного вектора")
        elif result['info'] == self.vector_manager.VECTOR_ERROR:
            mb.showerror("Ошибка", "Переданные вектора не уравнены")

    def sum(self):
        result = self.vector_manager.sum()
        print(result)
        self.chek_result(result)
        if result['info'] == self.vector_manager.SUCCESS:
            mb.showinfo("Cумма", "Результат суммы:  " + str(result['value']))

    def write_file(self):
        result = self.vector_manager.sum()
        print(result)
        self.chek_result(result)
        if result['info'] == self.vector_manager.SUCCESS:
            self.file_manager.write_file(result['value'])

    def clear(self):
        self.vector_manager.clear()
        print("Все вектора удалены")

    def draw(self):
        """Запуск приложения"""
        self.root.mainloop()

    def close(self):
        self.root.quit()
