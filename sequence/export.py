from module import Waited, Found

def work(t_center):
    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.double_click(t_center)
    Waited.right_click(t_center)

    # 우클릭 후 나타난 메뉴에서 키보드로 선택
    Waited.key_press('e') # Export to File
    Waited.key_press('down') # 하위 항목 이동
    Waited.key_press('enter') 
    
    # 팝업 처리 시퀀스 (엔터 등)
    Found.key_press("Warning", 'left')
    Waited.key_press('enter')
    Waited.hotkey_press(['alt', 'tab']) # Select the
    Waited.hotkey_press(['alt', 'tab']) # Save work window
    Waited.key_press('enter')

    Found.double_click("done", t_center)
    
    print(">>> [SUCCESS] Local Label 내보내기 완료")