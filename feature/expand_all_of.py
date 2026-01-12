import pyautogui
from package.center_click import center_click
from core import ICONS, CONFIDENCE, DELAY



def expand_all_of(icon_key):
    """지정한 아이콘([+] 상태)이 화면에서 더 이상 발견되지 않을 때까지 반복 확장"""
    while True:
        try:
            # 매번 화면을 새로 스캔하여 첫 번째 항목만 찾음
            item = pyautogui.locateCenterOnScreen(ICONS[icon_key], confidence=CONFIDENCE)
            if not item:
                break # 더 이상 열 항목이 없으면 루프 탈출
            
            print(f"[{icon_key.upper()}] 확장 중...")
            center_click(DELAY, item, 'double')

        except pyautogui.ImageNotFoundException:
            break
