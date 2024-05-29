from datetime import datetime
from typing import List, Tuple

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QAbstractItemView, QTableWidgetItem, QWidget

from src.manager.database_manager import database
from src.type.types import ReturnType
from src.ui.forms.generate.work_time import Ui_WorkTime


class WorkTime(QWidget, Ui_WorkTime):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table_init()
        self.date_edit.setDateTime(datetime.today())
        self.add.clicked.connect(self.add_record)

    def table_init(self):
        self.record_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.record_list.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.record_list.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.record_list.horizontalHeader().setHighlightSections(False)
        self.record_list.horizontalHeader().setStretchLastSection(True)
        self.record_list.setColumnWidth(2, 200)
        self.load_record_data()
        self.load_location_data()

    def load_record_data(self):
        records = self.get_records()
        self.record_list.setRowCount(length := len(records))
        for i, location in zip(range(length), records):
            for index in range(self.record_list.columnCount()):
                item = QTableWidgetItem(str(location[index]))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.record_list.setItem(i, index, item)

    def load_location_data(self):
        locations = self.get_locations()
        for location in locations:
            self.location_select.addItem(location[1])

    def add_record(self):
        date = self.date_edit.date()
        database.run_command(
            """
            INSERT INTO main.record (location_id, time, year, month, day) VALUES (?, ?, ?, ?, ?);
            """,
            [self.location_select.currentIndex() + 1, self.time_edit.text(), date.year(), date.month(), date.day()]
        )
        self.load_record_data()

    @staticmethod
    def get_records() -> List[Tuple[int, str, str, str, int, int]]:
        return database.run_command(
            """
            SELECT
                location.name, 
                record.time, 
                record.year, 
                record.month, 
                record.day
            FROM
                location
                INNER JOIN
                record
                ON location.id = record.location_id
            """, return_type=ReturnType.ALL)

    @staticmethod
    def get_locations() -> List[Tuple[int, str, str, str, int, int]]:
        return database.run_command("""SELECT * FROM main.location""", return_type=ReturnType.ALL)
