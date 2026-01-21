from module import Waited, Get, Found
from core import ICON

def work():
    print("LOG: before_sequence.work() called")
    Waited.click(Get.center_location(ICON.GXW3.Navigation), 0.05)
    while True:
        Waited.key_press('pageup')
        if Found.icon(ICON.GXW3.Project) is not None:
            print("--------------------------------------Project Found")
            return