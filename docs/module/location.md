# location.py

## 목적

`location` 모듈은 화면의 특정 위치를 찾는 간단하고 명확한 방법을 제공합니다. 주로 화면에 나타나는 특정 아이콘 이미지의 중심 좌표를 가져오는 데 사용됩니다.

---

## `Get` 클래스

- **설명**: 화면에서 무언가를 '가져오는(Get)' 기능들을 모아놓은 클래스입니다. 현재는 이미지의 위치를 가져오는 기능만 포함되어 있습니다.

- **`center_location(image_path)`**:
  - **파라미터**: `image_path` (str) - `core.ICONS` 딕셔너리에 정의된 아이콘의 키(key) 이름입니다. 이 키는 실제 이미지 파일 경로와 매핑되어 있습니다.
  - **기능**:
    1. `core.ICONS[image_path]`를 통해 `image_path` 키에 해당하는 실제 이미지 파일의 경로를 가져옵니다.
    2. `pyautogui.locateCenterOnScreen()` 함수를 호출하여 전체 화면에서 해당 이미지와 일치하는 영역을 찾습니다.
    3. 이미지 인식의 정확도는 `core.CONFIDENCE` 설정값을 따릅니다.
    4. 이미지를 성공적으로 찾으면, 해당 이미지 영역의 **중앙** x, y 좌표를 튜플 형태로 반환합니다.
    5. 이미지를 찾지 못하면 `pyautogui`는 `ImageNotFoundException`을 발생시키거나 `None`을 반환할 수 있습니다 (이 코드에서는 예외 처리가 호출하는 쪽에서 이루어져야 함).

- **사용 예시**:
  ```python
  # 'Navigation' 아이콘의 중앙 좌표를 찾아서 nav_pos 변수에 저장
  nav_pos = Get.center_location("Navigation")
  
  # 찾은 좌표를 mouse.click과 같은 다른 함수에 전달하여 사용
  if nav_pos:
      mouse.Just.click(nav_pos)
  ```

## 의존성

- **`pyautogui`**: 화면에서 이미지를 찾고 그 좌표를 반환하는 핵심 기능을 수행합니다.
- **`core.ICONS`**: 아이콘 키와 실제 이미지 파일 경로를 매핑하는 딕셔너리입니다.
- **`core.CONFIDENCE`**: `pyautogui`가 이미지를 찾을 때 사용할 신뢰도(정확도) 값입니다.
