import sys
from PyQt6.QtWidgets import QApplication
from UI.main_window import MainApp
from logic.redirector import StreamRedirector

def setup_logging(window):
    """터미널 출력을 GUI 로그창으로 연결"""
    redirector = StreamRedirector()
    # 리다이렉터의 신호를 메인 윈도우의 add_log 함수에 연결
    redirector.pkg_log_signal.connect(window.add_log)
    
    # 표준 출력(print)과 에러를 리다이렉터로 교체
    sys.stdout = redirector
    sys.stderr = redirector

def main():
    app = QApplication(sys.argv)
    
    # 1. 메인 윈도우 생성
    window = MainApp()
    
    # 2. 로깅 시스템 연결 (윈도우가 생성된 후 실행)
    setup_logging(window)
    
    # 3. 앱 실행
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()