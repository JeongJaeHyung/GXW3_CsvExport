from module import Just, Found, Waited
from .program_export_work import work as ExportWork
from .device_export_work import work as DeviceExportWork
from core import NODE_OPEN_TIMEOUT, ICON


def work():
    print("LOG: open_tree.work() called")

    nodes = [
        [ICON.GXW3.Program], # +1
        [ICON.GXW3.Scan], # +1
        [ICON.GXW3.Unit, ICON.GXW3.Folder, ICON.GXW3.ProgramBlock, ICON.GXW3.Device], # Found device +1
        [ICON.GXW3.Comment], # +1
        [ICON.GXW3.Parameter]
    ]
    pointer = 0

    file_path_setted = False
    Waited.click(Found.icon(ICON.GXW3.Navigation))

    while True:
        Just.key_press("down")
        # 작업 대상 아이콘 판별
        if (result := Found.icon_list(nodes[pointer], NODE_OPEN_TIMEOUT)) is not None:
            position, target = result

            # WORK EVENT! | Parameter인 경우 처리
            if target == ICON.GXW3.Parameter:
                Just.hotkey_press(['alt', 'f4'])
                return
            
            # WORK EVENT! | ProgramBlock인 경우 CSV Export 수행
            elif target == ICON.GXW3.ProgramBlock:
                ExportWork(position, file_path_setted)
                file_path_setted = True
            
            # WORK EVENT! | Comment인 경우 CSV Export 수행
            elif target == ICON.GXW3.Comment:
                DeviceExportWork(position)
                pointer += 1
            
            # WORK EVENT! | Unit, Folder의 경우 확장만 하기
            elif target in [ICON.GXW3.Unit, ICON.GXW3.Folder]: 
                Just.key_press('enter')

            else:
                pointer += 1
                Just.key_press('enter')
