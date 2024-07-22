import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QPushButton, \
    QHBoxLayout, QWidget, QVBoxLayout, QMessageBox, QLabel
from PyQt5.QtGui import QColor


class MainWindow(QMainWindow):
    def __init__(self, player, game):
        super().__init__()

        self.player = player
        self.game = game
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setFrameStyle(QGraphicsView.NoFrame)
        self.setCentralWidget(self.view)

        self.setWindowTitle("repaint")
        self.resize(self.player.nX * 50 + 200, self.player.nY * 50 + 200)

        self.setStyleSheet("background-color: #202124;")

        self.draw_fild()
        color_widget = self.draw_buttons()

        moves_label = QLabel("Оставшиеся ходы: {}".format(self.player.number_of_moves))
        moves_label.setAlignment(Qt.AlignCenter)
        moves_label.setStyleSheet("font-size: 25px; color: #CCCCCC;")

        main_layout = QVBoxLayout()
        main_layout.addWidget(moves_label)
        main_layout.addWidget(self.view)
        main_layout.addWidget(color_widget, alignment=Qt.AlignCenter)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.setWindowTitle("")
        self.resize(self.player.nX * 50 + 200, self.player.nY * 50 + 250)

        home_button = QPushButton("Домой")
        home_button.setStyleSheet("background-color: #FF4848; color: #FFFFFF;")  # Стиль кнопки
        home_button.setFixedSize(100, 50)  # Размер кнопки

        # Подключение обработчика событий для кнопки "Домой"
        home_button.clicked.connect(self.go_home)

        main_layout.addWidget(home_button, alignment=Qt.AlignCenter)  # Добавление кнопки на макет

    def go_home(self):
        self.close()

    def color_button_clicked(self, idx):
        color_index = idx
        if color_index != self.player.fild[0][0] and self.player.number_of_moves != 0:
            self.game.process_color()
            self.game.repaint_fild(color_index)
            self.draw_fild()
            self.player.number_of_moves -= 1
            self.update_moves_label()
            if self.game.count_colors() == 1:
                self.end_game("Вы победили!")
            if self.player.number_of_moves == 0:
                self.end_game("Вы проиграли!")

    def end_game(self, result):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Конец Игры")
        msgBox.setText(result)
        msgBox.setStyleSheet("QLabel { color : #CCCCCC; } QMessageBox { background-color: #303134; }")
        msgBox.exec_()
        sys.exit(app.exec_())

    def draw_fild(self):
        self.scene.clear()
        for y in range(self.player.nY):
            for x in range(self.player.nX):
                square = QGraphicsRectItem(x * 50, y * 50, 50, 50)
                square.setBrush(self.player.colors[self.player.fild[y][x]])
                square.setPen(QColor(0, 0, 0, 0))
                self.scene.addItem(square)

    def draw_buttons(self):
        color_layout = QHBoxLayout()
        color_widget = QWidget()
        color_widget.setLayout(color_layout)
        for i, color in enumerate(self.player.colors):
            color_button = QPushButton()
            color_button.setStyleSheet("background-color: " + color.name())
            color_button.setFixedSize(50, 50)
            color_button.clicked.connect(lambda _, idx=i: self.color_button_clicked(idx))
            color_layout.addWidget(color_button)
        return color_widget

    def update_moves_label(self):
        self.findChild(QLabel).setText("Оставшиеся ходы: {}".format(self.player.number_of_moves))