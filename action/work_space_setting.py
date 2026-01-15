from module import Waited, Just

def work():
    Waited.Found.key_press("information1", "enter", 60)
    Waited.Found.key_press("information2", "enter", 20)
    Waited.Found.key_press("warning", "enter", 20)
    Just.key_press("enter")