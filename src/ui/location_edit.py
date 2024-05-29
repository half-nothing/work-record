from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog

from src.ui.forms.generate.location_edit import Ui_LocationEdit


class LocationEdit(QDialog, Ui_LocationEdit):
    data_edited_signal: pyqtSignal = pyqtSignal(list)

    def __init__(self, parent=None):
        super(LocationEdit, self).__init__(parent)
        self.setupUi(self)
        self.id_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.address_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.remark_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.confirm.clicked.connect(self.send_data)
        self.cancel.clicked.connect(self.close)

    def accept_data(self, data: list):
        self.id_edit.setText(data[0])
        self.name_edit.setText(data[1])
        self.address_edit.setText(data[2])
        self.remark_edit.setText(data[3])

    def send_data(self):
        data = [
            self.id_edit.text(),
            self.name_edit.text(),
            self.address_edit.text(),
            self.remark_edit.toPlainText()
        ]
        self.data_edited_signal.emit(data)
        self.close()
