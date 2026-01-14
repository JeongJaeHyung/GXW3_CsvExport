import pyautogui
from module import Found
counter = 0

pyautogui.scroll(99999)
print(Found.icon("scroll", 15))



"""

while True:
    counter += 1
    print(counter)
    pyautogui.scroll(-100)
    if Found.icon("end", 0.1) is not None:
        print("Done")
        break

"""
