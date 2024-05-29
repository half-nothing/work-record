from os import getcwd
from os.path import join
from datetime import datetime
from typing import List, Tuple

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QWidget

from src.manager.database_manager import database
from src.type.types import ReturnType
from src.ui.forms.generate.dashboard import Ui_DashBoard


class Dashboard(QWidget, Ui_DashBoard):
    initialized: bool = False

    def __init__(self):
        super().__init__()
        self.echarts = None
        self.setupUi(self)
        self.webEngineView.setUrl(QUrl.fromLocalFile(join(getcwd(), 'resource/web/index.html')))
        self.webEngineView.loadFinished.connect(self.web_init)

    def web_init(self):
        if self.initialized:
            return
        self.initialized = True
        self.update_time_for_month()
        self.update_times()

    def update_duration_value(self, data: float, month: int = datetime.today().month,
                              year: int = datetime.today().year) -> None:
        if not self.initialized:
            return
        if not data:
            data = 0
        self.webEngineView.page().runJavaScript(
            f"""updateDurationTime({data}, {month}, {year});""")

    def update_time_for_month(self, month: int = datetime.today().month,
                              year: int = datetime.today().year) -> None:
        self.update_duration_value(database.run_command(
            """
            SELECT SUM(record.time) 
            FROM main.record 
            WHERE record.year = ?
            AND record.month = ?
            """,
            [year, month],
            ReturnType.ONE
        )[0], month, year)

    def update_times(self):
        data = self.get_all_records()
        x = []
        y = []
        for record in data:
            y.append(record[0])
            x.append(f"{record[1]}年{record[2]}月")
        self.webEngineView.page().runJavaScript(
            f"""updateAllDurationTime({x}, {y});""")

    @staticmethod
    def get_all_records() -> List[Tuple[int, int, int]]:
        return database.run_command(
            """
            SELECT 
                SUM(record.time) AS "total_time", 
                record.year, 
                record.month 
            FROM 
                record 
            GROUP BY 
                record.year, 
                record.month 
            ORDER BY 
                record.year, 
                record.month
            """,
            return_type=ReturnType.ALL)
