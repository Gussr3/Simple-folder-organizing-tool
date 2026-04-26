import os
import shutil
from pathlib import Path

python_list = []
text_list = []
doc_list = []
misc_list = []


folder_path = Path("source folder")
python_folder = "destination folder"
text_folder = "destination folder"
document_folder = "destination folder"

for i in folder_path.iterdir():
    x = i
    if x.suffix == ".py":
        python_list.append(x)
    elif x.suffix == ".txt":
        text_list.append(x)
    else:
        misc_list.append(x)

for i in range(len(text_list)):
    to_move = str(text_list[i])
    print(to_move)
    shutil.move(to_move, text_folder)

for i in range(len(python_list)):
    to_move = str(python_list[i])
    shutil.move(to_move, python_folder)

for i in range(len(misc_list)):
    to_move = str(misc_list[i])
    shutil.move(to_move, document_folder)
print(python_list, text_list, doc_list, misc_list)
