import os
import shutil
import pathlib
from datetime import datetime

def copy_file_by_date(dest_path:str, file_name: str):
    if os.path.exists(dest_path):
        pass

source_path = os.getcwd()
print(source_path)

for current_dir, cur_dir_lst, files_lst in os.walk(source_path):
    for file_name in files_lst:
        file_path:str = os.path.join(current_dir, file_name)
        if  os.path.exists(file_path):            
            creation_date = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(creation_date)
            year = creation_date.year
            month = creation_date.month
            day = creation_date.day
            print(file_name, year, month, day)
        
        