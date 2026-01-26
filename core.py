import os
import sys
import dotenv

# .env 파일 로드
ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
dotenv.load_dotenv(ENV_PATH)

# 환경 변수 및 전역 변수
CONFIDENCE = float(os.getenv('CONFIDENCE', 0.9)) # 신뢰도를 살짝 낮추는 것을 권장합니다 (0.988 -> 0.9)
DEFAULT_DELAY = float(os.getenv('DEFAULT_DELAY', 0.05))
KEY_PRESS_DELAY = float(os.getenv('KEY_PRESS_DELAY', 0.01))
DEFAULT_TIMEOUT = float(os.getenv('DEFAULT_TIMEOUT', 1))
NODE_OPEN_TIMEOUT = float(os.getenv('NODE_OPEN_TIMEOUT', 0))
EXPORT_PATH = os.getenv('EXPORT_PATH', '')

# [추가] 현재 파일의 결과물이 저장될 실제 경로
CURRENT_EXPORT_DIR = ""


processed_targets = []

def save_setting_to_env(key, value):
    """.env 파일 업데이트 및 메모리 변수 동기화 (형변환 오류 방지)"""
    dotenv.set_key(ENV_PATH, key, str(value))
    if hasattr(sys.modules[__name__], key):
        try:
            # 숫자로 변환 가능한 설정값만 float 처리
            setattr(sys.modules[__name__], key, float(value))
        except (ValueError, TypeError):
            # 경로와 같은 문자열은 그대로 저장
            setattr(sys.modules[__name__], key, value)

def resource_path(relative_path):
    try: 
        base_path = sys._MEIPASS
    except Exception: 
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# ICONS 정의는 기존과 동일하게 유지...

# 아이콘 경로는 생략 (기존과 동일)
class ICON:
    class GXW3:
        properties = resource_path('icons/GXW3/StartSequence/properties.png')
        tool_bar = resource_path('icons/GXW3/StartSequence/tool_bar.png')

        Loading1 = resource_path('icons/GXW3/Loading/1.png')
        Loading2 = resource_path('icons/GXW3/Loading/2.png')
        Loading3 = resource_path('icons/GXW3/Loading/3.png')
        Loading4 = resource_path('icons/GXW3/Loading/4.png')

        Navigation = resource_path('icons/GXW3/NonActiveNavigation.png')
        Parameter = resource_path('icons/GXW3/ActiveClosedParameter.png')
        Warning = resource_path('icons/GXW3/Error/Warning.png')
        Statement = resource_path('icons/GXW3/Error/statement.png')

        Project = resource_path('icons/GXW3/ActiveProject.png')
        Program = resource_path('icons/GXW3/ActiveClosedProgram.png')
        Scan = resource_path('icons/GXW3/ActiveClosedScan.png')
        Unit = resource_path('icons/GXW3/ActiveClosedUnit.png')
        Folder = resource_path('icons/GXW3/ActiveClosedFolder.png')
        ProgramBlock = resource_path('icons/GXW3/ActiveProgramBlock.png')
        ProgramBlock1 = resource_path('icons/GXW3/ActiveClosedProgramBlock.png')
        ProgramBlock2 = resource_path('icons/GXW3/ActiveOpenProgramBlock.png')

        Device = resource_path('icons/GXW3/ActiveClosedDevice.png')
        Comment = resource_path('icons/GXW3/ActiveDeviceComment.png')

        LineChange = resource_path('icons/GXW3/LineChange.png')


    class GXW2:
        ProjectProperty = resource_path('icons/GXW2/ProjectProperty.png')
        Parameter = resource_path('icons/GXW2/ActiveParameter.png')
        Navigation = resource_path('icons/GXW2/Navigation.png')
        GlobalDeviceComment = resource_path('icons/GXW2/GlobalDeviceComment.png')
        PS = resource_path('icons/GXW2/ProgramSetting.png')
        Scan = resource_path('icons/GXW2/Scan.png')
        Unit = resource_path('icons/GXW2/ActiveClosedUnit.png')
        POU = resource_path('icons/GXW2/ProgramOfUnit.png')
        PF = resource_path('icons/GXW2/ProgramFolder.png')
        Program1 = resource_path('icons/GXW2/ActiveProgram1.png')
        Program2 = resource_path('icons/GXW2/ActiveProgram2.png')
        DeviceInitialValue = resource_path('icons/GXW2/DeviceInitialValue.png')


    class ETC:
        FilePathSetting = resource_path('icons/FilePathSetting.png')
    

    class Error:
        Warning1 = resource_path('icons/Error/Warning1.png')
        Warning2 = resource_path('icons/Error/Warning2.png')
        Information1 = resource_path('icons/Error/Information1.png')
        Information2 = resource_path('icons/Error/Information2.png')
        Information3 = resource_path('icons/Error/Information3.png')
