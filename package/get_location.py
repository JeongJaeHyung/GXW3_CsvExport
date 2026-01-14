import pyautogui
from core import ICONS, CONFIDENCE

class Get():
    @staticmethod
    def center_location(image_path):
        """이미지의 중앙 좌표를 반환합니다."""
        location = pyautogui.locateCenterOnScreen(ICONS[image_path], confidence=CONFIDENCE)
        if location:
            print(f">>> [Get] 이미지 위치 발견: {location}")
        else:
            print(f"!!! [Get] 이미지 위치를 찾지 못했습니다: {image_path}")
        return location