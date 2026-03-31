import logging
from pathlib import Path

from config import image , bg_img
from gui import gui

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"), 
        logging.StreamHandler()             
    ]
)

log = logging.getLogger(__name__)


if __name__ == "__main__":
    gui(image,bg_img)

