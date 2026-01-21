# mouse.py

## 목적

`mouse` 모듈은 `pyautogui`를 사용하여 마우스 클릭과 관련된 동작을 추상화합니다. `keyboard.py`와 유사하게, 자동화 스크립트에서 마우스 조작을 쉽게 사용할 수 있도록 `Just`, `Waited`, `Found` 세 가지 클래스로 나누어 기능을 제공합니다.

---

## `Just` 클래스

- **설명**: 즉시 마우스 동작을 수행합니다.

- **`click(location)`**:
  - **파라미터**: `location` (tuple) - 클릭할 화면의 (x, y) 좌표.
  - **기능**: 지정된 위치에서 즉시 마우스 왼쪽 버튼을 한 번 클릭합니다.

- **`double_click(location)`**:
  - **파라미터**: `location` (tuple) - 더블 클릭할 화면의 (x, y) 좌표.
  - **기능**: 지정된 위치에서 즉시 더블 클릭합니다.

- **`right_click(location)`**:
  - **파라미터**: `location` (tuple) - 오른쪽 클릭할 화면의 (x, y) 좌표.
  - **기능**: 지정된 위치에서 즉시 마우스 오른쪽 버튼을 클릭합니다.

---

## `Waited` 클래스

- **설명**: 지정된 시간만큼 대기한 후 마우스 동작을 수행합니다. UI 반응 시간이나 애니메이션 효과를 기다릴 때 유용합니다.

- **`click(location, interval=DEFAULT_DELAY)`**:
  - **파라미터**:
    - `location` (tuple): 클릭할 좌표.
    - `interval` (float): 대기할 시간 (초). 기본값은 `core.DEFAULT_DELAY`입니다.
  - **기능**: `interval` 시간만큼 대기한 후, `Just.click(location)`을 호출하여 클릭합니다.

- **`double_click(location, interval=DEFAULT_DELAY)`**:
  - **기능**: `interval` 시간만큼 대기한 후, `Just.double_click(location)`을 호출하여 더블 클릭합니다.

- **`right_click(location, interval=DEFAULT_DELAY)`**:
  - **기능**: `interval` 시간만큼 대기한 후, `Just.right_click(location)`을 호출하여 오른쪽 클릭합니다.

---

## `Found` 클래스

- **설명**: 화면에서 특정 아이콘을 발견했을 때만 마우스 동작을 수행합니다. 특정 UI 요소가 나타났을 때만 상호작용해야 하는 경우에 사용됩니다.

- **`click(icon_key, location)`**:
  - **파라미터**:
    - `icon_key` (str): `screen.Found.icon`에서 확인할 아이콘의 키.
    - `location` (tuple): 클릭할 좌표.
  - **기능**: `screen.Found.icon(icon_key)`를 호출하여 화면에 해당 아이콘이 있는지 확인합니다. 아이콘이 존재하면 `Just.click(location)`을 호출하여 지정된 `location`을 클릭합니다.
  - **참고**: 이 함수는 아이콘의 존재 여부만 확인하고, 실제 클릭은 전달받은 `location` 좌표에 수행합니다. 아이콘을 찾아서 그 아이콘의 위치를 클릭하려면 `location.Get.center_location`과 조합해야 합니다. (예: `Found.click("my_icon", Get.center_location("my_icon"))`)

- **`double_click(icon_key, location)`**:
  - **기능**: `screen.Found.icon(icon_key)`로 아이콘 존재 여부를 확인한 후, `Just.double_click(location)`을 호출합니다.

- **`right_click(icon_key, location)`**:
  - **기능**: `screen.Found.icon(icon_key)`로 아이콘 존재 여부를 확인한 후, `Just.right_click(location)`을 호출합니다.

## 의존성

- **`pyautogui`**: 실제 마우스 이벤트를 생성하기 위해 사용됩니다.
- **`time`**: `Waited` 클래스에서 대기 시간을 구현하기 위해 사용됩니다.
- **`core.DEFAULT_DELAY`**: `Waited` 클래스의 기본 대기 시간을 정의합니다.
- **`module.screen`**: `Found` 클래스에서 화면의 아이콘 존재 여부를 확인하는 기능을 사용합니다.
