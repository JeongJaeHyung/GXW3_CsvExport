from module import Waited, Found
from core import ICON



def work(t_center):
    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.right_click(t_center)

    Waited.key_press('O')

    Waited.key_press('left')
    Waited.key_press('enter')

    Waited.key_press('enter')

    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.click(Found.icon(ICON.GXW2.Navigation))

    Waited.key_press('left')
    Waited.key_press('left')