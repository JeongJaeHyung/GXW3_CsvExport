import pyautogui
import time
from core import DEFAULT_DELAY
from . import screen





# ==============================================================================================================
# 즉시 마우스 클릭 동작을 수행합니다.
# ==============================================================================================================
class Just:
    @staticmethod
    def click(location): pyautogui.click(location)
    
    @staticmethod
    def double_click(location): pyautogui.doubleClick(location)
    
    @staticmethod
    def right_click(location): pyautogui.rightClick(location)



# ==============================================================================================================
# 일정 시간동안 대기한 뒤 마우스 클릭 동작을 수행합니다.
# ==============================================================================================================
class Waited:
    @staticmethod
    def click(location, interval=DEFAULT_DELAY):
        time.sleep(interval)
        Just.click(location)

    @staticmethod
    def double_click(location, interval=DEFAULT_DELAY):
        time.sleep(interval)
        Just.double_click(location)

    @staticmethod
    def right_click(location, interval=DEFAULT_DELAY):
        time.sleep(interval)
        Just.right_click(location)



# ==============================================================================================================
# 일정 시간동안 대기한 뒤 마우스 클릭 동작을 수행합니다.
# ==============================================================================================================
class Found:
    @staticmethod
    def click(icon_key, location):
        if screen.Found.icon(icon_key):
            Just.click(location)
        else:
            print(f"!!! [Found] {icon_key}를 찾지 못해 클릭을 취소합니다.")

    @staticmethod
    def double_click(icon_key, location):
        if screen.Found.icon(icon_key):
            Just.double_click(location)
        else:
            print(f"!!! [Found] {icon_key}를 찾지 못해 더블클릭을 취소합니다.")

    @staticmethod
    def right_click(icon_key, location):
        if screen.Found.icon(icon_key):
            Just.right_click(location)
        else:
            print(f"!!! [Found] {icon_key}를 찾지 못해 우클릭을 취소합니다.")