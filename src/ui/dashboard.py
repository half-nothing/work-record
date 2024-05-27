from PyQt6.QtWidgets import QWidget

from src.ui.forms.generate.dashboard import Ui_DashBoard


class Dashboard(QWidget, Ui_DashBoard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
