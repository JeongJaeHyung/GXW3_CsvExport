import os
import sys
import dotenv

dotenv.load_dotenv()

CONFIDENCE = float(os.getenv('CONFIDENCE'))
DELAY = float(os.getenv('DELAY'))

processed_targets = []

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)


ICONS = {
    "program": resource_path('icons/program.png'),
    "scan":    resource_path('icons/scan.png'),
    "unit":    resource_path('icons/unit.png'),
    "folder":  resource_path('icons/folder.png'),
    "target":  resource_path('icons/target.png')
}