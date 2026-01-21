import pyautogui
from core import ICONS, CONFIDENCE

class Get():
    @staticmethod
    def center_location(image_path):
        print(f"LOG: location.Get.center_location(image_path={image_path}) called")
        """이미지의 중앙 좌표를 반환합니다."""
        location = pyautogui.locateCenterOnScreen(ICONS[image_path], confidence=CONFIDENCE)
        return location