import os
from abc import ABC, abstractmethod

class BaseAutomationTemplate(ABC):
    def __init__(self, worker):
        """worker 객체를 주입받아 시그널(file_progress, status_update 등)을 제어합니다."""
        self.worker = worker

    @abstractmethod
    def run_workflow(self, idx, file_path, session_dir):
        """파일 하나에 대한 전체 워크플로우(경로 생성, UI 업데이트, 시퀀스 실행)를 정의합니다."""
        pass