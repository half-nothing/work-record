from PyQt6.QtWidgets import QButtonGroup, QMainWindow

from src.ui.forms.generate.main_window import Ui_MainWindow
from src.ui.dashboard import Dashboard
from src.ui.location import Location
from src.ui.work_time import WorkTime


class MainWindow(QMainWindow, Ui_MainWindow):
    dashboard_widget: Dashboard
    location_widget: Location
    work_time_widget: WorkTime
    button_group: QButtonGroup

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.dashboard_widget = Dashboard()
        self.location_widget = Location()
        self.work_time_widget = WorkTime()
        self.body_stacked_widget.addWidget(self.dashboard_widget)
        self.body_stacked_widget.addWidget(self.location_widget)
        self.body_stacked_widget.addWidget(self.work_time_widget)
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.dashboard, 0)
        self.button_group.addButton(self.location, 1)
        self.button_group.addButton(self.work_time, 2)
        self.button_group.button(0).setChecked(True)
        self.button_group.idClicked['int'].connect(lambda n: self.body_stacked_widget.setCurrentIndex(n))