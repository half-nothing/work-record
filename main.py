import sys

from PyQt6.QtWidgets import QApplication, QStyleFactory
from resource import *

from src.ui.main_window import MainWindow
from src.utils.qss_loader import QSSLoader


def main() -> None:
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("light fusion"))
    app.setStyleSheet(QSSLoader.readQssResource(":/style/style/style.qss"))
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
