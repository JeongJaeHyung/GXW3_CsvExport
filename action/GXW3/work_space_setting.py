from module import Waited, Found
from core import ICON
def work():
    print("LOG: work_space_setting.work() called")
    pop_up_list = {
        ICON.GXW3.information1,
        ICON.GXW3.information2,
        ICON.GXW3.warning,
        ICON.GXW3.Statement,
        ICON.GXW3.read_only
    }
    status = 0
    while status < 3:
        print("│  ├─{Workspace Setting Sequence}")

        if Found.icon("tool_bar", 1):
            print("--------------------------------------Workspace Setting is Done")
            return
        
        elif (result := Found.icon_list(pop_up_list, 1)) is not None:
            position, target = result
            print(f"│  │  └─({target} Found!)")
            status = 0
            Waited.key_press("enter")

        else:
            print("│  │  └─<Nothing Found>")
            status += 30