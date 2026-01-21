import os
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QFileDialog
from UI.elements.drag_drop import ActionButton
import core

class PathSelectorElement(QWidget):
    """
    폴더 경로를 선택하고 표시하는 기초 엘리먼트입니다.
    """
    def __init__(self, label_text="찾아보기", env_key="EXPORT_PATH"):
        super().__init__()
        self.env_key = env_key
        self.init_ui(label_text)
        self.load_initial_path()

    def init_ui(self, label_text):
        """레이아웃과 위젯 스타일을 설정합니다."""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) # 외부 여백 제거

        # 경로 표시창
        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("폴더 경로를 선택하세요...")
        self.path_input.setStyleSheet("""
            QLineEdit {
                background-color: #252526;
                border: 1px solid #3d3d3d;
                border-radius: 5px;
                color: #ddd;
                padding: 8px;
            }
        """)
        
        # 폴더 찾기 버튼 (기존 ActionButton 재활용)
        self.browse_btn = ActionButton(label_text, "#444")
        self.browse_btn.clicked.connect(self.open_directory_dialog)
        
        layout.addWidget(self.path_input)
        layout.addWidget(self.browse_btn)

    def load_initial_path(self):
        """core.py를 통해 .env에 저장된 기존 경로를 불러옵니다."""
        # core.py에 해당 키가 없을 경우를 대비해 처리
        import os
        initial_path = os.getenv(self.env_key, "")
        self.path_input.setText(initial_path)

    def open_directory_dialog(self):
        """폴더 선택 다이얼로그를 열고 선택된 경로를 반영합니다."""
        selected_path = QFileDialog.getExistingDirectory(self, "저장 폴더 선택")
        
        if selected_path:
            self.path_input.setText(selected_path)
            # 선택 즉시 .env 파일에 영구 저장
            core.save_setting_to_env(self.env_key, selected_path)
            print(f">>> {self.env_key} 경로가 저장되었습니다: {selected_path}")

    def get_path(self):
        """현재 입력창에 있는 경로를 반환합니다."""
        return self.path_input.text()