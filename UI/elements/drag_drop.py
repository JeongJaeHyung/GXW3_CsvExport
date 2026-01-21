import os
import time
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView
from PyQt6.QtCore import Qt, pyqtSignal

class FileTableElement(QTableWidget):
    """
    파일 정보를 테이블 형태로 표시하고 드롭을 처리하는 엘리먼트입니다.
    """
    files_dropped = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        # 4개 컬럼 설정
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["파일명", "경로", "최종 수정일", "상태"])
        
        # UI 설정
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DropOnly)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.setStyleSheet("background-color: #252526; color: #ddd; gridline-color: #3d3d3d;")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        paths = []
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if path.endswith('.gx3'):
                paths.append(path)
                self.add_file_row(path) # 테이블에 행 추가 로직 호출
        
        if paths:
            self.files_dropped.emit(paths)
            event.accept()

    def add_file_row(self, path):
        """파일 경로에서 정보를 추출하여 테이블에 새 행을 추가합니다."""
        row = self.rowCount()
        self.insertRow(row)
        
        file_name = os.path.basename(path)
        mod_time = time.ctime(os.path.getmtime(path)) # 최종 수정일 추출
        
        # 0. 파일명
        self.setItem(row, 0, QTableWidgetItem(file_name))
        # 1. 경로
        self.setItem(row, 1, QTableWidgetItem(path))
        # 2. 최종 수정일
        self.setItem(row, 2, QTableWidgetItem(mod_time))
        # 3. 상태 (초기값: 작업대기)
        status_item = QTableWidgetItem("작업대기")
        status_item.setForeground(Qt.GlobalColor.gray)
        self.setItem(row, 3, status_item)

    def update_row_status(self, row, status_text, color):
        """특정 행의 상태 텍스트와 색상을 변경합니다."""
        item = self.item(row, 3)
        if item:
            item.setText(status_text)
            item.setForeground(color)