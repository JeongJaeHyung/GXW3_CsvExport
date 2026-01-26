import os
from pathlib import Path
from module import Just, Found, Waited
from .program_export_work import work as ExportWork
from .device_export_work import work as DeviceExportWork
from core import NODE_OPEN_TIMEOUT, ICON
import core


def work():
    print("LOG: open_tree.work() called")

    nodes = [
        [ICON.GXW3.Program], # +1
        [ICON.GXW3.Scan], # +1
        [ICON.GXW3.Unit, ICON.GXW3.Folder, ICON.GXW3.ProgramBlock, ICON.GXW3.Device], # Found device +1
        [ICON.GXW3.Comment], # +1
        [ICON.GXW3.Parameter]
    ]
    

    SAVE_DIR = Path(core.CURRENT_EXPORT_DIR) / "wrrap"
    pointer, unit_number, folder_number = 0, 0, 0
    file_path_setted = False

    print(f"pointer : {pointer}, unit_number : {unit_number}, folder_number : {folder_number}")
    print(f"SAVE_DIR : {SAVE_DIR}")
    print(f"file_path_setted : {file_path_setted}")



    Waited.click(Found.icon(ICON.GXW3.Navigation))

    while True:
        print(f"SAVE_DIR : {SAVE_DIR}")
        Just.key_press("down")
        # 작업 대상 아이콘 판별
        if (result := Found.icon_list(nodes[pointer], NODE_OPEN_TIMEOUT)) is not None:
            position, target = result


            if target == ICON.GXW3.Parameter:
                Just.hotkey_press(['alt', 'f4'])
                return            


            elif target == ICON.GXW3.ProgramBlock:
                ExportWork(position, file_path_setted, SAVE_DIR)
                if Found.icon(ICON.GXW3.LineChange) is None:
                    SAVE_DIR = SAVE_DIR.parent
                    file_path_setted = False
                else:
                    file_path_setted = True
                
            


            elif target == ICON.GXW3.Comment:
                DeviceExportWork(position)
                pointer += 1
            

            elif target in ICON.GXW3.Folder: 
                folder_number += 1
                file_path_setted = False
                SAVE_DIR = SAVE_DIR / f"Folder-{folder_number:02d}"
                os.mkdir(f"{SAVE_DIR}")
                Just.key_press('enter')
            

            elif target == ICON.GXW3.Unit:
                SAVE_DIR = SAVE_DIR.parent
                file_path_setted = False
                unit_number += 1
                SAVE_DIR = SAVE_DIR / f"Unit-{unit_number:02d}"
                os.mkdir(f"{SAVE_DIR}")
                Just.key_press('enter')


            else:
                pointer += 1
                Just.key_press('enter')
