from PyQt6.QtWidgets import QWidget

from src.ui.forms.generate.work_time import Ui_WorkTime


class WorkTime(QWidget, Ui_WorkTime):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
