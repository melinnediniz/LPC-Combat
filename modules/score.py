from config import Color


class Score:
    def __init__(self):
        self.score_1 = 0
        self.score_2 = 0
        self.color_1 = Color['GREEN']
        self.color_2 = Color['BLUE']

    def update(self, score):
        if score == 1:
                self.score_1 +=1
        elif score == 2:
                self.score_2 += 1

    def reset(self):
        self.score_1 = 0
        self.score_2 = 0
