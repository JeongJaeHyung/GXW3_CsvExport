import pyautogui
import time
from core import CONFIDENCE

def center_click(time_interval: float, location, type='single'):
    """
    click the center of the target image, after waiting for time_interval seconds
    time_interval: float, seconds
    location: pyautogui.Point, the coordinate to click
    type: str, 'single' or 'double' click
    """
    time.sleep(time_interval)
    if isinstance(location, str):
        location = pyautogui.locateCenterOnScreen(location, confidence=CONFIDENCE)

    if location:
        if type == 'single' or type is None:
            pyautogui.click(location)
        elif type == 'double':
            pyautogui.doubleClick(location)
        elif type == 'right':
            pyautogui.rightClick(location)
    else:
        print(f"Target location {location} not found on screen.")