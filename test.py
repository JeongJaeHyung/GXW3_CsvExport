from module import Waited, Get, Found

def work():
    print("LOG: before_sequence.work() called")
    Waited.click(Get.center_location("GXW2_Navigation"), 0.05)
    Waited.key_press('up')
    while True:
        Waited.key_press('pageup')
        if Found.icon('GXW2_Parameter') is not None:
            print("--------------------------------------GXW2 Parameter Found")
            return

work()