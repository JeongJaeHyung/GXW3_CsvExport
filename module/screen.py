import logging
import time
import pyautogui
from core import ICONS, CONFIDENCE, DEFAULT_TIMEOUT 

logging.basicConfig(level=logging.INFO, format='%(message)s')

class Found():
    @staticmethod
    def icon(icon_key, timeout=DEFAULT_TIMEOUT, confidence=CONFIDENCE):
        logging.info(f"LOG: screen.Found.icon(icon_key={icon_key}, timeout={timeout}, confidence={confidence}) called")
        start_time = time.time()

        while True:
            try:
                confirm_btn = pyautogui.locateCenterOnScreen(ICONS[icon_key], confidence=confidence)
                
                if confirm_btn:
                    return confirm_btn
            
            except pyautogui.ImageNotFoundException:
                pass
            
            if time.time() - start_time > timeout:
                return None
            
            time.sleep(0.1) 
    
    @staticmethod
    def icon_list(icon_key_list, timeout=0):
        logging.info(f"LOG: screen.Found.icon_list(icon_key_list={icon_key_list}, timeout={timeout}) called")
        for key in icon_key_list:
            confirm_btn = Found.icon(key, timeout=timeout)
            if confirm_btn is not None:
                return confirm_btn, key
        return None