from core import CURRENT_EXPORT_DIR, ICON
import pyperclip
from module import Waited, Found


def work(t_center):
    print("LOG: export_to_csv.work() called")
    print("│  │  └─(Export to CSV Start)")

    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.right_click(t_center)


    Waited.key_press('e')
    Waited.key_press('down')
    Waited.key_press('enter')
    if Found.icon(ICON.GXW3.Statement) is not None:
        print("│  │     ├─<Statement Error!>")
        Waited.key_press('enter')
    
    Waited.Found.key_press(ICON.GXW3.Warning, 'left', 5, 0.8)
    Waited.key_press('enter', 0.05)

    Waited.click(Found.icon(ICON.ETC.WindowsFolder))
    print(f"CURRENT_EXPORT_DIR : {CURRENT_EXPORT_DIR}")
    pyperclip.copy(CURRENT_EXPORT_DIR)
    Waited.hotkey_press(['ctrl', 'v'])

    Waited.hotkey_press(['alt', 'tab'])
    Waited.hotkey_press(['alt', 'tab'])

    Waited.key_press('enter', 0.05)

    if Found.icon(ICON.GXW3.Warning) is not None:
        print("│  │     ├─<CSV is already saved!>")
        Waited.key_press('enter')
        Waited.key_press('esc')
    else:
        print("│  │     ├─ Success!")

    Waited.key_press('esc', 0.1)
    Waited.hotkey_press(['ctrl', 'shift', 'q'], 0.1)

    Waited.click(Found.icon(ICON.GXW3.Navigation))

    Waited.key_press('up')
    Waited.key_press('up')
    Waited.key_press('enter')
    print("│  │     └─(CSV Export End)")
