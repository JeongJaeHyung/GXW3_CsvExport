from package.key_press import Waited, Found
from package.click import Waited as C_Waited
from package.click import Found as C_Found
#from core import DELAY

def work(t_center):
    #export_speed = 0.05
    # 작업 전 환경조건 개선
    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    C_Waited.double_click(t_center)
    C_Waited.right_click(t_center)

    # 우클릭 후 나타난 메뉴에서 키보드로 선택
    Waited.key_press('e') # Export to File
    Waited.key_press('down') # 하위 항목 이동
    Waited.key_press('enter') 
    
    # 팝업 처리 시퀀스 (엔터 등)
    Found.key_press("Warning", 'left')
    Waited.key_press('enter')
    for _ in range(2):Waited.hotkey_press(['alt', 'tab']) # Save work window
    Waited.key_press('enter')

    C_Found.double_click("done", t_center)
    
    print(">>> [SUCCESS] Local Label 내보내기 완료")