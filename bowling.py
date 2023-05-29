class Game(object):

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def total_score(self):
        score = 0
        roll_index = 0
        for frame in range(10):
            score += self.rolls[roll_index] + self.rolls[roll_index + 1]
            roll_index += 2
        return score