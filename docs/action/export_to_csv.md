# export_to_csv.py

## 목적

`export_to_csv` 모듈은 GXWorks3의 특정 프로그램 블록을 CSV 파일로 내보내는 자동화 스크립트입니다. 이 기능은 주로 `open_tree.py`에서 프로그램 블록 노드를 발견했을 때 호출됩니다.

## 주요 기능

### `work(t_center)` 함수

- **파라미터**:
  - `t_center`: 내보내고자 하는 대상 프로그램 블록 노드의 화면상 중앙 좌표.

- **설명**:
  이 함수는 `t_center` 좌표를 기준으로 마우스 우클릭 메뉴를 열고, 'Export to CSV' 관련 메뉴를 탐색하여 실행합니다. 내보내기 과정에서 발생할 수 있는 여러 대화상자(에러, 경고 등)를 자동으로 처리합니다.

- **동작 순서**:
  1. `Waited.hotkey_press(['ctrl', 'shift', 'q'])`: 다른 창이 활성화되어 있을 경우를 대비해 포커스를 초기화하거나 특정 모드로 전환하는 역할을 할 수 있습니다.
  2. `Waited.right_click(t_center)`: 대상 프로그램 블록의 위치에서 마우스 오른쪽 버튼을 클릭하여 컨텍스트 메뉴를 엽니다.
  3. `Waited.key_press('e')`: 컨텍스트 메뉴에서 'Export...' 또는 유사한 이름의 항목으로 빠르게 이동하기 위해 'E' 키를 누릅니다.
  4. `Waited.key_press('down')`: 'Export to CSV' 메뉴 항목을 정확히 선택하기 위해 아래 방향키를 누릅니다.
  5. `Waited.key_press('enter')`: 메뉴를 실행합니다.
  6. `if Found.icon("Statement") is not None:`:
     - 'Statement' 관련 에러 팝업이 나타나는지 확인합니다.
     - 만약 나타나면, 'Enter' 키를 눌러 팝업을 닫습니다.
  7. `Waited.Found.key_press("Warning", 'left', ...)`: '다른 이름으로 저장' 대화상자에서 파일 덮어쓰기 관련 'Warning' 아이콘이 나타나는 경우를 처리합니다. '왼쪽' 방향키를 눌러 '예' 버튼으로 포커스를 이동하려는 의도일 수 있습니다.
  8. `Waited.key_press('enter', ...)` (2회): 파일 저장 및 덮어쓰기 확인을 위해 'Enter'를 두 번 누릅니다.
  9. `if Found.icon("Warning") is not None:`:
     - CSV 파일이 이미 저장되어 있다는 내용의 추가 경고창이 뜨는지 확인합니다.
     - 경고창이 있으면 'Enter'와 'Esc'를 눌러 창을 닫습니다.
  10. `Waited.key_press('esc', 0.1)`: 열려 있을 수 있는 추가적인 창이나 메뉴를 닫습니다.
  11. `Waited.hotkey_press(['ctrl', 'shift', 'q'], 0.1)`: 포커스를 다시 초기화합니다.
  12. `Waited.click(Found.icon("Navigation"))`: 'Navigation' 창을 다시 클릭하여 포커스를 프로젝트 트리로 되돌립니다.
  13. `Waited.key_press('up')` (2회) 및 `Waited.key_press('enter')`: CSV 내보내기가 완료된 후, 다음 탐색을 위해 프로젝트 트리 내에서 위치를 조정하는 과정일 수 있습니다.

## 의존성

- **`module.Waited`**: 시간 지연을 포함한 키 입력, 핫키, 마우스 클릭을 위해 사용됩니다.
- **`module.Found`**: 화면에서 'Statement', 'Warning', 'Navigation'과 같은 특정 아이콘의 존재 유무를 확인하는 데 사용됩니다.
