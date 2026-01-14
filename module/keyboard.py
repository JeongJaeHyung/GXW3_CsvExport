import pyautogui
import time
from core import DEFAULT_DELAY, KEY_PRESS_DELAY
from . import screen



# ==============================================================================================================
# 즉시 키 입력을 수행합니다.
# ==============================================================================================================
class Just:
    @staticmethod
    def key_press(key):
        time.sleep(KEY_PRESS_DELAY)
        pyautogui.press(key)
        print(f">>> [Just] {key} 입력 완료")

    @staticmethod
    def hotkey_press(hotkey_list):
        time.sleep(KEY_PRESS_DELAY)
        pyautogui.hotkey(*hotkey_list)
        print(f">>> [Just] {hotkey_list} 입력 완료")



# ==============================================================================================================
# 일정 시간동안 대기한 뒤 키 입력을 수행합니다.
# ==============================================================================================================
class Waited:
    @staticmethod
    def key_press(key, interval=DEFAULT_DELAY):
        time.sleep(KEY_PRESS_DELAY+interval)
        Just.key_press(key)
        print(f">>> [Just] {key} 입력 완료")

    @staticmethod
    def hotkey_press(hotkey_list, interval=DEFAULT_DELAY):
        time.sleep(KEY_PRESS_DELAY+interval)
        Just.hotkey_press(hotkey_list)
        print(f">>> [Just] {hotkey_list} 입력 완료")



# ==============================================================================================================
# 특정 아이콘을 발견한 경우 키 입력을 수행합니다.
# ==============================================================================================================
class Found:
    @staticmethod
    def key_press(icon_key, key):
        if screen.Found.icon(icon_key):
            Just.key_press(key)
    
    @staticmethod
    def hotkey_press(icon_key, hotkey_list):
        if screen.Found.icon(icon_key):
            Just.hotkey_press(hotkey_list)