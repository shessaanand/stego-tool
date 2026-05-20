import subprocess

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
        layout.setSpacing(15)

        back_button = QPushButton("← Back")
        back_button.clicked.connect(
            self.main_window.show_home
        )

        self.image_label = QLabel("No image selected")

        select_button = QPushButton("Choose Image")
        select_button.clicked.connect(self.select_image)

        self.message_box = QTextEdit()
        self.message_box.setPlaceholderText(
            "Enter secret message"
        )

        encode_button = QPushButton("Encode")
        encode_button.clicked.connect(self.encode_message)

        self.status_label = QLabel("Status: Ready")

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
            self.image_label.setText(file_path)

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
            self.status_label.setText(
                "Status: Encoding failed"
            )
