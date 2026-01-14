import time
import pyautogui
from feature.export_sequence import work as export_sequence
from core import ICONS, CONFIDENCE, DELAY, processed_targets


def work(icon_key):
    targets = list(pyautogui.locateAllOnScreen(ICONS[icon_key], confidence=CONFIDENCE))
    for t_box in targets:
        t_center = pyautogui.center(t_box)
        if not any(abs(t_center.x - p[0]) < 5 and abs(t_center.y - p[1]) < 5 for p in processed_targets):
            export_sequence(t_center)
            time.sleep(0.1)
            processed_targets.append((t_center.x, t_center.y))
            time.sleep(DELAY)