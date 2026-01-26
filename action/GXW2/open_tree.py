from module import Found, Just
from .program_export_work import work as ProgramExportWork
from .comment_export_work import work as CommentExportWork
from .bring_to_folder import work as BringToFolder

from core import ICON, NODE_OPEN_TIMEOUT

def work():
    node_list = [
        [ICON.GXW2.GlobalDeviceComment],
        [ICON.GXW2.PS],
        [ICON.GXW2.Scan],
        [ICON.GXW2.Unit, ICON.GXW2.Program1, ICON.GXW2.Program2, ICON.GXW2.POU],
        [ICON.GXW2.PF, ICON.GXW2.Program1, ICON.GXW2.Program2],
        [ICON.GXW2.DeviceInitialValue]
    ]
    pointer = 0
    failed_count = 0

    while True:
        print('- '*200)
        Just.key_press("down")
        search_result = Found.icon_list(node_list[pointer], NODE_OPEN_TIMEOUT)

        if search_result is not None:
            failed_count = 0
            position, target = search_result
            print('-'*300, f"{target} found!")

            if target == ICON.GXW2.DeviceInitialValue:
                BringToFolder()
                Just.hotkey_press(['alt', 'f4'])
                return
            
            elif target in [ICON.GXW2.Program1, ICON.GXW2.Program2]:
                ProgramExportWork(position)
            
            elif target == ICON.GXW2.GlobalDeviceComment:
                pointer += 1
                CommentExportWork(position)
                
            elif target in [ICON.GXW2.Unit, ICON.GXW2.PF]:
                Just.key_press('right')
            
            else:
                Just.key_press('right')
                pointer += 1
        
        elif failed_count >= 5:
            pointer += 1
            failed_count = 0
        
        else:
            failed_count += 1