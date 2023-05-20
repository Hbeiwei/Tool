import sys
from PySide6.QtWidgets import QMainWindow
from gpt_ui import Ui_MainWindow
from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.load(QUrl("https://poe.com/"))
        self.ui.actionpin.toggled.connect(self.pin_windows)

    def pin_windows(self, checked):
        if checked:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("ChatNow")
    app.setApplicationDisplayName("ChatNow")
    app.setWindowIcon(QIcon("resources/icon/brand.png"))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
