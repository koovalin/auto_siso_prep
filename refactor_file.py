import pandas as pd

file_path = '../auto_siso_prep/xls/Июль_2024.xls'  # Укажите путь к вашему Excel-файлу

# Читаем весь файл, чтобы найти строку с "Артикул" и игнорировать все строки до неё
df = pd.read_excel(file_path, header=None)

# Найдём индекс строки, содержащей "Артикул", чтобы знать, с какой строки начинать обработку
header_index = df[df.apply(lambda row: row.astype(str).str.contains('Артикул').any(), axis=1)].index[0]

# Читаем файл, начиная с места, где находится "Артикул"
df = pd.read_excel(file_path, skiprows=header_index)

# Инициализация переменной для хранения текущего названия города
current_city = None

new_df = df.copy()

# Обход каждой строки DataFrame
for i, row in new_df.iterrows():
    # Проверка на наличие строки с названием региона
    if 'Регион' in str(row['Аналитика']):
        # Игнорируем строку с регионом
        continue
    # Проверяем, не является ли строка началом блока для нового города
    elif not pd.notna(row.iloc[2]):
        # Устанавливаем текущий город
        current_city = row.iloc[1]
    else:
        if pd.notna(row.iloc[2]):
            row.iloc[0] = current_city

new_df.to_csv("output.csv", index=False, encoding='windows-1251', sep=';')
# Переупорядочивание столбцов

# Вывод очищенного DataFrame
print(new_df)

# (Опционально) Сохраните изменения обратно в Excel
# cleaned_df.to_excel('output_file_path.xlsx', index=False, sheet_name='Sheet1')
