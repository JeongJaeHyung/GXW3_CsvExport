# work_space_setting.py

## 목적

`work_space_setting` 모듈은 GXWorks3 애플리케이션이 시작될 때 나타날 수 있는 다양한 초기 팝업창이나 대화상자를 자동으로 처리하여 주 작업 공간으로 진입할 수 있도록 준비하는 역할을 합니다.

## 주요 기능

### `work()` 함수

- **설명**:
  이 함수는 애플리케이션 실행 초기에 나타날 수 있는 정보, 경고, 성명 등의 팝업창을 순차적으로 확인하고 닫습니다. 최종적으로 GXWorks3의 메인 툴바가 화면에 나타나면, 작업 공간 준비가 완료된 것으로 판단하고 함수를 종료합니다.

- **주요 변수**:
  - `pop_up_list`: 처리해야 할 팝업창을 식별하는 아이콘 키의 집합입니다. (`information1`, `information2`, `warning`, `Statement`)
  - `status`: 특정 시간 동안 아무런 팝업도 감지되지 않았을 때, 프로세스를 종료하기 위한 카운터 변수입니다.

- **동작 순서**:
  1. `while status < 3:` 루프:
     - `if Found.icon("tool_bar", 1):`:
       - 화면에서 'tool_bar' 아이콘을 1초의 타임아웃으로 찾습니다.
       - 툴바가 발견되면, 이는 메인 작업 공간에 성공적으로 진입했음을 의미하므로, "Workspace Setting is Done" 메시지를 출력하고 함수를 즉시 종료합니다.
     - `elif (result := Found.icon_list(pop_up_list, 1)) is not None:`:
       - `pop_up_list`에 정의된 팝업 아이콘들을 1초의 타임아웃으로 화면에서 찾습니다.
       - 만약 팝업 중 하나라도 발견되면 (`result`가 `None`이 아니면):
         - `position`, `target`: 발견된 팝업의 위치와 아이콘 키입니다.
         - `status = 0`: 팝업을 성공적으로 처리했으므로, `status` 카운터를 0으로 리셋합니다.
         - `Waited.key_press("enter")`: 'Enter' 키를 눌러 해당 팝업창을 닫습니다. (대부분의 정보/경고창은 Enter로 닫힘)
     - `else:` (툴바도, 팝업도 찾지 못한 경우):
       - "Nothing Found" 메시지를 출력합니다.
       - `status += 1`: `status` 카운터를 1 증가시킵니다. 루프가 3번 연속으로 아무것도 찾지 못하면 (약 3초 이상 소요), 더 이상 처리할 팝업이 없다고 간주하고 `while` 루프가 종료됩니다.

## 의존성

- **`module.Waited`**: 시간 지연을 포함한 키 입력을 위해 사용됩니다.
- **`module.Found`**: 화면에서 특정 아이콘 또는 아이콘 목록을 찾는 데 사용됩니다.
