from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
import core

class ConfigTableElement(QTableWidget):
    """환경 변수를 표시하고 영구 저장 기능을 지원하는 테이블입니다."""
    def __init__(self):
        super().__init__(5, 2)
        self.setHorizontalHeaderLabels(["변수명", "설정값"])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.setStyleSheet("background-color: #252526; color: #ddd; gridline-color: #3d3d3d;")
        self.load_settings()

    def load_settings(self):
        """core.py에 로드된 .env 초기값을 테이블에 채웁니다."""
        configs = [
            ("CONFIDENCE", core.CONFIDENCE),
            ("DEFAULT_DELAY", core.DEFAULT_DELAY),
            ("KEY_PRESS_DELAY", core.KEY_PRESS_DELAY),
            ("DEFAULT_TIMEOUT", core.DEFAULT_TIMEOUT),
            ("NODE_OPEN_TIMEOUT", core.NODE_OPEN_TIMEOUT)
        ]
        for row, (name, value) in enumerate(configs):
            self.setItem(row, 0, QTableWidgetItem(name))
            self.setItem(row, 1, QTableWidgetItem(str(value)))

    def save_to_env_file(self):
        """현재 테이블의 모든 값을 실제 .env 파일에 영구 저장합니다."""
        for row in range(self.rowCount()):
            key = self.item(row, 0).text()
            value = self.item(row, 1).text()
            core.save_setting_to_env(key, value)
        print(">>> .env 파일에 영구 저장되었습니다.")