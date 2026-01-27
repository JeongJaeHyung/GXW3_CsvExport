from module import Waited, Found
from core import ICON

def work():
    print("LOG: work_space_setting.work() called")
    pop_up_list = {
        ICON.Error.Information3,# enter
        ICON.Error.Warning2, # left, enter
        ICON.Error.Danger1, # restart
    }
    status = 0
    while status < 3:
        print("│  ├─{Workspace Setting Sequence}")

        if Found.