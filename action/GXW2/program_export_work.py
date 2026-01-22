from module import Waited, Found
from core import ICON



def work(t_center):
    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.right_click(t_center)

    Waited.key_press('O')

    Waited.Found.key_press(ICON.GXW2.Warning, 'left', 5, 0.8) # Warning Pop-up wait
    Waited.key_press('enter')

    Waited.key_press('enter')

    if Found.icon(ICON.Error.Warning2) is not None:
        Waited.key_press('enter')
        Waited.key_press('esc')
    else:
        print("done")

    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.click(Found.icon(ICON.GXW2.Navigation))

    Waited.key_press('left')
    Waited.key_press('left')