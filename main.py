import time
import sequence
from core import DEFAULT_DELAY


from module import Found, Just


def tmp():
    Found.key_press("information1", "enter")
    Found.key_press("information2", "enter")
    Found.key_press("warning", "enter")
    Just.key_press("enter")
    Just.key_press("f4")
    Just.hotkey_press(['ctrl', 'shift', 'q'])
    Just.key_press("enter")

def export2csv():
    # Workflow 1~4
    print(">>> [WORKFLOW 1] 시작")
    sequence.open_tree("program")
    time.sleep(DEFAULT_DELAY)

    print(">>> [WORKFLOW 2] 시작")
    sequence.open_tree("scan")
    time.sleep(DEFAULT_DELAY)

    print(">>> [WORKFLOW 3] 시작")
    sequence.open_tree("unit")
    time.sleep(DEFAULT_DELAY)

    print(">>> [WORKFLOW 4] 시작")
    sequence.open_tree("folder")
    time.sleep(DEFAULT_DELAY)

    print(">>> [WORKFLOW 5] 시작")
    sequence.open_program_block("target")
    time.sleep(DEFAULT_DELAY)
    
    print(">>> 모든 작업 완료!")
        
if __name__ == "__main__":
    #tmp()
    export2csv()