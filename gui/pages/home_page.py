from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class HomePage(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        title = QLabel("Stego Tool")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        encode_button = QPushButton("Encode")
        decode_button = QPushButton("Decode")

        encode_button.setFixedHeight(40)
        decode_button.setFixedHeight(40)

        encode_button.clicked.connect(
            self.main_window.show_encode
        )

        decode_button.clicked.connect(
            self.main_window.show_decode
        )

        layout.addWidget(title)
        layout.addWidget(encode_button)
        layout.addWidget(decode_button)

        self.setLayout(layout)
