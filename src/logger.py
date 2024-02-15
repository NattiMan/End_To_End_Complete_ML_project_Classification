import logging
import os
from datetime import datetime

os.makedirs('logs',exist_ok=True)
ct = datetime.now().strftime("%d%m%Y_%H%M%S")

FILE_PATH_NAME = os.path.join('logs', f"{ct}.log")

logging.basicConfig(
    filename=FILE_PATH_NAME,
    level = logging.INFO
)


