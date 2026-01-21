from PyQt6.QtWidgets import QWidget, QHBoxLayout
from UI.elements.path_selector import PathSelectorElement
from UI.elements.run_button import RunButtonElement

class BottomSectionWidget(QWidget):
    """경로 선택바와 실행 버튼을 가로로 배치하는 위젯입니다."""
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.path_selector = PathSelectorElement(env_key="EXPORT_PATH")
        self.run_btn = RunButtonElement()
        
        layout.addWidget(self.path_selector, stretch=4) # 경로바를 길게
        layout.addWidget(self.run_btn, stretch=1)      # 버튼은 짧게