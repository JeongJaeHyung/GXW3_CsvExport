import time
import pyautogui
from core import ICONS, CONFIDENCE, DEFAULT_DELAY

class Found():
    def icon(icon_key, timeout=3):
        start_time = time.time()
        print(f">>> [{icon_key}] 대기 시작...")

        while True:
            try:
                # 이미지 찾기 시도
                confirm_btn = pyautogui.locateCenterOnScreen(ICONS[icon_key], confidence=CONFIDENCE)
                
                if confirm_btn:
                    print(f"found it! 위치: {confirm_btn}")
                    return confirm_btn  # 성공 시 좌표 반환
            
            except pyautogui.ImageNotFoundException:
                pass
            
            # 타임아웃 체크
            if time.time() - start_time > timeout:
                print(f"!!! {timeout}초 동안 [{icon_key}] 버튼이 나타나지 않았습니다.")
                return None  # 실패 시 None 반환
                
            time.sleep(DEFAULT_DELAY)