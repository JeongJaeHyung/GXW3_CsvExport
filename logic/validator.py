import os
import winapps
from PyQt6.QtWidgets import QMessageBox

def check_software_dependencies(parent):
    """GX Works 설치 여부 확인 및 경고창 표시"""
    try:
        installed_apps = [app.name.lower() for app in winapps.list_installed()]
        has_gxw2 = any("gx works2" in name for name in installed_apps)
        has_gxw3 = any("gx works3" in name for name in installed_apps)

        if not has_gxw2 and not has_gxw3:
            QMessageBox.critical(parent, "설치 오류", "GX Works 2/3가 설치되어 있지 않습니다.")
        elif not has_gxw2:
            QMessageBox.warning(parent, "주의", "GX Works2가 없어 .gxw 작업이 불가합니다.")
        elif not has_gxw3:
            QMessageBox.warning(parent, "주의", "GX Works3가 없어 .gx3 작업이 불가합니다.")
    except Exception as e:
        print(f"Software check error: {e}")

def validate_root_path(path):
    """대상 폴더 유효성 검사"""
    return path and os.path.exists(path)