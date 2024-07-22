from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QMessageBox
from Game_Logic import Game_Logic
from Player import Player
from MainWindow import MainWindow
from SettingsWindow import SettingsWindow


class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Перекраска")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #202124; color: #CCCCCC; font-size: 15px;")

        self.start_game_button = QPushButton("Начать игру")
        self.settings_button = QPushButton("Настройки")
        self.about_button = QPushButton("Об игре")

        layout = QVBoxLayout()
        layout.addWidget(self.start_game_button)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.about_button)

        button_width = 200
        button_height = 50
        self.start_game_button.setFixedSize(button_width, button_height)
        self.settings_button.setFixedSize(button_width, button_height)
        self.about_button.setFixedSize(button_width, button_height)

        layout = QVBoxLayout()
        layout.addWidget(self.start_game_button)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.about_button)
        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.start_game_button.setStyleSheet("background-color: #303134")
        self.settings_button.setStyleSheet("background-color: #303134")
        self.about_button.setStyleSheet("background-color: #303134")

        self.start_game_button.clicked.connect(self.start_game)
        self.settings_button.clicked.connect(self.open_settings)
        self.about_button.clicked.connect(self.show_about)

    def start_game(self):
        player = Player(10, 12, 5, 20)
        game = Game_Logic(player)
        window = MainWindow(player, game)
        window.show()

    def open_settings(self):
        settings_window = SettingsWindow()
        if settings_window.exec_() == QDialog.Accepted:
            num_moves, num_colors, nX, nY = settings_window.get_settings()
            player = Player(nX, nY, num_colors, num_moves)
            game = Game_Logic(player)
            window = MainWindow(player, game)
            window.show()

    def show_about(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Об Игре")
        msgBox.setText(
            "Перекраска - захватывающая игра, где ваше воображение и логическое мышление будут подвергнуты испытанию!"
            + " Игра сочетает в себе элементы головоломки и стратегии, и ваша задача - перекрасить поле в один цвет за ограниченное количество ходов." + "\n " + "\n " +
            "Цель игры: Перекрасить все клетки поля в один цвет." + "\n " +"\n "+
            "Ходы: У вас есть ограниченное количество ходов, чтобы достичь цели. Каждый ход - это возможность выбрать цвет, которым будете перекрашивать поле." + "\n "+"\n " +
            "Стратегия: Выбирайте ходы так, чтобы максимально эффективно использовать свои ресурсы и быстро достичь победы." +"\n "+ "\n " +
            "Победа: Когда все клетки поля окрашены в один цвет, вы выигрываете игру!" + "\n "+"\n " +
            "Наслаждайтесь ощущением удовлетворения от успешно завершенной головоломки.")
        msgBox.setStyleSheet("QLabel { color : #CCCCCC; } QMessageBox { background-color: #303134; }")
        msgBox.exec_()
