class Game_Logic:
    def __init__(self, player):
        self.player = player
        self.repainting_table = [[0] * self.player.nX for i in range(self.player.nY)]

    def process_color(self):
        id_color = self.player.fild[0][0]
        visiting_cage = set()
        self.finding_way(visiting_cage, 0, id_color)
        visiting_cage.clear()

    def finding_way(self, visiting_cage, id_cage, id_color):
        visiting_cage.add(id_cage)
        i = int(id_cage / 100)
        j = int(id_cage % 100)
        self.repainting_table[i][j] = 1
        if i + 1 < len(self.repainting_table) and self.player.fild[i + 1][j] == id_color and not (
                id_cage + 100 in visiting_cage):
            self.finding_way(visiting_cage, id_cage + 100, id_color)
        if i - 1 >= 0 and self.player.fild[i - 1][j] == id_color and not (id_cage - 100 in visiting_cage):
            self.finding_way(visiting_cage, id_cage - 100, id_color)
        if j + 1 < len(self.repainting_table[0]) and self.player.fild[i][
            j + 1] == id_color and not (id_cage + 1 in visiting_cage):
            self.finding_way(visiting_cage, id_cage + 1, id_color)
        if j - 1 >= 0 and self.player.fild[i][j - 1] == id_color and not (id_cage - 1 in visiting_cage):
            self.finding_way(visiting_cage, id_cage - 1, id_color)

    def count_colors(self):
        count = set()
        for i in range(self.player.nY):
            for j in range(self.player.nX):
                if not (self.player.fild[i][j] in count):
                    count.add(self.player.fild[i][j])
        return len(count)

    def repaint_fild(self, id_color):
        for i in range(self.player.nY):
            for j in range(self.player.nX):
                if self.repainting_table[i][j] == 1:
                    self.player.fild[i][j] = id_color
