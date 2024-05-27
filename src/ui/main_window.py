from PyQt6.QtWidgets import QMainWindow

from src.ui.forms.generate.main_window import Ui_MainWindow
from src.ui.dashboard import Dashboard
from src.ui.location import Location
from src.ui.work_time import WorkTime


class MainWindow(QMainWindow, Ui_MainWindow):
    dashboard: Dashboard
    location: Location
    work_time: WorkTime

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.dashboard = Dashboard()
        self.location = Location()
        self.work_time = WorkTime()
        self.body_stacked_widget.addWidget(self.dashboard)
        self.body_stacked_widget.addWidget(self.location)
        self.body_stacked_widget.addWidget(self.work_time)
