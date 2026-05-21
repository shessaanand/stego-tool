from PyQt6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
)

from PyQt6.QtGui import QGuiApplication

from pages.home_page import HomePage
from pages.encode_page import EncodePage
from pages.decode_page import DecodePage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Stego Tool"
        )

        self.setFixedSize(700, 500)

        screen = QGuiApplication.primaryScreen()

        geometry = screen.availableGeometry()

        x = (
            geometry.width() - self.width()
        ) // 2

        y = (
            geometry.height() - self.height()
        ) // 2

        self.move(x, y)

        self.stack = QStackedWidget()

        self.home_page = HomePage(self)

        self.encode_page = EncodePage(self)

        self.decode_page = DecodePage(self)

        self.stack.addWidget(
            self.home_page
        )

        self.stack.addWidget(
            self.encode_page
        )

        self.stack.addWidget(
            self.decode_page
        )

        self.setCentralWidget(
            self.stack
        )

        self.stack.setCurrentWidget(
            self.home_page
        )

    def show_home(self):
        self.stack.setCurrentWidget(
            self.home_page
        )

    def show_encode(self):
        self.stack.setCurrentWidget(
            self.encode_page
        )

    def show_decode(self):
        self.stack.setCurrentWidget(
            self.decode_page
        )
        
