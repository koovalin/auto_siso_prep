import tkinter as tk
from tkinter import filedialog, messagebox
from functions import *
from constants import *

"""
    Запуск GUI и получение пути к файлу
    file_path = create_gui()
"""


class FileSelectorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Выбор файла")

        width = 150
        height = 100
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = int((screen_height // 2.5) - (height // 2))
        self.master.geometry(f"{width}x{height}+{x}+{y}")
        self.master.resizable(False, False)

        self.selected_file_path = None

        self.btn_select_file = tk.Button(self.master, text="Выбрать файл", command=self.on_file_selected)
        self.btn_select_file.grid(row=0, column=0, padx=width // 5, pady=10)

        self.var_sale = tk.BooleanVar()
        self.checkbox_sale = tk.Checkbutton(self.master, text="Sale", variable=self.var_sale)
        self.checkbox_sale.grid(row=1, column=0, sticky="w")

        self.var_stock = tk.BooleanVar()
        self.checkbox_stock = tk.Checkbutton(self.master, text="Stock", variable=self.var_stock)
        self.checkbox_stock.grid(row=2, column=0, sticky="w")

    def on_file_selected(self):
        __DEFAULT_FILES_DIR = '.\\xls'
        selected_file = filedialog.askopenfilename(
            initialdir=__DEFAULT_FILES_DIR, title='Выберите файл',
            filetypes=[('Excel Files', '*.xls*')]
        )
        if selected_file:
            self.selected_file_path = selected_file
        else:
            messagebox.showwarning("Нет файла", "Вы не выбрали файл.")

    def get_selected_file_path(self):
        return self.selected_file_path


def file_selector():
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()
    return app.get_selected_file_path()
