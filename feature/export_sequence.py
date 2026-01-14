from package.wait_found_this import wait_found_this # 임포트 방식 통일
from package.key_press import key_press, hotkey_press
from package.center_click import center_click
from core import DELAY

def work():
    export_speed = 0.05
    # 우클릭 후 나타난 메뉴에서 키보드로 선택
    key_press(export_speed, 'e') # Export to File
    key_press(export_speed, 'down') # 하위 항목 이동
    key_press(export_speed, 'enter') 
    
    # "Warning" 팝업 혹은 완료창 대기
    wait_found_this("Warning")
    
    # 팝업 처리 시퀀스 (엔터 등)
    key_press(export_speed, 'left')
    key_press(export_speed, 'enter')
    hotkey_press(export_speed, ['alt', 'tab']) # Select the
    hotkey_press(export_speed, ['alt', 'tab']) # Save work window
    key_press(export_speed, 'enter')
    center_click(DELAY, t_center, 'double')
    
    print(">>> [SUCCESS] Local Label 내보내기 완료")