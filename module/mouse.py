import pyautogui
import time
from core import DEFAULT_DELAY
from . import screen





# ==============================================================================================================
# 즉시 마우스 클릭 동작을 수행합니다.
# ==============================================================================================================
class Just:
    @staticmethod
    def click(location): 
        print(f"LOG: mouse.Just.click(location={location}) called")
        pyautogui.click(location)
    
    @staticmethod
    def double_click(location): 
        print(f"LOG: mouse.Just.double_click(location={location}) called")
        pyautogui.doubleClick(location)
    
    @staticmethod
    def right_click(location): 
        print(f"LOG: mouse.Just.right_click(location={location}) called")
        pyautogui.rightClick(location)



# ==============================================================================================================
# 일정 시간동안 대기한 뒤 마우스 클릭 동작을 수행합니다.
# ==============================================================================================================
class Waited:
    @staticmethod
    def click(location, interval=DEFAULT_DELAY):
        print(f"LOG: mouse.Waited.click(location={location}, interval={interval}) called")
        time.sleep(interval)
        Just.click(location)

    @staticmethod
    def double_click(location, interval=DEFAULT_DELAY):
        print(f"LOG: mouse.Waited.double_click(location={location}, interval={interval}) called")
        time.sleep(interval)
        Just.double_click(location)

    @staticmethod
    def right_click(location, interval=DEFAULT_DELAY):
        print(f"LOG: mouse.Waited.right_click(location={location}, interval={interval}) called")
        time.sleep(interval)
        Just.right_click(location)



# ==============================================================================================================
# 일정 시간동안 대기한 뒤 마우스 클릭 동작을 수행합니다.
# ==============================================================================================================
class Found:
    @staticmethod
    def click(icon_key, location):
        print(f"LOG: mouse.Found.click(icon_key={icon_key}, location={location}) called")
        if screen.Found.icon(icon_key):
            Just.click(location)

    @staticmethod
    def double_click(icon_key, location):
        print(f"LOG: mouse.Found.double_click(icon_key={icon_key}, location={location}) called")
        if screen.Found.icon(icon_key):
            Just.double_click(location)

    @staticmethod
    def right_click(icon_key, location):
        print(f"LOG: mouse.Found.right_click(icon_key={icon_key}, location={location}) called")
        if screen.Found.icon(icon_key):
            Just.right_click(location)