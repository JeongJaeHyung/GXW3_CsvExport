# open_tree.py

## 목적

`open_tree` 모듈은 GXWorks3 자동화의 핵심 로직 중 하나로, 프로젝트의 트리 구조를 탐색하고 각 노드의 유형에 따라 적절한 작업을 수행하는 역할을 합니다.

## 주요 기능

### `work()` 함수

- **설명**:
  이 함수는 'Navigation' 창에서 아래 방향키를 눌러가며 프로젝트 트리를 순차적으로 탐색합니다. 각 단계에서 인식된 노드(아이콘)의 종류에 따라 분기 처리를 수행하며, 'ProgramBlock' 노드를 찾으면 CSV로 내보내는 작업을 호출하고, 'Parameter' 노드를 찾으면 탐색을 종료합니다.

- **주요 변수**:
  - `node_list`: 탐색 대상이 되는 노드들의 이름 리스트입니다. (`Program`, `Scan`, `Unit`, `Folder`, `ProgramBlock1`, `ProgramBlock2`, `Parameter`)
  - `start_point`, `end_point`: `node_list`에서 현재 탐색할 아이콘의 범위를 지정하는 인덱스입니다.
  - `base_nodes`: 하위 트리를 열어야 하는 기본 노드 그룹입니다.
  - `programblock`: CSV로 내보내야 하는 프로그램 블록 노드 그룹입니다.

- **동작 순서**:
  1. `Waited.click(Found.icon("Navigation"))`: 'Navigation' 창을 클릭하여 탐색을 시작할 준비를 합니다.
  2. `while True:` 루프:
     - `Just.key_press("down")`: 아래 방향키를 눌러 트리에서 다음 항목으로 이동합니다.
     - `result = Found.icon_list(...)`: 현재 포커스된 위치에서 `node_list`의 지정된 범위(`start_point`:`end_point`)에 해당하는 아이콘이 있는지 찾습니다.
     - `if result is not None:` (아이콘을 찾은 경우):
       - `position`, `target`: 찾은 아이콘의 화면상 위치와 노드 이름입니다.
       - `if target in "Parameter":`: 'Parameter' 노드를 찾으면 모든 탐색이 완료된 것으로 간주하고 함수를 종료합니다.
       - `elif target in programblock:`: 'ProgramBlock' 노드를 찾으면, `ExportWork(position)`를 호출하여 해당 블록을 CSV 파일로 내보내는 작업을 수행합니다. (`ExportWork`는 `export_to_csv.py`의 `work` 함수입니다.)
       - `elif target in base_nodes:`: 'Program', 'Scan', 'Unit' 등 하위 항목을 포함하는 기본 노드를 찾으면, `Just.key_press('enter')`를 통해 트리를 확장합니다.
         - 만약 'Scan' 노드를 열었다면, 다음 탐색 대상이 'Unit', 'Folder', 'ProgramBlock'이 될 수 있으므로 `start_point`와 `end_point`를 조정하여 탐색 범위를 변경합니다.
     - `else:` (아이콘을 찾지 못한 경우):
       - 지정된 시간 내에 예상된 노드를 찾지 못한 경우, 탐색 범위를 조정(`start_point`, `end_point`)하여 다음 단계에서 다른 종류의 노드를 찾도록 시도합니다. 이는 트리 구조의 깊이나 상태에 따라 유연하게 대응하기 위한 로직입니다.

## 의존성

- **`module.Just`**: 즉각적인 키 입력을 위해 사용됩니다.
- **`module.Found`**: 화면에서 특정 아이콘 또는 아이콘 목록을 찾는 데 사용됩니다.
- **`module.Waited`**: 시간 지연을 포함한 클릭을 위해 사용됩니다.
- **`action.export_to_csv.work` (as `ExportWork`)**: 프로그램 블록을 CSV로 내보내기 위해 호출됩니다.
- **`core.NODE_OPEN_TIMEOUT`**: 노드를 찾는 데 사용할 최대 대기 시간입니다.
