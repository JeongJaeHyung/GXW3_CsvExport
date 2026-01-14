import pyautogui
import time
from feature.expand_all_of import expand_all_of
from feature.main_workflow import work as main_workflow
from core import DELAY

def export2csv():
    # Workflow 1~4
    print(">>> [WORKFLOW 1] 시작")
    expand_all_of("program")
    time.sleep(DELAY)

    print(">>> [WORKFLOW 2] 시작")
    expand_all_of("scan")
    time.sleep(DELAY)

    print(">>> [WORKFLOW 3] 시작")
    expand_all_of("unit")
    time.sleep(DELAY)

    print(">>> [WORKFLOW 4] 시작")
    expand_all_of("folder")
    time.sleep(DELAY)

    print(">>> [WORKFLOW 5] 시작")
    main_workflow("target")
    time.sleep(DELAY)
    
    print(">>> 모든 작업 완료!")
        
if __name__ == "__main__":
    export2csv()