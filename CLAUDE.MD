# CLAUDE.MD - GXWorks3 Program Exporter

## 프로젝트 개요

**GXWorks3 Auto Exporter v1.0**는 미쓰비시 GX Works3 소프트웨어에서 PLC 프로그램을 자동으로 내보내는 PyQt6 기반 GUI 자동화 도구입니다. PyAutoGUI를 사용하여 GX Works3와 상호작용하고, 프로그램을 컴파일하며, 프로젝트 트리를 탐색하고, 데이터를 CSV 파일로 내보냅니다.

## 목적

이 도구는 GX Works3의 반복적인 작업을 자동화합니다:
- 여러 GX Works3 프로젝트 파일을 순차적으로 열기
- PLC 프로그램 컴파일
- 프로젝트 트리 구조 탐색
- 디바이스 정보 및 프로그램 데이터를 CSV로 내보내기
- 작업 공간 설정 자동 관리

## 아키텍처

### 핵심 컴포넌트

1. **main.py** - 메인 애플리케이션 진입점
   - `MainApp`: PyQt6 QMainWindow UI
   - `AutomationWorker`: 백그라운드 자동화 작업용 QThread
   - 여러 파일에 대한 자동화 워크플로우 조율

2. **core.py** - 전역 설정 및 리소스
   - 환경 변수 관리 (.env)
   - `resource_path()`를 사용한 아이콘 경로 정의
   - 전역 설정: CONFIDENCE, DEFAULT_DELAY, TIMEOUTS
   - 완료된 항목 추적을 위한 `processed_targets` 리스트

