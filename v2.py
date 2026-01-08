import pyautogui
import time
import os
import sys

# --- 환경 설정 ---
CONFIDENCE = 0.99  # 이미지 인식 정확도 (0.8 권장)
DELAY = 0.05       # 동작 사이의 대기 시간

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# 아이콘 경로 설정
ICONS = {
    "program": resource_path('icons/program.png'),
    "scan":    resource_path('icons/scan.png'),
    "unit":    resource_path('icons/unit.png'),
    "folder":  resource_path('icons/folder.png'),
    "target":  resource_path('icons/target.png'),
    "target2": resource_path('icons/target2.png') # 선택된 노란색 상태
}

def export_sequence():
    """워크플로우 5단계: 우클릭 -> Export to File -> Local Label -> 엔터 2번"""
    time.sleep(DELAY)
    pyautogui.press('e') # Export to File 단축키
    time.sleep(DELAY)
    pyautogui.press('enter') # Execute
    time.sleep(DELAY)
    pyautogui.press('enter') # Execute
    time.sleep(DELAY)
    pyautogui.hotkey('alt', 'tab') # Execute
    time.sleep(DELAY) # 파일 생성 대기
    pyautogui.hotkey('alt', 'tab') # Execute
    time.sleep(DELAY) # 파일 생성 대기
    pyautogui.press('enter') # 완료 확인
    print(">>> [SUCCESS] Local Label 내보내기 완료")

def expand_all_of(icon_key):
    """지정한 아이콘([+] 상태)이 화면에서 더 이상 발견되지 않을 때까지 반복 확장"""
    while True:
        try:
            # 매번 화면을 새로 스캔하여 첫 번째 항목만 찾음
            item = pyautogui.locateCenterOnScreen(ICONS[icon_key], confidence=CONFIDENCE)
            if not item:
                break # 더 이상 열 항목이 없으면 루프 탈출
            
            print(f"[{icon_key.upper()}] 확장 중...")
            pyautogui.doubleClick(item)
            # 트리가 확장되면서 아래 항목들이 밀리는 시간을 충분히 줌

            time.sleep(DELAY) 
        except pyautogui.ImageNotFoundException:
            break

def run_automation():
    
    processed_targets = [] # 타겟 중복 작업 방지를 위한 좌표 저장

    while True:
        # 1~2단계: Program 및 Scan 확장
        expand_all_of("program")
        expand_all_of("scan")

        # 3~4단계: 모든 Unit 및 Folder가 완전히 열릴 때까지 무한 재탐색
        # 폴더 안에 폴더가 있는 중첩 구조도 이 루프에서 모두 처리됨
        expand_all_of("unit")
        expand_all_of("folder")

        # 5단계: Target 작업 (현재 화면에 보이는 모든 타겟 처리)

        targets = list(pyautogui.locateAllOnScreen(ICONS['target'], confidence=CONFIDENCE))
        for t_box in targets:
            t_center = pyautogui.center(t_box)
            # 좌표가 오차 범위(5px) 내에 있으면 이미 처리한 것으로 간주
            if not any(abs(t_center.x - p[0]) < 5 and abs(t_center.y - p[1]) < 5 for p in processed_targets):
                print("[TARGET] 발견! 작업 시작...")
                pyautogui.hotkey('ctrl', 'shift', 'q')
                time.sleep(DELAY)
                pyautogui.doubleClick(t_center)
                time.sleep(DELAY)
                pyautogui.rightClick(t_center)
                time.sleep(DELAY)
                export_sequence()
                print("작업종료")
                time.sleep(DELAY)
                pyautogui.doubleClick(t_center)
                time.sleep(DELAY)
                print("폴더 닫음")
                processed_targets.append((t_center.x, t_center.y))
                time.sleep(DELAY)

        # 더 이상 처리할 항목이 없으면 아래로 스크롤 (100개 유닛 대응)
        pyautogui.scroll(-2)
        time.sleep(1.0)
        
        # [Fail-safe] 마우스를 화면 구석으로 밀어넣으면 즉시 중지됨

if __name__ == "__main__":
    run_automation()