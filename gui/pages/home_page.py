from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QApplication,
)


class HomePage(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        layout = QVBoxLayout()

        layout.setContentsMargins(
            40,
            40,
            40,
            40
        )

        layout.setSpacing(20)

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title = QLabel("Stego Tool")

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setStyleSheet(
            "font-size: 28px; font-weight: bold;"
        )

        encode_button = QPushButton(
            "Encode"
        )

        decode_button = QPushButton(
            "Decode"
        )

        exit_button = QPushButton(
            "Exit"
        )

        encode_button.setFixedHeight(42)
        decode_button.setFixedHeight(42)

        encode_button.setFixedWidth(220)
        decode_button.setFixedWidth(220)

        exit_button.setFixedHeight(36)
        exit_button.setFixedWidth(120)

        encode_button.clicked.connect(
            self.main_window.show_encode
        )

        decode_button.clicked.connect(
            self.main_window.show_decode
        )

        exit_button.clicked.connect(
            QApplication.quit
        )

        layout.addWidget(title)

        layout.addWidget(
            encode_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            decode_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addSpacing(10)

        layout.addWidget(
            exit_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.setLayout(layout)
