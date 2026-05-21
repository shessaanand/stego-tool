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


class DecodePage(QWidget):
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

        decode_button = QPushButton(
            "Decode"
        )

        decode_button.setFixedHeight(42)

        decode_button.clicked.connect(
            self.decode_message
        )

        self.output_box = QTextEdit()

        self.output_box.setReadOnly(True)

        self.output_box.setPlaceholderText(
            "Decoded message appears here"
        )

        self.status_label = QLabel(
            "Status: Ready"
        )

        layout.addWidget(back_button)
        layout.addWidget(select_button)
        layout.addWidget(self.image_label)
        layout.addWidget(decode_button)
        layout.addWidget(self.output_box)
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

    def decode_message(self):
        if not self.image_path:
            self.status_label.setText(
                "Status: Select an image"
            )

            return

        result = subprocess.run(
            [
                "../build/stego",
                "decode",
                self.image_path,
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            output = result.stdout.strip()

            if "Decoded message:" in output:
                output = output.replace(
                    "Decoded message:",
                    ""
                ).strip()

            self.output_box.setText(output)

            self.status_label.setText(
                "Status: Decode successful"
            )

        else:
            error_message = result.stderr.strip()

            if not error_message:
                error_message = "Decode failed"

            self.status_label.setText(
                f"Status: {error_message}"
            )
