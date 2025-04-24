import os
import pathlib
from datetime import datetime

source_path = os.getcwd()
print(source_path)
date_dct: dict = dict()
for current_dir, cur_dir_lst, files_lst in os.walk(source_path):
    for file_name in files_lst:
        file_path:str = os.path.join(current_dir, file_name)
        if  os.path.exists(file_path):            
            creation_date = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(creation_date)
            date_dct['year'] = creation_date.year
            date_dct['month'] = creation_date.month
            date_dct['day'] = creation_date.day
            print(file_name, date_dct)
        