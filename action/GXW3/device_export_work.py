import time
import threading
from module import Waited, Found
from .comment_move import work as CommentMove

from core import ICON

def work(t_center):
    print("LOG: program_export_work.work() called")
    Waited.hotkey_press(['ctrl', 'shift', 'q'])
    Waited.right_click(t_center)

    Waited.key_press('e')
    Waited.key_press('left')
    Waited.key_press('enter')

    Waited.key_press('enter')

    Waited.key_press('enter')

    while True:
        if (position := Found.icon(ICON.GXW3.Navigation)) is not None:
            move_thread = threading.Thread(target=CommentMove, daemon=True)
            move_thread.start()
            Waited.click(position)
            break
        else:
            time.sleep(0.5)
