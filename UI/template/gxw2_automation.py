import os
import time
from PyQt6.QtGui import QColor
import core
from .base_automation import BaseAutomationTemplate
from action.GXW2 import before_sequence, open_tree
from action.GXW3 import compile # 필요한 액션 임포트

class GXW2AutomationTemplate(BaseAutomationTemplate):
    def run_workflow(self, idx, file_path, session_dir):

        print("-------------------------------------------------------------------------------------------------------")
        print("-------------------------G X   W o r k s 2   A u t o   E x p o r t   S t a r t-------------------------")
        print("-------------------------------------------------------------------------------------------------------")

        # 1. 파일별 출력 폴더 생성 및 core 경로 업데이트
        file_name_only = os.path.splitext(os.path.basename(file_path))[0]
        target_file_dir = os.path.join(session_dir, file_name_only)
        os.makedirs(target_file_dir, exist_ok=True)
        core.CURRENT_EXPORT_DIR = target_file_dir #
        core.processed_targets = []

        # 2. UI 상태 업데이트 (작업중 시작)
        self.worker.status_update.emit(idx, "작업중", QColor("#f1c40f"))
        self.worker.file_progress.emit(0)

        # 3. 대상 소프트웨어 실행
        os.startfile(file_path)
        time.sleep(5) 
        
        self.worker.file_progress.emit(30)
        compile.work() #
        
        self.worker.file_progress.emit(60)
        time.sleep(0.5)
        before_sequence.work() #

        self.worker.file_progress.emit(90)
        open_tree.work() #

        # 5. UI 상태 완료 업데이트
        self.worker.status_update.emit(idx, "작업 완료", QColor("#2ecc71"))
        self.worker.file_progress.emit(100)