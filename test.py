from module import Waited, Get
import time

from core import ICON

time.sleep(5)

while True:
    time.sleep(0.1)
    Waited.click(Get.center_location(ICON.GXW2.ProjectProperty))