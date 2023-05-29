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
    
    # helper method
    def roll_many(self, pins, number):
        for i in range(number):
            self.game.roll(pins)