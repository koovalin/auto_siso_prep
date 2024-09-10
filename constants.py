SQL_DIR = 'sql\\'
XLS_DIR = 'xls\\'

file_prep_type = 'sales'
partner_code = "PARTNER_CODE"
file_name = 'АВСэлектро_28022023.xlsb'
file_date = '20230228'

article_col_name = 'vendor_article'
region_col_name = 'rf_subject'
city_col_name = 'city'
qty_col_name = 'sellout'
sum_col_name = 'sales_amount_with_VAT_in_the_purchase_price'
GROUP_COLS = [region_col_name, city_col_name, article_col_name]
SUM_COLS = [qty_col_name, sum_col_name]

sale_cols_name = ['Date_sale', 'Region_code', 'City_code',
                  'Article', 'sale_qty', 'total_Sum', 'Manager']
