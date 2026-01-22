from module import Waited, Found
import pyperclip
from core import ICON
import core

def work():
    print("LOG: program_export_work.work() called")
    Waited.click(Found.icon(ICON.ETC.FilePathSetting))
    print(f"CURRENT_EXPORT_DIR : {core.CURRENT_EXPORT_DIR}")
    pyperclip.copy(core.CURRENT_EXPORT_DIR)
    Waited.hotkey_press(['ctrl', 'v'])
    Waited.key_press('enter')
    Waited.key_press('enter')
    Waited.key_press('enter')
    Waited.key_press('enter')