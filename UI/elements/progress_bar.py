from PyQt6.QtWidgets import QProgressBar
from PyQt6.QtCore import Qt

class ProgressBarElement(QProgressBar):
    """
    작업의 진행 상태를 시각적으로 표시하는 독립 진행률 바 엘리먼트입니다.
    """
    def __init__(self, color="#2ecc71"):
        super().__init__()
        self.color = color
        self.init_ui()

    def init_ui(self):
        """진행률 바의 스타일 및 텍스트 위치를 설정합니다."""
        self.setTextVisible(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setHeight(25) # 기본 높이 설정
        
        # QProgressBar 스타일 설정 (전달받은 색상 적용)
        self.setStyleSheet(f"""
            QProgressBar {{
                border: 1px solid #3d3d3d;
                border-radius: 5px;
                text-align: center;
                background-color: #252526;
                color: white;
                font-weight: bold;
            }}
            QProgressBar::chunk {{
                background-color: {self.color};
                border-radius: 4px;
                width: 2px;
            }}
        """)

    def setHeight(self, height):
        """바의 높이를 고정합니다."""
        self.setFixedHeight(height)

    def update_value(self, value):
        """진행률 값을 안전하게 업데이트합니다."""
        if value < 0:
            self.setValue(0)
        elif value > 100:
            self.setValue(100)
        else:
            self.setValue(int(value))