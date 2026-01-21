# screen.py

## 목적

`screen` 모듈은 화면에서 특정 이미지(아이콘)를 찾는 기능을 담당합니다. `pyautogui`의 이미지 인식 기능을 사용하여, 지정된 시간 동안 주기적으로 화면을 스캔하고 원하는 아이콘이 나타나는지 확인합니다.

---

## `Found` 클래스

- **설명**: 화면에서 무언가를 '찾는(Found)' 기능들을 모아놓은 클래스입니다. 이 클래스의 메서드들은 단순히 이미지를 한 번 찾는 것을 넘어, 지정된 시간 동안 반복적으로 탐색하는 로직을 포함하고 있습니다.

- **`icon(icon_key, timeout=DEFAULT_TIMEOUT, confidence=CONFIDENCE)`**:
  - **파라미터**:
    - `icon_key` (str): `core.ICONS` 딕셔너리에 정의된 찾고자 하는 아이콘의 키.
    - `timeout` (int): 아이콘을 찾기 위해 시도할 최대 시간 (초). 이 시간 동안 아이콘을 찾지 못하면 탐색을 중단합니다. 기본값은 `core.DEFAULT_TIMEOUT`입니다.
    - `confidence` (float): 이미지 인식의 정확도(신뢰도). 0.0(완전히 다름)에서 1.0(완전히 같음) 사이의 값입니다. 기본값은 `core.CONFIDENCE`입니다.
  - **기능**:
    1. `start_time`에 현재 시간을 기록합니다.
    2. `while True` 루프를 시작하여 `timeout` 시간 동안 반복합니다.
    3. `pyautogui.locateCenterOnScreen()`을 사용하여 `icon_key`에 해당하는 이미지를 화면에서 찾습니다.
    4. 이미지를 찾으면 해당 이미지의 **중앙 좌표**를 즉시 반환합니다.
    5. 이미지를 찾지 못하면 `pyautogui.ImageNotFoundException` 예외가 발생할 수 있으나, `try-except` 구문으로 이를 무시하고 계속 진행합니다.
    6. `time.time() - start_time`이 `timeout`을 초과하면, 루프를 중단하고 `None`을 반환합니다.
    7. 루프의 각 주기마다 0.1초씩 대기하여 CPU 사용량을 줄입니다.

- **`icon_list(icon_key_list, timeout=0)`**:
  - **파라미터**:
    - `icon_key_list` (list of str): 찾고자 하는 아이콘 키들의 리스트.
    - `timeout` (int): 각 아이콘을 찾을 때 `Found.icon` 메서드에 전달할 타임아웃 값. 기본값은 0으로, 거의 즉시 확인하고 넘어감을 의미합니다.
  - **기능**:
    1. `icon_key_list`에 있는 각 `key`에 대해 순차적으로 반복합니다.
    2. `Found.icon(key, timeout=timeout)`을 호출하여 해당 아이콘이 화면에 있는지 확인합니다.
    3. 만약 아이콘을 찾았다면(`confirm_btn`이 `None`이 아니라면), 찾은 **좌표**와 해당 아이콘의 **키 이름**을 `(confirm_btn, key)` 튜플 형태로 즉시 반환하고 함수를 종료합니다.
    4. 리스트에 있는 모든 아이콘을 확인했는데도 아무것도 찾지 못하면, 최종적으로 `None`을 반환합니다.
  - **사용 예시**: 여러 종류의 팝업창 중 어떤 것이라도 나타났는지 한 번에 확인하고 싶을 때 유용합니다.

## 의존성

- **`pyautogui`**: 화면에서 이미지를 찾고 위치를 반환하는 핵심 기능을 수행합니다.
- **`time`**: `timeout`을 구현하기 위해 사용됩니다.
- **`logging`**: 함수 호출 정보를 로그로 남깁니다.
- **`core`**: `ICONS` 딕셔너리, `CONFIDENCE`, `DEFAULT_TIMEOUT` 등 핵심 설정값을 참조합니다.
