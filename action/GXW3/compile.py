from module import Just 

def work():
    print("LOG: compile.work() called")
    Just.key_press("f4")
    Just.hotkey_press(['ctrl', 'shift', 'q'])
    Just.key_press("enter")
    print("--------------------------------------Compile Done")