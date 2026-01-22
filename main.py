import os
import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QColor

import core
from UI.widget.top_section import TopSectionWidget
from UI.widget.bottom_section import BottomSectionWidget
from UI.elements.progress_bar import ProgressBarElement
from UI.template.gxw3_automation import GXW3AutomationTemplate

class AutomationWorker(QThread):
    file_progress = pyqtSignal(int)
    total_progress = pyqtSignal(int)
    status_update = pyqtSignal(int, str, QColor) 

    def __init__(self, files, session_dir):
        super().__init__()
        self.files = files
        self.session_dir = session_dir
        # UI 제어 권한을 가진 템플릿 생성
        self.template = GXW3AutomationTemplate(self)

    def run(self):
        total_files = len(self.files)
        for idx, file_path in enumerate(self.files):
            try:
                # 템플릿에 전체 워크플로우 실행 위임
                self.template.run_workflow(idx, file_path, self.session_dir)
            except Exception as e:
                print(f"!!! [{os.path.basename(file_path)}] 에러 발생: {e}")
                self.status_update.emit(idx, "실패", QColor("#e74c3c"))
            
            # 전체 진행도는 Worker에서 직접 관리
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
        self.top_section.config_table.save_to_env_file()
        
        root_export_path = self.bottom_section.path_selector.get_path()
        if not root_export_path or not os.path.exists(root_export_path):
            print(">>> [오류] 유효한 대상 폴더를 선택해주세요.")
            return

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