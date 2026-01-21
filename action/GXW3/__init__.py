from . import work_space_setting
from . import before_sequence

from . import compile
from . import open_tree
from . import program_export_work


class PreWork:
    work_space_setting = work_space_setting.work
    before_sequence = before_sequence.work

class GeneralWork:
    open_tree = open_tree.work
    compile = compile.work
   
class ExportWork:
    export_to_csv = program_export_work.work
    device_export_work = program_export_work.work