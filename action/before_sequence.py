from module import Waited, Get, Found

def work():
    Waited.click(Get.center_location("Navigation"), 0.05)
    while True:
        Waited.key_press('pageup')
        if Found.icon('Project') is not None:
            return