import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'CDC'
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/_init _. py",
    f"src/{project_name}/components/_init _. py",
    f"src/{project_name}/utils/_init _. py",
    f"src/{project_name}/config/_init _. py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init _. py",
    f"src/{project_name}/entity/_init _. py",
    f"src/{project_name}/constants/_init _. py",
    "config/config.yaml",
    "dvc.yaml",
    "params. yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, fileName = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        with open(filepath,'w') as f:
            pass

        