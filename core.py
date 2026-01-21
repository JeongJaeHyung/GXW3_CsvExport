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
ICONS = {
    # GXW3 ==========================================================================
    # Start sequence icons
    "GXW3_read_only": resource_path('icons/GXW3/Error/ReadOnly.png'),
    "GXW3_information1": resource_path('icons/GXW3/StartSequence/information1.png'),
    "GXW3_information2": resource_path('icons/GXW3/StartSequence/information2.png'),
    "GXW3_warning": resource_path('icons/GXW3/StartSequence/warning.png'),
    "GXW3_properties": resource_path('icons/GXW3/StartSequence/properties.png'),
    "GXW3_tool_bar": resource_path('icons/GXW3/StartSequence/tool_bar.png'),

    # Loading icons
    "GXW3_Loading1": resource_path('icons/GXW3/Loading/1.png'),
    "GXW3_Loading2": resource_path('icons/GXW3/Loading/2.png'),
    "GXW3_Loading3": resource_path('icons/GXW3/Loading/3.png'),
    "GXW3_Loading4": resource_path('icons/GXW3/Loading/4.png'),

    # Sequence Control icons
    "GXW3_Navigation": resource_path('icons/GXW3/NonActiveNavigation.png'),
    "GXW3_Parameter": resource_path('icons/GXW3/ActiveClosedParameter.png'),
    "GXW3_Warning": resource_path('icons/GXW3/Error/Warning.png'),
    "GXW3_Statement": resource_path('icons/GXW3/Error/statement.png'),
    
    # Node icons
    "GXW3_Project": resource_path('icons/GXW3/ActiveProject.png'),
    "GXW3_Program": resource_path('icons/GXW3/ActiveClosedProgram.png'),
    "GXW3_Scan": resource_path('icons/GXW3/ActiveClosedScan.png'),
    "GXW3_Unit": resource_path('icons/GXW3/ActiveClosedUnit.png'),
    "GXW3_Folder": resource_path('icons/GXW3/ActiveClosedFolder.png'),
    "GXW3_ProgramBlock1": resource_path('icons/GXW3/ActiveClosedProgramBlock.png'),
    "GXW3_ProgramBlock2": resource_path('icons/GXW3/ActiveOpenProgramBlock.png'),

    # Devices
    "GXW3_Device": resource_path('icons/GXW3/ActiveClosedDevice.png'),
    "GXW3_Comment": resource_path('icons/GXW3/ActiveDeviceComment.png'),

    # ETC
    "WindowsFolder": resource_path('icons/WindowsFolder.png'),


    # GXW2 ==========================================================================
    # Sequence icons
    "GXW2_Parameter": resource_path('icons/GXW2/ActiveParameter.png'),
    "GXW2_Navigation": resource_path('icons/GXW2/Navigation.png'),
    "GXW2_GlobalDeviceComment": resource_path('icons/GXW2/GlobalDeviceComment.png'),
    "GXW2_ProgramSetting": resource_path('icons/GXW2/ProgramSetting.png'),
    "GXW2_Scan": resource_path('icons/GXW2/Scan.png'),
    "GXW2_Unit": resource_path('icons/GXW2/ActiveClosedUnit.png'),
    "GXW2_Program": resource_path('icons/GXW2/ActiveProgram.png'),
    "GXW2_END": resource_path('icons/GXW2/END.png'),
}

class ICON:
    class GXW3:
        read_only = ICONS["GXW3_read_only"]
        information1 = ICONS["GXW3_information1"]
        information2 = ICONS["GXW3_information2"]
        warning = ICONS["GXW3_warning"]
        properties = ICONS["GXW3_properties"]
        tool_bar = ICONS["GXW3_tool_bar"]

        Loading1 = ICONS["GXW3_Loading1"]
        Loading2 = ICONS["GXW3_Loading2"]
        Loading3 = ICONS["GXW3_Loading3"]
        Loading4 = ICONS["GXW3_Loading4"]

        Navigation = ICONS["GXW3_Navigation"]
        Parameter = ICONS["GXW3_Parameter"]
        Warning = ICONS["GXW3_Warning"]
        Statement = ICONS["GXW3_Statement"]

        Project = ICONS["GXW3_Project"]
        Program = ICONS["GXW3_Program"]
        Scan = ICONS["GXW3_Scan"]
        Unit = ICONS["GXW3_Unit"]
        Folder = ICONS["GXW3_Folder"]
        ProgramBlock1 = ICONS["GXW3_ProgramBlock1"]
        ProgramBlock2 = ICONS["GXW3_ProgramBlock2"]

        Device = ICONS["GXW3_Device"]
        Comment = ICONS["GXW3_Comment"]

    class GXW2:
        Parameter = ICONS["GXW2_Parameter"]
        Navigation = ICONS["GXW2_Navigation"]
        GlobalDeviceComment = ICONS["GXW2_GlobalDeviceComment"]
        ProgramSetting = ICONS["GXW2_ProgramSetting"]
        Scan = ICONS["GXW2_Scan"]
        Unit = ICONS["GXW2_Unit"]
        Program = ICONS["GXW2_Program"]
        END = ICONS["GXW2_END"]

    class ETC:
        WindowsFolder = ICONS["WindowsFolder"]







