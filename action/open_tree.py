from module import Just, Found
from .export_to_csv import work as ExportWork
from core import NODE_OPEN_TIMEOUT



def work():
    node_list = [
        "Program",
        "Scan",
        "Unit",
        "Folder",
        "ProgramBlock1",
        "ProgramBlock2",
        "Parameter",
    ]
    status = 0

    while True:
        Just.key_press("down")
        result = Found.icon_list(node_list[status:], NODE_OPEN_TIMEOUT)
        if result is not None:
            position, target = result[0], result[1]
            print(target, position)
            if target == "Parameter":
                return
            elif target == "ProgramBlock1" or "ProgramBlock2":
                ExportWork(position)

            elif target == "Program" or "Scan" or "Unit":
                status += 1