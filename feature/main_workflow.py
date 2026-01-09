import time
import pyautogui
from package.center_click import center_click
from package.key_press import hotkey_press
from feature.export_sequence import work as export_sequence
from core import ICONS, CONFIDENCE, DELAY, processed_targets


def work(icon_key):
    targets = list(pyautogui.locateAllOnScreen(ICONS[icon_key], confidence=CONFIDENCE))
    for t_box in targets:
        t_center = pyautogui.center(t_box)
        if not any(abs(t_center.x - p[0]) < 5 and abs(t_center.y - p[1]) < 5 for p in processed_targets):
            hotkey_press(DELAY, ['ctrl', 'shift', 'q'])
            center_click(DELAY, t_center, 'double')
            center_click(DELAY, t_center, 'right')
            export_sequence()
            center_click(0.15, t_center, 'double')
            time.sleep(0.1)
            processed_targets.append((t_center.x, t_center.y))
            time.sleep(DELAY)