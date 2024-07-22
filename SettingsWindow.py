from PyQt5.QtWidgets import QDialog, QLabel, QSpinBox, QPushButton, QVBoxLayout


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Настройки")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #303134; color: #CCCCCC; font-size: 15px;")

        self.num_moves_label = QLabel("Количество ходов:")
        self.num_moves_spinbox = QSpinBox()
        self.num_moves_spinbox.setMinimum(1)
        self.num_moves_spinbox.setMaximum(100)
        self.num_moves_spinbox.setValue(20)

        self.num_colors_label = QLabel("Количество цветов:")
        self.num_colors_spinbox = QSpinBox()
        self.num_colors_spinbox.setMinimum(2)
        self.num_colors_spinbox.setMaximum(25)
        self.num_colors_spinbox.setValue(5)

        self.field_size_label_nX = QLabel("Ширина поля:")
        self.field_size_nX = QSpinBox()
        self.field_size_nX.setMinimum(5)
        self.field_size_nX.setMaximum(35)
        self.field_size_nX.setValue(10)

        self.field_size_label_nY = QLabel("Высота поля:")
        self.field_size_nY = QSpinBox()
        self.field_size_nY.setMinimum(5)
        self.field_size_nY.setMaximum(18)
        self.field_size_nY.setValue(10)

        self.confirm_button = QPushButton("Начать игру")
        self.confirm_button.setStyleSheet("background-color: #404144")
        self.confirm_button.clicked.connect(self.on_confirm)

        layout = QVBoxLayout()
        layout.addWidget(self.num_moves_label)
        layout.addWidget(self.num_moves_spinbox)
        layout.addWidget(self.num_colors_label)
        layout.addWidget(self.num_colors_spinbox)
        layout.addWidget(self.field_size_label_nX)
        layout.addWidget(self.field_size_nX)
        layout.addWidget(self.field_size_label_nY)
        layout.addWidget(self.field_size_nY)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def on_confirm(self):
        num_moves = self.num_moves_spinbox.value()
        num_colors = self.num_colors_spinbox.value()
        nX = self.field_size_nX.value()
        nY = self.field_size_nY.value()
        if num_moves > 0 and num_colors > 0 and nX > 0 and nY > 0:
            self.accept()

    def get_settings(self):
        num_moves = self.num_moves_spinbox.value()
        num_colors = self.num_colors_spinbox.value()
        nX = self.field_size_nX.value()
        nY = self.field_size_nY.value()
        return num_moves, num_colors, nX, nY
