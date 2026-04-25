import os
import shutil
from pathlib import Path

python_list = []

folder_path = Path("/home/gustavo/PythonProjects/test_folder")
python_folder = "/home/gustavo/PythonProjects"


for i in folder_path.iterdir():
    x = i
    if x.suffix == ".py":
        python_list.append(x)

for i in range(len(python_list)):
    to_move = str(python_list[i])
    print(to_move)
    shutil.move(to_move, python_folder)
