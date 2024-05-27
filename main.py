import sys

from PyQt6.QtWidgets import QApplication, QStyleFactory

from src.ui.main_window import MainWindow

import images


def main() -> None:
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("fusion"))
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
