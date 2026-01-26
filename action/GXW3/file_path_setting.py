from module import Waited, Found
import pyperclip
import core


def work(SAVE_DIR):
    print("LOG: program_export_work.work() called")
    print(f"CURRENT_EXPORT_DIR : {core.CURRENT_EXPORT_DIR}")
    pyperclip.copy(SAVE_DIR)
    Found.icon(core.ICON.ETC.FilePathSetting, 5)
    Waited.hotkey_press(['ctrl', 'v'])
    Waited.key_press('enter')
    Waited.key_press('enter')