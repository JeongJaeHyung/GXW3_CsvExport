import pyautogui
import time
from feature.expand_all_of import expand_all_of
from feature.main_workflow import work as main_workflow

def export2csv():
    while True:
        # Workflow 1~4
        expand_all_of("program")
        expand_all_of("scan")
        expand_all_of("unit")
        expand_all_of("folder")
        main_workflow("target")
        pyautogui.scroll(-2)
        time.sleep(1.0)
        
if __name__ == "__main__":
    export2csv()