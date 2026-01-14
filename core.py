import os
import sys
import dotenv

dotenv.load_dotenv()

CONFIDENCE = float(os.getenv('CONFIDENCE'))
DEFAULT_DELAY = float(os.getenv('DEFAULT_DELAY'))
KEY_PRESS_DELAY = float(os.getenv('KEY_PRESS_DELAY'))

SEQUENCE_DELAY = float(os.getenv('SEQUENCE_DELAY'))
SEQUENCE_TIMEOUT = float(os.getenv('SEQUENCE_TIMEOUT'))

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
    # Start sequence icons
    "information1": resource_path('icons/StartSequence/information1.png'),
    "information2": resource_path('icons/StartSequence/information2.png'),
    "warning": resource_path('icons/StartSequence/warning.png'),
    "properties": resource_path('icons/StartSequence/properties.png'),

    # main seuence icons
    "program": resource_path('icons/SequenceAssets/program.png'),
    "scan": resource_path('icons/SequenceAssets/scan.png'),
    "unit": resource_path('icons/SequenceAssets/unit.png'),
    "folder": resource_path('icons/SequenceAssets/folder.png'),
    "target": resource_path('icons/SequenceAssets/target.png'),
    "Local Labels": resource_path('icons/SequenceAssets/Local Label.png'),
    "Warning": resource_path('icons/SequenceAssets/Warning.png'),
    "done": resource_path('icons/SequenceAssets/done.png'),

    # etc
    "end": resource_path('icons/etc/end.png'),
    "scroll": resource_path('icons/etc/scroll.png')
}