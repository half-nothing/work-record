from PyQt6.QtWidgets import QMainWindow

from src.ui.forms.generate.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
