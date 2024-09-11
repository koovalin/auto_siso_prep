import tkinter as tk  # Импортируем библиотеку tkinter для создания GUI
from tkinter import ttk, messagebox, filedialog  # Импортируем дополнительные модули для интерфейса
import pandas as pd  # Импортируем pandas для работы с данными Excel
import os  # Импортируем os для работы с файловой системой
import re  # Импортируем re для работы с регулярными выражениями


class App:
    def __init__(self, root):
        self.root = root  # Сохраняем корневое окно
        self.root.title("Client Data Processor")  # Устанавливаем заголовок окна

        width = 150
        height = 150
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = int((screen_height // 2.5) - (height // 2))
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(False, False)

        # Создаем и размещаем метку и поле ввода для кода клиента
        self.client_code_label = tk.Label(root, text="Код клиента:")
        self.client_code_label.pack()
        self.client_code_entry = tk.Entry(root)
        self.client_code_entry.pack()

        # Создаем и размещаем метку и поле ввода для даты
        self.date_label = tk.Label(root, text="Дата (YYYYMMDD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        # Создаем и размещаем метку и выпадающий список для выбора типа
        self.sale_type_label = tk.Label(root, text="Тип:")
        self.sale_type_label.pack()
        self.sale_type = ttk.Combobox(root, values=["sales", "stock"])  # Варианты выбора типа
        self.sale_type.pack()

        # Создаем кнопку для обработки данных
        self.process_button = tk.Button(root, text="Обработать", command=self.process_data)
        self.process_button.pack()

    def process_data(self):
        # Получаем введенные данные
        client_code = self.client_code_entry.get().strip()  # Код клиента
        date = self.date_entry.get().strip()  # Дата
        sale_type = self.sale_type.get()  # Тип

        # Проверяем формат даты
        if not self.validate_date(date):
            messagebox.showerror("Ошибка", "Неверный формат даты, должен быть YYYYMMDD")  # Показ ошибки
            return

        # Получаем ФИО клиента
        client_name = self.get_client_name(client_code)

        # Открываем диалог для выбора файла в папке "./xls"
        file_path = filedialog.askopenfilename(initialdir="./xls", title="Выберите файл",
                                               filetypes=[("Excel files", "*.xls*")])
        if not file_path:
            messagebox.showerror("Ошибка", "Файл не выбран")  # Показ ошибки, если файл не был выбран
            return

        # Загружаем данные из выбранного Excel файла
        df = pd.read_excel(file_path)

        # Группируем и суммируем данные по первым трём столбцам
        grouped_df = df.groupby([df.columns[0], df.columns[1], df.columns[2]]).sum().reset_index()

        # Добавляем новый столбец 'Data' с введенной датой
        grouped_df.insert(0, 'Data', date)

        # Добавляем новый столбец 'City_code', заменяя города на их коды
        grouped_df.insert(2, 'City_code', grouped_df['city'].apply(self.get_city_code))  # Получаем коды городов

        # Добавляем новый столбец 'Manager', заполняя его ФИО клиента
        grouped_df['Manager'] = client_name

        # Формируем имя файла для сохранения
        output_filename = f"{date}_{client_code}_{sale_type}.csv"  # Формат имени файла
        output_path = os.path.join("./csv", output_filename)  # Полный путь для сохранения файла

        # Сохраняем обработанные данные в CSV файл с указанной кодировкой и сепаратором
        grouped_df.to_csv(output_path, index=False, sep=";", encoding="windows-1251")
        messagebox.showinfo("Готово",
                            f"Обработка завершена. Файл сохранен как {output_filename}")  # Сообщение об успешном завершении

    def validate_date(self, date_str):
        # Проверка формата даты с помощью регулярного выражения
        return bool(re.match(r'^\d{8}$', date_str))

    def get_client_name(self, client_code):
        # Получение ФИО клиента по коду (заменить заглушку на реальную логику)
        return "ФИО клиента"  # Заглушка для ФИО клиента

    def get_city_code(self, city):
        # Получение кода города по его названию (можно заменить на реальную логику)
        city_code_map = {
            'Москва'         : '77',
            'Санкт-Петербург': '78',
            'Нижний-Новгород': '52',
            # Добавьте другие соответствия городам
        }
        return city_code_map.get(city, city)  # Возвращает код города или само название, если код не найден


if __name__ == "__main__":
    root = tk.Tk()  # Создание основного окна приложения
    app = App(root)  # Инициализация приложения
    root.mainloop()  # Запуск главного цикла приложения
