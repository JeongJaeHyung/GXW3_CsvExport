import os
import logging
from datetime import datetime
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QPlainTextEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor

# 기존 커스텀 위젯 및 로직 임포트
from UI.widget.top_section import TopSectionWidget
from UI.widget.bottom_section import BottomSectionWidget
from UI.elements.progress_bar import ProgressBarElement
from logic.worker import AutomationWorker
from logic.validator import check_software_dependencies, validate_root_path

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. 의존성 체크 (GX Works 설치 여부)
        check_software_dependencies(self)
        
        # 2. UI 초기화
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("GX Works Auto Exporter v1.2")
        self.resize(1100, 850)
        self.setStyleSheet("background-color: #f0f0f0; color: #333;")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # 섹션 위젯 생성
        self.top_section = TopSectionWidget()
        self.bottom_section = BottomSectionWidget()
        self.total_bar = ProgressBarElement(color="#3498db")
        self.file_bar = ProgressBarElement(color="#2ecc71")

        # 레이아웃 배치
        layout.addWidget(self.top_section)
        layout.addWidget(self.bottom_section)
        
        layout.addWidget(QLabel("<b>전체 작업 진척도</b>"))
        layout.addWidget(self.total_bar)
        layout.addWidget(QLabel("<b>현재 파일 작업 진척도</b>"))
        layout.addWidget(self.file_bar)

        # 로그 영역 UI 구성
        self.setup_log_ui(layout)

        # 메인 버튼 이벤트 연결
        self.bottom_section.run_btn.clicked.connect(self.start_automation_workflow)

    def setup_log_ui(self, parent_layout):
        self.toggle_log_btn = QPushButton("▼ 작업 로그 보기 / 숨기기")
        self.toggle_log_btn.setCheckable(True)
        self.toggle_log_btn.setStyleSheet("""
            QPushButton { background-color: #34495e; color: white; padding: 8px; border: none; font-weight: bold; }
            QPushButton:hover { background-color: #2c3e50; }
        """)
        self.toggle_log_btn.clicked.connect(self.toggle_log_window)
        parent_layout.addWidget(self.toggle_log_btn)

        self.log_console = QPlainTextEdit()
        self.log_console.setReadOnly(True)
        self.log_console.setStyleSheet("""
            background-color: #1e1e1e; color: #dcdcdc; 
            font-family: 'Consolas', monospace; font-size: 10pt;
        """)
        self.log_console.setMinimumHeight(250)
        parent_layout.addWidget(self.log_console)

    def toggle_log_window(self):
        self.log_console.setVisible(not self.log_console.isVisible())

    def add_log(self, text):
        """리다이렉트된 로그를 화면에 표시 (main.py의 시그널과 연결됨)"""
        timestamp = datetime.now().strftime("[%H:%M:%S] ")
        self.log_console.appendPlainText(f"{timestamp}{text}")
        self.log_console.moveCursor(QTextCursor.MoveOperation.End)

    def start_automation_workflow(self):
        # 환경 설정 저장
        self.top_section.config_table.save_to_env_file()
        
        # 경로 확인
        root_path = self.bottom_section.path_selector.get_path()
        if not validate_root_path(root_path):
            QMessageBox.warning(self, "오류", "유효한 대상 폴더를 선택해주세요.")
            return

        # 세션 디렉토리 생성
        session_dir = os.path.join(root_path, datetime.now().strftime("%Y%m%d_%H%M_Export"))
        os.makedirs(session_dir, exist_ok=True)

        # 파일 리스트 추출
        table = self.top_section.file_table
        files = [table.item(i, 1).text() for i in range(table.rowCount()) if table.item(i, 1)]
        
        if not files:
            QMessageBox.information(self, "알림", "작업할 파일이 없습니다.")
            return

        # UI 상태 업데이트 및 스레드 시작
        self.log_console.clear()
        logging.info("⚙️ 시스템 준비 완료. 자동화 세션을 시작합니다.")
        self.bottom_section.run_btn.set_running(True)
        
        self.worker = AutomationWorker(files, session_dir)
        self.worker.file_progress.connect(self.file_bar.update_value)
        self.worker.total_progress.connect(self.total_bar.update_value)
        self.worker.status_update.connect(table.update_row_status)
        self.worker.finished.connect(lambda: self.bottom_section.run_btn.set_running(False))
        self.worker.start()