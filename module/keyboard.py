import pyautogui
import time
from core import DEFAULT_DELAY, KEY_PRESS_DELAY, DEFAULT_TIMEOUT, CONFIDENCE
from . import screen



# ==============================================================================================================
# 즉시 키 입력을 수행합니다.
# ==============================================================================================================
class Just:
    @staticmethod
    def key_press(key):
        print(f"LOG: keyboard.Just.key_press(key={key}) called")
        time.sleep(KEY_PRESS_DELAY)
        pyautogui.press(key)

    @staticmethod
    def hotkey_press(hotkey_list):
        print(f"LOG: keyboard.Just.hotkey_press(hotkey_list={hotkey_list}) called")
        time.sleep(KEY_PRESS_DELAY)
        pyautogui.hotkey(*hotkey_list)



# ==============================================================================================================
# 일정 시간동안 대기한 뒤 키 입력을 수행합니다.
# ==============================================================================================================
class Waited:
    @staticmethod
    def key_press(key, interval=DEFAULT_DELAY):
        print(f"LOG: keyboard.Waited.key_press(key={key}, interval={interval}) called")
        time.sleep(KEY_PRESS_DELAY+interval)
        Just.key_press(key)

    @staticmethod
    def hotkey_press(hotkey_list, interval=DEFAULT_DELAY):
        print(f"LOG: keyboard.Waited.hotkey_press(hotkey_list={hotkey_list}, interval={interval}) called")
        time.sleep(KEY_PRESS_DELAY+interval)
        Just.hotkey_press(hotkey_list)



# ==============================================================================================================
# 특정 아이콘을 발견한 경우 키 입력을 수행합니다.
# ==============================================================================================================
class Found:
    @staticmethod
    def key_press(icon_key, key, timeout=DEFAULT_TIMEOUT, confidence=CONFIDENCE):
        print(f"LOG: keyboard.Found.key_press(icon_key={icon_key}, key={key}, timeout={timeout}, confidence={confidence}) called")
        if screen.Found.icon(icon_key, timeout, confidence):
            Just.key_press(key)
    
    @staticmethod
    def hotkey_press(icon_key, hotkey_list, timeout=DEFAULT_TIMEOUT, confidence=CONFIDENCE):
        print(f"LOG: keyboard.Found.hotkey_press(icon_key={icon_key}, hotkey_list={hotkey_list}, timeout={timeout}, confidence={confidence}) called")
        if screen.Found.icon(icon_key, timeout, confidence):
            Just.hotkey_press(hotkey_list)