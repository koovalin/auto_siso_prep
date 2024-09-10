from functions import *
from File_selector import *

if __name__ == '__main__':
    flag = True
    while flag:
        file_path = file_selector()
        if file_path:
            db = pd.read_excel(file_path)
            get_sales_csv_file(db, GROUP_COLS, SUM_COLS, sale_cols_name, file_date, file_name)
        else:
            flag = False

    # db = pd.read_excel(XLS_DIR + file_name)
