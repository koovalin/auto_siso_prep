import pandas as pd
import os


def get_sales_csv_file(new_db, group_cols: list, sum_cols: list[str], sale_cols_name: list[str], file_date: str,
                       file_name: str):
    new_db = get_db_from_excel(new_db, group_cols, sum_cols)
    new_db = prepare_sales_table(new_db, file_date, sale_cols_name)
    save_table_to_csv(new_db, os.path.splitext(file_name)[0])


def get_stock_csv_file():
    pass


def get_db_from_excel(df, group_by_cols: list, sum_by_cols: list):
    excel_db = df[group_by_cols + sum_by_cols].copy()
    for col in sum_by_cols:
        excel_db[col] = excel_db[col].astype(float)
    excel_db = excel_db.groupby(group_by_cols)[sum_by_cols].sum().reset_index()
    return excel_db


def prepare_sales_table(sales_df, date_value: str, rename_cols: list[str]):
    sales_df.insert(0, 'Date_sale', date_value)
    # sales_df.insert(2, 'City_code', 'CITY_CODE')
    sales_df['Manager'] = 'MANAGER_NAME'
    sales_df.columns = rename_cols
    return sales_df


def prepare_stock_table():
    pass


def save_table_to_csv(prepared_table, file_path: str):
    csv_folder = f"{os.getcwd()}\\csv"
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)
    file_path = f"{csv_folder}\\{file_path}.csv"
    prepared_table.to_csv(file_path, sep=';', index=False, encoding='windows-1251', decimal=',')
