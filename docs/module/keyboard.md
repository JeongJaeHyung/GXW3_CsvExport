# keyboard.py

## 목적

`keyboard` 모듈은 `pyautogui` 라이브러리를 기반으로 키보드 입력을 시뮬레이션하는 기능들을 래핑하여 제공합니다. 이 모듈은 자동화 스크립트에서 키보드 조작을 보다 쉽게 사용할 수 있도록 추상화된 클래스와 메서드를 포함합니다.

동작의 즉시성, 지연, 조건부 실행 여부에 따라 `Just`, `Waited`, `Found` 세 가지 클래스로 구분됩니다.

---

## `Just` 클래스

- **설명**: 즉시 키보드 동작을 수행합니다. 대기 시간이 거의 필요 없는 빠른 입력에 사용됩니다.

- **`key_press(key)`**:
  - **파라미터**: `key` (str) - `pyautogui`가 인식할 수 있는 키 이름 (예: 'enter', 'f4', 'a').
  - **기능**: 지정된 단일 키를 즉시 누릅니다. `KEY_PRESS_DELAY` 만큼의 짧은 딜레이 후 `pyautogui.press()`를 호출합니다.

- **`hotkey_press(hotkey_list)`**:
  - **파라미터**: `hotkey_list` (list of str) - 동시에 누를 키들의 리스트 (예: `['ctrl', 'shift', 'q']`).
  - **기능**: 지정된 키 조합(핫키)을 즉시 누릅니다. `pyautogui.hotkey()`를 호출합니다.

---

## `Waited` 클래스

- **설명**: 지정된 시간만큼 대기한 후 키보드 동작을 수행합니다. UI가 업데이트되거나 특정 작업이 완료될 시간을 확보해야 할 때 사용됩니다.

- **`key_press(key, interval=DEFAULT_DELAY)`**:
  - **파라미터**:
    - `key` (str): 누를 키.
    - `interval` (float): 대기할 시간 (초). 기본값은 `core.DEFAULT_DELAY`입니다.
  - **기능**: `interval` + `KEY_PRESS_DELAY` 만큼 대기한 후, `Just.key_press(key)`를 호출하여 키를 누릅니다.

- **`hotkey_press(hotkey_list, interval=DEFAULT_DELAY)`**:
  - **파라미터**:
    - `hotkey_list` (list of str): 누를 핫키.
    - `interval` (float): 대기할 시간 (초).
  - **기능**: `interval` + `KEY_PRESS_DELAY` 만큼 대기한 후, `Just.hotkey_press(hotkey_list)`를 호출하여 핫키를 누릅니다.

---

## `Found` 클래스

- **설명**: 화면에서 특정 아이콘을 발견했을 때만 키보드 동작을 수행합니다. 특정 조건이 충족되었을 때만 다음 단계를 진행하고자 할 때 유용합니다.

- **`key_press(icon_key, key, timeout=DEFAULT_TIMEOUT, confidence=CONFIDENCE)`**:
  - **파라미터**:
    - `icon_key` (str): `screen.Found.icon`에서 사용할 아이콘의 키.
    - `key` (str): 누를 키.
    - `timeout` (int): 아이콘을 찾을 최대 대기 시간 (초).
    - `confidence` (float): 이미지 인식의 정확도.
  - **기능**: `screen.Found.icon`을 호출하여 `timeout` 시간 동안 `icon_key`에 해당하는 아이콘을 찾습니다. 아이콘을 찾으면 `Just.key_press(key)`를 호출하여 키를 누릅니다.

- **`hotkey_press(icon_key, hotkey_list, timeout=DEFAULT_TIMEOUT, confidence=CONFIDENCE)`**:
  - **파라미터**:
    - `icon_key` (str): 찾을 아이콘의 키.
    - `hotkey_list` (list of str): 누를 핫키.
    - `timeout`, `confidence`: 위와 동일.
  - **기능**: `screen.Found.icon`을 호출하여 아이콘을 찾습니다. 아이콘을 찾으면 `Just.hotkey_press(hotkey_list)`를 호출하여 핫키를 누릅니다.

## 의존성

- **`pyautogui`**: 실제 키보드 이벤트를 생성하기 위해 사용됩니다.
- **`time`**: `Waited` 클래스에서 대기 시간을 구현하기 위해 사용됩니다.
- **`core`**: `DEFAULT_DELAY`, `KEY_PRESS_DELAY` 등 핵심 설정값을 참조합니다.
- **`module.screen`**: `Found` 클래스에서 화면의 아이콘을 찾는 기능을 사용합니다.
