from module import Waited, Get
from core import ICON
import time

def work():
    print("LOG: before_sequence.work() called")
    time.sleep(0.1)
    Waited.click(Get.center_location(ICON.GXW2.ProjectProperty))
    Waited.key_press('c')
    return