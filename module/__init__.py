# Project/module/__init__.py
from . import keyboard
from . import mouse
from . import screen
from . import location



class Just:
    key_press = keyboard.Just.key_press
    hotkey_press = keyboard.Just.hotkey_press
    click = mouse.Just.click
    double_click = mouse.Just.double_click
    right_click = mouse.Just.right_click



class Waited:
    key_press = keyboard.Waited.key_press
    hotkey_press = keyboard.Waited.hotkey_press
    click = mouse.Waited.click
    double_click = mouse.Waited.double_click
    right_click = mouse.Waited.right_click


    class Found:
        icon = screen.Found.icon
        key_press = keyboard.Found.key_press
        hotkey_press = keyboard.Found.hotkey_press



class Found:
    icon = screen.Found.icon
    icon_list = screen.Found.icon_list
    click = mouse.Found.click
    double_click = mouse.Found.double_click
    right_click = mouse.Found.right_click



class Get:
    center_location = location.Get.center_location