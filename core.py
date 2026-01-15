import os
import sys
import dotenv

dotenv.load_dotenv()

CONFIDENCE = float(os.getenv('CONFIDENCE'))
DEFAULT_DELAY = float(os.getenv('DEFAULT_DELAY'))
KEY_PRESS_DELAY = float(os.getenv('KEY_PRESS_DELAY'))

DEFAULT_TIMEOUT = float(os.getenv('DEFAULT_TIMEOUT'))
NODE_OPEN_TIMEOUT = float(os.getenv('NODE_OPEN_TIMEOUT'))


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

    # Sequence Control icons
    "Navigation": resource_path('icons/NonActiveNavigation.png'),
    "Parameter": resource_path('icons/ActiveClosedParameter.png'),
    "Warning": resource_path('icons/Warning.png'),
    "ProgramBody": resource_path('icons/ProgramBody.png'),
    
    
    # Node icons
    "Project": resource_path('icons/ActiveProject.png'),
    "Program": resource_path('icons/ActiveClosedProgram.png'),
    "Scan": resource_path('icons/ActiveClosedScan.png'),
    "Unit": resource_path('icons/ActiveClosedUnit.png'),
    "Folder": resource_path('icons/ActiveClosedFolder.png'),
    "ProgramBlock1": resource_path('icons/ActiveClosedProgramBlock.png'),
    "ProgramBlock2": resource_path('icons/ActiveOpenProgramBlock.png'),

}