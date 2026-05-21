import subprocess
import os

from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QTextEdit,
    QFileDialog,
    QVBoxLayout,
)


class EncodePage(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.image_path = ""

        layout = QVBoxLayout()

        layout.setContentsMargins(
            40,
            40,
            40,
            40
        )

        layout.setSpacing(20)

        back_button = QPushButton("← Back")
        back_button.setFixedHeight(42)

        back_button.clicked.connect(
            self.main_window.show_home
        )

        self.image_label = QLabel(
            "No image selected"
        )

        select_button = QPushButton(
            "Choose Image"
        )

        select_button.setFixedHeight(42)

        select_button.clicked.connect(
            self.select_image
        )

        self.message_box = QTextEdit()

        self.message_box.setPlaceholderText(
            "Enter secret message"
        )

        encode_button = QPushButton(
            "Encode"
        )

        encode_button.setFixedHeight(42)

        encode_button.clicked.connect(
            self.encode_message
        )

        self.status_label = QLabel(
            "Status: Ready"
        )

        layout.addWidget(back_button)
        layout.addWidget(select_button)
        layout.addWidget(self.image_label)
        layout.addWidget(self.message_box)
        layout.addWidget(encode_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select PNG",
            "",
            "PNG Files (*.png)"
        )

        if file_path:
            self.image_path = file_path

            filename = os.path.basename(
                file_path
            )

            self.image_label.setText(
                filename
            )

    def encode_message(self):
        if not self.image_path:
            self.status_label.setText(
                "Status: Select an image"
            )

            return

        message = self.message_box.toPlainText()

        if not message:
            self.status_label.setText(
                "Status: Message is empty"
            )

            return

        output_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Encoded Image",
            "encoded.png",
            "PNG Files (*.png)"
        )

        if not output_path:
            return

        result = subprocess.run(
            [
                "../build/stego",
                "encode",
                self.image_path,
                output_path,
                message,
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            self.status_label.setText(
                "Status: Encoding successful"
            )

        else:
            error_message = result.stderr.strip()

            if not error_message:
                error_message = "Encoding failed"

            self.status_label.setText(
                f"Status: {error_message}"
            )
