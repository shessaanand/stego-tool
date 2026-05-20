import subprocess

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
        layout.setSpacing(15)

        back_button = QPushButton("← Back")
        back_button.clicked.connect(
            self.main_window.show_home
        )

        self.image_label = QLabel("No image selected")

        select_button = QPushButton("Choose Image")
        select_button.clicked.connect(self.select_image)

        decode_button = QPushButton("Decode")
        decode_button.clicked.connect(self.decode_message)

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)

        self.status_label = QLabel("Status: Ready")


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
            self.image_label.setText(file_path)

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
            self.output_box.setText(result.stdout)
            self.status_label.setText(
                "Status: Decode successful"
            )
        else:
            self.status_label.setText(
                "Status: Decode failed"
            )
