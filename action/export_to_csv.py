from module import Waited, Get

def work(t_center):
    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.right_click(t_center)

    # 우클릭 후 나타난 메뉴에서 키보드로 선택
    Waited.key_press('e') # Export to File
    Waited.key_press('down') # 하위 항목 이동
    Waited.key_press('enter') 
    
    # 팝업 처리 시퀀스 (엔터 등)
    Waited.Found.key_press("ProgramBody", 'left')
    Waited.key_press('enter')
    Waited.key_press('enter')

    Waited.hotkey_press(['ctrl', 'shift', 'q'])

    Waited.click(Get.center_location("Navigation"), 1)

    Waited.key_press('up', 0.1)
    Waited.key_press('up', 0.1)
    Waited.key_press('enter', 0.1)
    
    print(">>> [SUCCESS] Local Label 내보내기 완료")