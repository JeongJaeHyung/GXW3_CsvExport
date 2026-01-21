from module import Waited, Found
import time
import pyperclip
from core import CURRENT_EXPORT_DIR, ICON


def work(t_center):
    print("LOG: program_export_work.work() called")
    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.right_click(t_center)

    Waited.key_press('e')
    Waited.key_press('left')
    Waited.key_press('enter')

    Waited.key_press('f')
    print(f"CURRENT_EXPORT_DIR : {CURRENT_EXPORT_DIR}")
    pyperclip.copy(CURRENT_EXPORT_DIR)
    Waited.hotkey_press(['ctrl', 'v'])
    Waited.key_press('enter')
    Waited.key_press('enter')

    while True:
        if Found.icon(ICON.GXW3.Navigation) is not None:
            break
        else:
            time.sleep(0.5)
            
    Waited.click(Found.icon(ICON.GXW3.Navigation))
    

    