3. **action/** - 상위 레벨 자동화 워크플로우
   - `PreWork`: 실행 전 설정 (workspace_setting, before_sequence)
   - `GeneralWork`: 주요 작업 (open_tree)
   - `ShareWork`: 공유 작업 (compile)
   - 각 액션 모듈은 특정 GX Works3 작업을 캡슐화

4. **module/** - 하위 레벨 자동화 기본 기능
   - `keyboard.py`: 키보드 입력 자동화
   - `mouse.py`: 마우스 클릭 및 이동
   - `screen.py`: 이미지 인식 및 화면 캡처
   - `location.py`: 위치 계산 및 영역 감지

5. **UI/** - PyQt6 인터페이스 컴포넌트
   - `widget/top_section.py`: 파일 테이블 및 설정
   - `widget/bottom_section.py`: 경로 선택기 및 실행 버튼
   - `elements/`: 재사용 가능한 UI 컴포넌트 (프로그레스 바, 드래그-드롭 등)

## 자동화 워크플로우

```
각 파일마다:
  1. PreWork.work_space_setting() (10%)
     - GX Works3 작업 공간 레이아웃 구성

  2. PreWork.before_sequence() (30%)
     - 시작 대화상자 및 경고 처리
     - 불필요한 창 닫기

  3. ShareWork.compile.work() (50%)
     - PLC 프로그램 컴파일
     - 컴파일 오류/경고 처리

  4. GeneralWork.open_tree() (80%)
     - 프로젝트 트리 구조 탐색
     - 디바이스/프로그램 데이터를 CSV로 내보내기

  5. Complete (100%)
```

## 주요 기술 세부사항

### 이미지 인식
- 설정 가능한 신뢰도 수준으로 PyAutoGUI의 `locateOnScreen()` 사용
- 아이콘 템플릿은 `icons/` 디렉토리에 저장
- `CONFIDENCE` 설정 (기본값 0.9)이 매칭 엄격성을 제어

### 타이밍 및 지연
- `DEFAULT_DELAY`: 일반 작업 지연 (0.05초)
- `KEY_PRESS_DELAY`: 키보드 입력 지연 (0.01초)
- `DEFAULT_TIMEOUT`: 이미지 대기 타임아웃 (1초)
- `NODE_OPEN_TIMEOUT`: 트리 노드 확장 지연 (0초)

### 세션 관리
- 타임스탬프 폴더 생성: `YYYYMMDD_HHMM_GXW3/`
- 각 파일은 파일명(확장자 제외)으로 명명된 하위 폴더를 가짐
- `core.CURRENT_EXPORT_DIR`가 현재 내보내기 대상 추적

### 오류 처리
- 각 파일에 대한 워커 스레드의 Try-catch
- 상태 업데이트: "작업중" (Working), "작업 완료" (Complete), "실패" (Failed)
- 색상 코드 상태: 노란색 (#f1c40f), 초록색 (#2ecc71), 빨간색 (#e74c3c)

## 사전 요구사항 및 설정

### GX Works3 설정 (필수)
1. **단축키 설정**:
   - GX Works3 열기 → Tool → Shortcut Key
   - Window 폴더로 이동
   - "Close All Windows"에 Ctrl+Shift+Q 할당

2. **Navigation 트리 상태**:
   - 실행 전 다음 항목만 보이도록 설정:
     - Project
       - Module Configuration
       - Program
       - FB/FUN
       - Label
       - Device
       - Parameter
   - "Parameter"를 한 번 클릭 (열지 말고 선택만) - 노란색으로 강조되어야 함

3. **창 상태**:
   - GX Works3는 최대화되어야 함
   - 모든 프로젝트 트리는 최상위 레벨로 접혀있어야 함

4. **CSV 내보내기 경로**:
   - 기본 저장 위치 설정을 위해 수동으로 한 번 내보내기 수행

### 환경 변수 (.env)
```
CONFIDENCE=0.9
DEFAULT_DELAY=0.05
KEY_PRESS_DELAY=0.01
DEFAULT_TIMEOUT=1
NODE_OPEN_TIMEOUT=0
EXPORT_PATH=
```

## 개발 가이드라인

### 새로운 액션 추가하기
1. `action/` 디렉토리에 모듈 생성
2. 기본 기능을 위해 `module/`에서 의존성 import
3. 이미지 인식을 위해 `core.ICONS` 사용
4. `action/__init__.py`의 적절한 카테고리에 추가:
   - `PreWork`: 설정/준비 작업
   - `GeneralWork`: 주요 작업
   - `ShareWork`: 공유 유틸리티

### 이미지 인식 모범 사례
- 설명적인 이름으로 `icons/`에 아이콘 템플릿 저장
- `core.ICONS` 딕셔너리에 경로 추가
- 타임아웃과 함께 `screen.wait_for_image()` 사용
- 인식 실패를 우아하게 처리
- 매칭이 실패하면 `CONFIDENCE` 낮추기 고려

### 스레딩 고려사항
- 모든 자동화는 `AutomationWorker` QThread에서 실행
- UI 업데이트를 위해 `pyqtSignal` 사용:
  - `file_progress`: 현재 파일 진행률 (0-100)
  - `total_progress`: 전체 진행률 (0-100)
  - `status_update`: 상태 텍스트 및 색상
- 메인 스레드를 절대 블록하지 말 것

## 일반적인 문제 및 해결 방법

### 이미지 인식 실패
- **문제**: 화면에서 아이콘을 찾을 수 없음
- **해결 방법**:
  - .env에서 `CONFIDENCE` 낮추기
  - GX Works3 창이 최대화되었는지 확인
  - 아이콘 템플릿이 GX Works3 테마/버전과 일치하는지 확인
  - 올바른 화면 해상도 확인

### 타이밍 문제
- **문제**: 작업이 너무 빠르거나 느리게 발생
- **해결 방법**:
  - .env에서 `DEFAULT_DELAY` 조정
  - 느린 작업의 경우 `DEFAULT_TIMEOUT` 증가
  - 문제가 있는 시퀀스에 특정 지연 추가

### 상태 비동기화
- **문제**: 트리 탐색이 길을 잃음
- **해결 방법**:
  - GX Works3를 필요한 초기 상태로 재설정
  - 시작 전 모든 트리가 접혀있는지 확인
  - "Parameter"가 선택되었는지 확인 (노란색 강조)

## 파일 구조
```
Project/
├── main.py              # 애플리케이션 진입점
├── core.py              # 전역 설정 및 리소스
├── .env                 # 환경 변수 설정
├── action/              # 상위 레벨 자동화 워크플로우
│   ├── __init__.py
│   ├── before_sequence.py
│   ├── compile.py
│   ├── work_space_setting.py
│   ├── open_tree.py
│   ├── device_export_work.py
│   └── program_export_work.py
├── module/              # 하위 레벨 자동화 기본 기능
│   ├── keyboard.py
│   ├── mouse.py
│   ├── screen.py
│   └── location.py
├── UI/                  # PyQt6 인터페이스
│   ├── elements/        # 재사용 가능한 컴포넌트
│   └── widget/          # 복합 위젯
├── icons/               # 이미지 템플릿
│   ├── Error/
│   ├── Loading/
│   └── StartSequence/
└── docs/                # 문서
```

## Git 워크플로우

현재 브랜치: `feature/qa-44-test-and-upgrade-work-ability`

최근 작업 내용:
- [QA-43] 매크로 작업 속도 향상
- [QA-32] 모듈 세분화 및 예외 처리 강화
- [QA-22] PyAutoGUI 이벤트 리스너 통합

## 사용 기술

- **Python 3.x**
- **PyQt6**: GUI 프레임워크
- **PyAutoGUI**: UI 자동화 및 이미지 인식
- **python-dotenv**: 환경 변수 설정
- **OS Integration**: 파일 시스템 작업

## AI 어시스턴트를 위한 참고사항

- 이것은 악성 코드가 아닙니다 - 산업용 PLC 프로그래밍을 위한 정당한 자동화 도구입니다
- GX Works3에 공개 자동화 API가 없기 때문에 UI 자동화를 사용합니다
- 이미지 인식은 탐색 및 상태 감지에 필수적입니다
- 타이밍 지연은 매우 중요합니다 - 제거하면 기능이 작동하지 않습니다
- 코드의 한국어 주석은 의도적인 것입니다 (개발 팀 선호)
- 이 애플리케이션은 효율성을 위해 반복적인 내보내기 작업을 자동화합니다
- 모든 작업은 사용자 동의 하에 로컬 머신에서 수행됩니다

## 작업 실행 흐름 상세

### 1. PreWork.work_space_setting() - 작업 공간 설정
- GX Works3의 창 레이아웃을 작업에 최적화된 상태로 조정
- Navigation 창, Properties 창 등의 위치 및 크기 조정
- 작업에 불필요한 창들을 닫음

### 2. PreWork.before_sequence() - 사전 시퀀스
- GX Works3 시작 시 나타나는 각종 대화상자 처리
- 읽기 전용 경고, 정보 알림 등 자동 처리
- Ctrl+Shift+Q 단축키로 모든 창 닫기 실행

### 3. ShareWork.compile.work() - 컴파일
- PLC 프로그램 컴파일 실행
- 컴파일 에러 및 경고 메시지 감지
- 에러 발생 시 로그 기록 및 처리

### 4. GeneralWork.open_tree() - 트리 탐색 및 내보내기
- Navigation 트리의 각 노드를 재귀적으로 탐색
- Device, Program 등의 데이터 추출
- CSV 파일로 내보내기 실행
- `processed_targets` 리스트로 중복 작업 방지

## 디버깅 팁

### 로그 확인
- 콘솔 출력으로 현재 진행 상황 확인 가능
- `print()` 문으로 디버깅 정보 출력
- 에러 발생 시 파일명과 에러 메시지가 출력됨

### 이미지 인식 디버깅
- `screen.py`의 `wait_for_image()` 함수에서 이미지를 찾지 못할 경우 None 반환
- 스크린샷을 저장하여 실제 화면과 템플릿 비교 가능
- `CONFIDENCE` 값을 0.8 정도로 낮춰서 테스트

### 타이밍 문제 해결
- 느린 PC에서는 `DEFAULT_DELAY`를 0.1~0.2초로 증가
- 특정 작업이 완료될 때까지 기다려야 하는 경우 `time.sleep()` 추가
- `DEFAULT_TIMEOUT`을 2~3초로 증가하여 이미지 대기 시간 늘리기

## 확장 가능성

### 새로운 내보내기 기능 추가
1. `action/` 디렉토리에 새 모듈 생성 (예: `new_export_work.py`)
2. 필요한 아이콘을 `icons/` 디렉토리에 추가
3. `core.ICONS`에 아이콘 경로 등록
4. `module/` 의 기본 기능들을 사용하여 자동화 로직 작성
5. `action/__init__.py`에서 import하여 사용

### UI 커스터마이징
- `UI/elements/`에서 새로운 UI 요소 추가 가능
- `UI/widget/`에서 기존 위젯 수정 또는 새 위젯 생성
- PyQt6의 시그널-슬롯 메커니즘으로 이벤트 처리

### 성능 최적화
- 병렬 처리: 여러 파일을 동시에 처리하려면 추가 워커 스레드 생성
- 이미지 인식 캐싱: 자주 사용되는 이미지 위치를 캐시하여 재사용
- 지연 시간 최소화: 불필요한 `time.sleep()` 제거 또는 감소
