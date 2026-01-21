from module import Found, Just
from program_export_work import work as ProgramExportWork
#from device_export_work import work as DeviceExportWork
from core import ICON

def work():
    node_list = [
        ICON.GXW2.GlobalDeviceComment,
        ICON.GXW2.ProgramSetting,
        ICON.GXW2.Scan,
        ICON.GXW2.Unit,
        ICON.GXW2.Program,
        ICON.GXW2.END
    ]
    base_nodes = [ICON.GXW2.ProgramSetting, ICON.GXW2.Scan, ICON.GXW2.Unit]

    while True:
        Just.key_press("down")

        if (result := Found.icon_list(node_list, 1)) is not None:
            position, target = result

            if target in ICON.GXW2.END:
                return
            
            elif target in ICON.GXW2.Program:
                ProgramExportWork(position)


            elif target in ICON.GXW2.GlobalDeviceComment:
                pass

            elif target in base_nodes:
                Just.key_press('right')
