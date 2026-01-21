import os
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QFileDialog
from PyQt6.QtCore import pyqtSignal
import core

class PathSelectorElement(QWidget):
    """
    폴더를 선택하고 그 경로를 .env에 영구 저장하는 독립 엘리먼트입니다.
    """
    # 경로가 변경되었을 때 외부로 알려주는 시그널
    path_changed = pyqtSignal(str)

    def __init__(self, env_key="EXPORT_PATH"):
        super().__init__()
        self.env_key = env_key
        self.init_ui()
        self.load_initial_path()

    def init_ui(self):
        """UI 구성 및 스타일 설정"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 경로 표시창
        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("폴더 경로를 선택하세요...")
        self.path_input.setReadOnly(True)  # 버튼을 통해서만 변경 가능하게 설정
        self.path_input.setStyleSheet("""
            QLineEdit {
                background-color: #252526;
                border: 1px solid #3d3d3d;
                border-radius: 5px;
                color: #ddd;
                padding: 8px;
            }
        """)
        
        # 폴더 찾기 버튼
        self.browse_btn = QPushButton("찾아보기")
        self.browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #444;
                color: white;
                border-radius: 5px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #555; }
        """)
        self.browse_btn.clicked.connect(self.open_directory_dialog)
        
        layout.addWidget(self.path_input)
        layout.addWidget(self.browse_btn)

    def load_initial_path(self):
        """core.py를 통해 .env에서 저장된 기존 경로를 불러옵니다."""
        # os.getenv를 통해 초기값을 가져오거나 core에 정의된 변수 사용
        current_path = os.getenv(self.env_key, "")
        self.path_input.setText(current_path)

    def open_directory_dialog(self):
        """폴더 선택 창을 열고 선택된 경로를 저장합니다."""
        selected_path = QFileDialog.getExistingDirectory(self, "저장 폴더 선택")
        
        if selected_path:
            # 1. 화면 업데이트
            self.path_input.setText(selected_path)
            
            # 2. .env 파일에 영구 저장 (core의 저장 함수 활용)
            if hasattr(core, 'save_setting_to_env'):
                core.save_setting_to_env(self.env_key, selected_path)
            
            # 3. 외부로 변경 알림
            self.path_changed.emit(selected_path)
            print(f">>> {self.env_key} 경로 저장됨: {selected_path}")

    def get_path(self):
        """현재 설정된 경로를 반환합니다."""
        return self.path_input.text()