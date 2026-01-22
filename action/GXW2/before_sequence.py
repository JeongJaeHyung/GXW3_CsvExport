from module import Waited, Get, Found
from core import ICON


def work():
    print("LOG: before_sequence.work() called")
    Waited.click(Get.center_location(ICON.GXW2.Navigation), 0.05)
    Waited.key_press('up')
    while True:
        Waited.key_press('pageup')
        if Found.icon(ICON.GXW2.Parameter) is not None:
            print("--------------------------------------Project Found")
            return