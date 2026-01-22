from module import Just, Found, Waited
from .program_export_work import work as ExportWork
from .device_export_work import work as DeviceExportWork
from core import NODE_OPEN_TIMEOUT, ICON



def work():
    print("LOG: open_tree.work() called")
    node_list = [
        ICON.GXW3.Program,
        ICON.GXW3.Scan,
        ICON.GXW3.Unit,
        ICON.GXW3.Comment,
        ICON.GXW3.Folder,
        ICON.GXW3.Device,
        ICON.GXW3.ProgramBlock1,
        ICON.GXW3.ProgramBlock2,
        ICON.GXW3.Parameter,
    ]
    start_point, end_point = 0, 5

    base_nodes = [ICON.GXW3.Program, ICON.GXW3.Scan, ICON.GXW3.Unit, ICON.GXW3.Folder, ICON.GXW3.Device] # Program, Scan, Unit, Folder
    programblock = [ICON.GXW3.ProgramBlock1, ICON.GXW3.ProgramBlock2] # ProgramBlock1, ProgramBlock2

    Waited.click(Found.icon(ICON.GXW3.Navigation))

    while True:
        Just.key_press("down")
        if (result := Found.icon_list(node_list[start_point:end_point], NODE_OPEN_TIMEOUT)) is not None:
            position, target = result
            print(f"{node_list[start_point:end_point]}")
            print(f"<<<<<<<<<<<<<<<<<<<<<{target} Found!>>>>>>>>>")

            if target in ICON.GXW3.Parameter:
                print("--------------------------------------Parameter Found")
                Just.hotkey_press(['alt', 'f4'])
                return
            
            elif target in programblock:
                print("--------------------------------------ProgramBlock Found")
                ExportWork(position)

            elif target in base_nodes:
                print("--------------------------------------Base Node Found")
                Just.key_press('enter')
                if target == ICON.GXW3.Scan:
                    start_point, end_point = 2, 9

            elif target in ICON.GXW3.Comment:
                DeviceExportWork(position)