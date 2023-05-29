import unittest

from bowling import Game

class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_gutter_game(self):
        self.roll_many(0, 20)
        self.assertEqual(0, self.game.total_score())
    
    def test_for_all_nines(self):
        self.roll_many(9, 20)
        self.assertEqual(180, self.game.total_score())

    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(0, 17)
        self.assertEqual(16, self.game.total_score())

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(0, 16)
        self.assertEqual(24, self.game.total_score())

    def test_the_perfect_game(self):
        self.roll_many(10, 12)
        self.assertEqual(300, self.game.total_score())

    
    # helper methods
    def roll_many(self, pins, number):
        for i in range(number):
            self.game.roll(pins)
    
    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)
