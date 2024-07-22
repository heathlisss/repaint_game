import random

from PyQt5.QtGui import QColor


class Player:
    def __init__(self, nX, nY, count_color, number_of_moves):
        self.nX = nX
        self.nY = nY
        self.number_of_moves = number_of_moves
        self.count_color = count_color
        self.fild = [[0] * nX for i in range(nY)]
        self.colors = []
        self.generate_random_colors()
        self.init_fild()

    def init_fild(self):
        for y in range(self.nY):
            for x in range(self.nX):
                self.fild[y][x] = random.randint(0, len(self.colors) - 1)

    def generate_random_colors(self):
        for _ in range(self.count_color):
            random_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.colors.append(random_color)
