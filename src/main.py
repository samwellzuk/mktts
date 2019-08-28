# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from view.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())
