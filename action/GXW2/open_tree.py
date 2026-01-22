from module import Found, Just
from .program_export_work import work as ProgramExportWork
from .comment_export_work import work as CommentExportWork
from .bring_to_folder import work as BringToFolder

from core import ICON, NODE_OPEN_TIMEOUT

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

        if (result := Found.icon_list(node_list, NODE_OPEN_TIMEOUT)) is not None:
            position, target = result

            if target in ICON.GXW2.END:
                BringToFolder()
                return
            
            elif target in ICON.GXW2.Program:
                ProgramExportWork(position)


            elif target in ICON.GXW2.GlobalDeviceComment:
                CommentExportWork(position)

            elif target in base_nodes:
                Just.key_press('right')