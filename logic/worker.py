import os
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QColor
from UI.template.gxw2_automation import GXW2AutomationTemplate
from UI.template.gxw3_automation import GXW3AutomationTemplate

class AutomationWorker(QThread):
    file_progress = pyqtSignal(int)
    total_progress = pyqtSignal(int)
    status_update = pyqtSignal(int, str, QColor)

    def __init__(self, files, session_dir):
        super().__init__()
        self.files = files
        self.session_dir = session_dir

    def run(self):
        total_files = len(self.files)
        print(f"🚀 작업을 시작합니다. 총 파일 수: {total_files}")

        for idx, file_path in enumerate(self.files):
            file_name = os.path.basename(file_path)
            try:
                print(f"📂 [{file_name}] 분석 및 자동화 시작...")
                _, ext = os.path.splitext(file_path)
                
                # Factory logic
                template_cls = GXW2AutomationTemplate if ext.lower() == '.gxw' else GXW3AutomationTemplate
                current_template = template_cls(self)
                
                current_template.run_workflow(idx, file_path, self.session_dir)
                print(f"✅ [{file_name}] 내보내기 작업 완료")

            except Exception as e:
                print(f"❌ [{file_name}] 에러 발생: {str(e)}")
                self.status_update.emit(idx, "실패", QColor("#e74c3c"))
            
            self.total_progress.emit(int((idx + 1) / total_files * 100))
        
        print("🏁 모든 파일에 대한 프로세스가 종료되었습니다.")