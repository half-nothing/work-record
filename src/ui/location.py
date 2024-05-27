from PyQt6.QtWidgets import QWidget

from src.ui.forms.generate.location import Ui_Location


class Location(QWidget, Ui_Location):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
