import pyautogui
import time

def key_press(time_interval: float, key):
    """
    press the key, after waiting for time_interval seconds
    time_interval: float, seconds
    key: str, the key to be pressed
    """
    time.sleep(time_interval)
    pyautogui.press(key)

def hotkey_press(time_interval, hotkey_list):
    """
    press the hotkey combination, after waiting for time_interval seconds
    time_interval: int, milliseconds
    hotkey_list: list of str, the hotkey combination to be pressed
    """
    time.sleep(time_interval)
    pyautogui.hotkey(*hotkey_list)