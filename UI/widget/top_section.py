from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from UI.elements.drag_drop import FileTableElement # 클래스명 변경 반영
from UI.elements.config_table import ConfigTableElement

class TopSectionWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)

        # 왼쪽: 파일 정보 테이블 영역
        left_container = QWidget()
        left_layout = QVBoxLayout(left_container)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.addWidget(QLabel("📁 대상 파일 목록 (Drag & Drop)"))
        self.file_table = FileTableElement() # 변수명도 직관적으로 변경
        left_layout.addWidget(self.file_table)
        
        # 오른쪽: 설정 테이블
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.addWidget(QLabel("⚙️ 변수 값 설정"))
        self.config_table = ConfigTableElement()
        right_layout.addWidget(self.config_table)

        layout.addWidget(left_container, stretch=2) # 테이블 영역을 더 넓게 설정
        layout.addWidget(right_container, stretch=1)