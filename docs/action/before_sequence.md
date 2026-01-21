# before_sequence.py

## 목적

`before_sequence` 모듈은 GXWorks3 자동화 스크립트의 초기 단계를 담당합니다. 자동화 시퀀스를 시작하기 전에 작업 환경을 준비하고, 프로젝트 트리의 시작점으로 탐색하는 것을 주된 목적으로 합니다.

## 주요 기능

### `work()` 함수

- **설명**:
  이 함수는 자동화의 첫 단계로 호출됩니다. GXWorks3의 'Navigation' 창을 활성화하고, 프로젝트 트리의 최상단으로 스크롤하여 'Project' 항목을 찾는 역할을 합니다.

- **동작 순서**:
  1. `Waited.click(Get.center_location("Navigation"), 0.05)`:
     - 화면에서 'Navigation' 아이콘의 위치를 찾습니다 (`Get.center_location`).
     - 해당 위치를 0.05초 대기 후 클릭합니다 (`Waited.click`). 이를 통해 프로젝트 탐색 창을 활성화 상태로 만듭니다.
  2. `while True:` 루프:
     - `Waited.key_press('pageup')`: 'Page Up' 키를 반복적으로 눌러 프로젝트 트리를 위로 스크롤합니다.
     - `if Found.icon('Project') is not None:`:
       - 매 스크롤마다 화면에 'Project' 아이콘이 나타나는지 확인합니다 (`Found.icon`).
       - 'Project' 아이콘을 찾으면, 이는 트리의 최상단에 도달했음을 의미하므로 루프를 종료하고 함수 실행을 마칩니다.

## 의존성

- **`module.Waited`**: 시간 지연을 포함한 클릭 및 키 입력을 위해 사용됩니다.
- **`module.Get`**: 화면에서 특정 아이콘의 좌표를 얻기 위해 사용됩니다.
- **`module.Found`**: 화면에서 특정 아이콘의 존재 유무를 확인하기 위해 사용됩니다.
