import pyautogui
from package.click import Waited
from package.get_location import Get



def expand_all_of(icon_key):
    """지정한 아이콘([+] 상태)이 화면에서 더 이상 발견되지 않을 때까지 반복 확장"""
    while True:
        try:
            # 매번 화면을 새로 스캔하여 첫 번째 항목만 찾음
            location = Get.center_location(icon_key)
            if not location:
                break # 더 이상 열 항목이 없으면 루프 탈출
            
            print(f"[{icon_key.upper()}] 확장 중...")
            Waited.double_click(location)

        except pyautogui.ImageNotFoundException:
            break
