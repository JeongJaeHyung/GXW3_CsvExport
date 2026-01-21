# Action 모듈

`action` 모듈은 GXWorks3 애플리케이션 내에서 특정 자동화 작업을 수행하는 스크립트들을 포함합니다. 각 파일은 전체 자동화 시퀀스의 한 단계를 나타냅니다.

## 모듈 상세 설명

각 모듈의 상세한 기능과 동작 방식은 아래 링크에서 확인할 수 있습니다.

- **`before_sequence.py`**:
  - **목적**: 자동화 시퀀스를 시작하기 전에 초기 설정을 수행합니다.
  - **[상세 설명](./before_sequence.md)**

- **`compile.py`**:
  - **목적**: GXWorks3 프로젝트를 컴파일합니다.
  - **[상세 설명](./compile.md)**

- **`export_to_csv.py`**:
  - **목적**: 특정 프로그램을 CSV 파일로 내보냅니다.
  - **[상세 설명](./export_to_csv.md)**

- **`open_tree.py`**:
  - **목적**: GXWorks3의 프로젝트 트리 구조를 탐색하고 각 항목에 대해 적절한 작업을 수행합니다.
  - **[상세 설명](./open_tree.md)**

- **`work_space_setting.py`**:
  - **목적**: GXWorks3의 작업 공간 설정을 처리하고 초기 팝업창들을 닫습니다.
  - **[상세 설명](./work_space_setting.md)**