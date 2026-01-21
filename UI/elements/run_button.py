from PyQt6.QtWidgets import QPushButton

class RunButtonElement(QPushButton):
    """
    자동화 시퀀스를 시작하는 독립 버튼 엘리먼트입니다.
    """
    def __init__(self, text="작업 시작"):
        super().__init__(text)
        self.init_ui()

    def init_ui(self):
        """버튼의 고유 스타일과 호버 효과를 설정합니다."""
        self.setStyleSheet("""
            QPushButton {
                background-color: #e67e22;
                color: white;
                border-radius: 5px;
                padding: 12px;
                font-weight: bold;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
            QPushButton:pressed {
                background-color: #a04000;
            }
            QPushButton:disabled {
                background-color: #7f8c8d;
                color: #bdc3c7;
            }
        """)

    def set_running(self, is_running):
        """작업 상태에 따라 버튼의 텍스트와 활성화 여부를 변경합니다."""
        if is_running:
            self.setText("작업 진행 중...")
            self.setEnabled(False)
        else:
            self.setText("작업 시작")
            self.setEnabled(True)