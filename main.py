import os
import sys
import time
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QColor

import core
from action import PreWork, GeneralWork, ShareWork
from UI.widget.top_section import TopSectionWidget
from UI.widget.bottom_section import BottomSectionWidget
from UI.elements.progress_bar import ProgressBarElement

class AutomationWorker(QThread):
    file_progress = pyqtSignal(int)
    total_progress = pyqtSignal(int)
    status_update = pyqtSignal(int, str, QColor) 

    def __init__(self, files, session_dir):
        super().__init__()
        self.files = files
        self.session_dir = session_dir

    def run(self):
        total_files = len(self.files)
        
        for idx, file_path in enumerate(self.files):
            try:
                # [폴더 생성] 파일명으로 하위 폴더 생성 (확장자 제외)
                file_name_only = os.path.splitext(os.path.basename(file_path))[0]
                target_file_dir = os.path.join(self.session_dir, file_name_only)
                os.makedirs(target_file_dir, exist_ok=True)

                print(target_file_dir)
                
                # core.py에 현재 작업 폴더 정보 업데이트
                core.CURRENT_EXPORT_DIR = target_file_dir
                
                self.status_update.emit(idx, "작업중", QColor("#f1c40f"))
                
                os.startfile(file_path)
                time.sleep(5) 
                
                core.processed_targets = []
                
                # 자동화 시퀀스 실행
                self.file_progress.emit(10)
                PreWork.work_space_setting()
                
                self.file_progress.emit(30)
                PreWork.before_sequence()
                
                self.file_progress.emit(50)
                ShareWork.compile.work()
                
                self.file_progress.emit(80)
                GeneralWork.open_tree()
                
                self.status_update.emit(idx, "작업 완료", QColor("#2ecc71"))
                self.file_progress.emit(100)

            except Exception as e:
                print(f"!!! [{os.path.basename(file_path)}] 에러 발생: {e}")
                self.status_update.emit(idx, "실패", QColor("#e74c3c"))
            
            self.total_progress.emit(int((idx + 1) / total_files * 100))

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GX Works3 Auto Exporter v1.0")
        self.resize(1100, 750)
        self.setStyleSheet("background-color: #f0f0f0; color: #333;")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.top_section = TopSectionWidget()
        layout.addWidget(self.top_section)

        self.bottom_section = BottomSectionWidget()
        layout.addWidget(self.bottom_section)

        layout.addWidget(QLabel("<b>전체 작업 진척도</b>"))
        self.total_bar = ProgressBarElement(color="#3498db")
        layout.addWidget(self.total_bar)

        layout.addWidget(QLabel("<b>현재 파일 작업 진척도</b>"))
        self.file_bar = ProgressBarElement(color="#2ecc71")
        layout.addWidget(self.file_bar)

        self.bottom_section.run_btn.clicked.connect(self.start_automation_workflow)

    def start_automation_workflow(self):
        """0. 작업 시작 시 설정 저장 및 폴더 트리 생성"""
        self.top_section.config_table.save_to_env_file()
        
        # 대상 루트 폴더 경로 확인
        root_export_path = self.bottom_section.path_selector.get_path()
        if not root_export_path or not os.path.exists(root_export_path):
            print(">>> [오류] 유효한 대상 폴더를 선택해주세요.")
            return

        # YYYYMMDD_HHMM_GXW3 세션 폴더 생성
        folder_name = datetime.now().strftime("%Y%m%d_%H%M_GXW3")
        session_dir = os.path.join(root_export_path, folder_name)
        os.makedirs(session_dir, exist_ok=True)

        table = self.top_section.file_table
        files = [table.item(i, 1).text() for i in range(table.rowCount())]
        
        if not files:
            return

        self.bottom_section.run_btn.set_running(True)
        self.total_bar.update_value(0)
        self.file_bar.update_value(0)
        
        self.worker = AutomationWorker(files, session_dir)
        self.worker.file_progress.connect(self.file_bar.update_value)
        self.worker.total_progress.connect(self.total_bar.update_value)
        self.worker.status_update.connect(table.update_row_status)
        self.worker.finished.connect(lambda: self.bottom_section.run_btn.set_running(False))
        self.worker.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())