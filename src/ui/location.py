from typing import List, Tuple

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QAbstractItemView, QTableWidgetItem, QWidget

from src.base.logger import logger
from src.manager.database_manager import database
from src.type.types import ReturnType
from src.ui.forms.generate.location import Ui_Location
from src.ui.location_edit import LocationEdit


class Location(QWidget, Ui_Location):
    editor: LocationEdit

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.editor = LocationEdit(self)
        self.table_init()
        self.locationList.doubleClicked.connect(self.edit_location)
        self.editor.data_edited_signal.connect(self.update_location)

    def edit_location(self):
        data = self.locationList.selectedItems()
        temp = []
        for i in data:
            temp.append(i.text())
        self.editor.accept_data(temp)
        self.editor.show()

    def update_location(self, data: list):
        temp = database.run_command(
            """
            SELECT id FROM main.location WHERE id = ?
            """,
            [int(data[0])],
            ReturnType.ALL
        )
        if len(temp) == 0:
            database.run_command(
                """
                INSERT INTO main.location (name, address, remark) VALUES (?, ?, ?)
                """,
                data[1:]
            )
        else:
            database.run_command(
                """
                UPDATE main.location SET name = ?, address = ?, remark = ? WHERE id = ?
                """,
                [data[1], data[2], data[3], int(data[0])],
            )
        self.load_location_data()

    def table_init(self):
        self.locationList.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.locationList.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.locationList.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.locationList.horizontalHeader().setHighlightSections(False)
        self.locationList.horizontalHeader().setStretchLastSection(True)
        self.locationList.setColumnWidth(2, 200)
        self.load_location_data()

    def load_location_data(self):
        locations = self.get_locations()
        self.locationList.setRowCount(length := len(locations))
        for i, location in zip(range(length), locations):
            for index in range(self.locationList.columnCount()):
                item = QTableWidgetItem(str(location[index]))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.locationList.setItem(i, index, item)

    @staticmethod
    def get_locations() -> List[Tuple[int, str, str, str, int, int]]:
        return database.run_command("""SELECT * FROM main.location""", return_type=ReturnType.ALL)
