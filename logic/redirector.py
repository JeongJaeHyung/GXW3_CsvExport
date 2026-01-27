from PyQt6.QtCore import QObject, pyqtSignal

class StreamRedirector(QObject):
    pkg_log_signal = pyqtSignal(str)

    def write(self, text):
        if text and text.strip():
            self.pkg_log_signal.emit(text)

    def flush(self):
        pass