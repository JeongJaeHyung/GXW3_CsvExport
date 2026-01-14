import pyautogui
import time
from core import DELAY
from .wait_found_this import wait_found_this



# ==============================================================================================================
# 즉시 키 입력을 수행합니다.
# ==============================================================================================================
class Just:
    @staticmethod
    def key_press(key):
        """기다린 후 키 입력"""
        pyautogui.press(key)
        print(f">>> [Just] {key} 입력 완료")

    @staticmethod
    def hotkey_press(hotkey_list):
        """기다린 후 조합키 입력"""
        pyautogui.hotkey(*hotkey_list)
        print(f">>> [Just] {hotkey_list} 입력 완료")



# ==============================================================================================================
# 일정 시간동안 대기한 뒤 키 입력을 수행합니다.
# ==============================================================================================================
class Waited:
    @staticmethod
    def key_press(key, interval=DELAY):
        """기다린 후 키 입력"""
        time.sleep(interval)
        Just.key_press(key)
        print(f">>> [Just] {key} 입력 완료")

    @staticmethod
    def hotkey_press(hotkey_list, interval=DELAY):
        """기다린 후 조합키 입력"""
        time.sleep(interval)
        Just.hotkey_press(hotkey_list)
        print(f">>> [Just] {hotkey_list} 입력 완료")



# ==============================================================================================================
# 특정 아이콘을 발견한 경우 키 입력을 수행합니다.
# ==============================================================================================================
class Found:
    @staticmethod
    def key_press(icon_key, key):
        """아이콘을 발견하면 키 입력"""
        if wait_found_this(icon_key):
            Just.key_press(key)
            print(f">>> [Found] {icon_key} 확인 후 {key} 입력 완료")
        else:
            print(f"!!! [Found] {icon_key}를 찾지 못해 {key} 입력을 취소합니다.")

    @staticmethod
    def hotkey_press(icon_key, hotkey_list):
        """아이콘을 발견하면 조합키 입력"""
        if wait_found_this(icon_key):
            Just.hotkey_press(hotkey_list)
            print(f">>> [Found] {icon_key} 확인 후 {hotkey_list} 입력 완료")