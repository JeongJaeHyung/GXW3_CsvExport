from core import ICON
from module import Waited, Found
from .file_path_setting import work as PathSetting


def work(t_center, file_path_setted):
    print("LOG: export_to_csv.work() called")
    print("│  │  └─(Export to CSV Start)")

    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.right_click(t_center)


    Waited.key_press('e')
    Waited.key_press('down')
    Waited.key_press('enter')
    if Found.icon(ICON.Error.Information2) is not None:
        print("│  │     ├─<Statement Error!>")
        Waited.key_press('enter')
    
    Waited.Found.key_press(ICON.Error.Warning1, 'left', 5, 0.8)
    Waited.key_press('enter', 0.05)
    if file_path_setted is False:
        PathSetting()
    if Found.icon(ICON.Error.Warning1) is not None:
        print("│  │     ├─<CSV is already saved!>")
        Waited.key_press('enter')
        Waited.key_press('esc')
    else:
        Waited.key_press('enter')
        print("│  │     ├─ Success!")

    Waited.key_press('esc', 0.1)
    Waited.hotkey_press(['ctrl', 'shift', 'q'], 0.1)

    Waited.click(Found.icon(ICON.GXW3.Navigation))

    Waited.key_press('up')
    Waited.key_press('up')
    Waited.key_press('enter')
    print("│  │     └─(CSV Export End)")
