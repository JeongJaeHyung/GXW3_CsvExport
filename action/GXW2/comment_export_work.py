from module import Waited, Found
from core import ICON



def work(t_center):
    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.right_click(t_center)

    Waited.key_press('O')

    Waited.Found.key_press(ICON.Error.Warning2, 'left', 5, 0.8) # Warning Pop-up wait
    Waited.key_press('enter', 0.2)

    Waited.key_press('enter', 0.5)

    Waited.click(Found.icon(ICON.GXW2.Navigation))