import pyautogui
from core import CONFIDENCE

class Get():
    @staticmethod
    def center_location(icon_path):
        print(f"LOG: location.Get.center_location(icon_path={icon_path}) called")
        """이미지의 중앙 좌표를 반환합니다."""
        location = pyautogui.locateCenterOnScreen(icon_path, confidence=CONFIDENCE)
        return location