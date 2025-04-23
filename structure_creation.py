from pathlib import Path
import os

import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "src\__init__.py",  # Linux use / , for windows use \
    "src\helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research\\trials.ipynb",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:  #This will create empty file as we pass w
            pass
            logging.info(f"creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")
