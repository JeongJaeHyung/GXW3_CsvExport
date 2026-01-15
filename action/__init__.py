from . import work_space_setting

from . import before_sequence



from . import compile

from . import open_tree

from . import export_to_csv


class WorkManager:
    pass

class PreWork:
    work_space_setting = work_space_setting.work
    before_sequence = before_sequence.work


    pass

class GeneralWork:
    open_tree = open_tree.work
   

class ExportWork:
    export_to_csv = export_to_csv.work

class ShareWork:
    compile = compile
    pass