# Project/package/__init__.py
from . import keyboard as kp
from . import mouse as cl
from . import screen as ic
from . import location as lc


# 패키지 레벨에서 바로 접근 가능한 통합 클래스 정의
class Just:
    key_press = kp.Just.key_press
    hotkey_press = kp.Just.hotkey_press
    # 마우스 Just 기능이 click.py에 있다면 추가

class Waited:
    # 키보드 동작
    key_press = kp.Waited.key_press
    hotkey_press = kp.Waited.hotkey_press
    
    # 마우스 동작
    double_click = cl.Waited.double_click
    right_click = cl.Waited.right_click

class Found:
    icon = ic.Found.icon
    # Key_press's
    key_press = kp.Found.key_press
    hotkey_press = kp.Found.hotkey_press
    
    # click's
    double_click = cl.Found.double_click



class Get:
    center_location = lc.Get.center_location