# Imagine a game with one or more rats can attack a player. each individual rat
# has an initial attack value of 1. However, rats attack as a swarm so each rat’s
# attack value is actually equal to the total number of rats in play.
# Given that a rat enters play through the initializer and leave play (dies)
# via its __exit__ method, please implement the Game and Rat classes so that at,
# any point in the game the attack value of a rat is always consistent.



import unittest

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Game:
    def __init__(self):
        self.rat_born = Event()
        self.rat_dies = Event()

class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1

        self.game.rat_born.append(self.rat_born)
        self.game.rat_dies.append(self.rat_dies)

        self.game.rat_born()


    def rat_born(self):
        self.attack = len(self.game.rat_born)

    def rat_dies(self, x):
        self.attack -= 1
        if x == self:
            self.game.rat_dies.remove(x.rat_dies)
            self.game.rat_born.remove(x.rat_born)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.rat_dies(self)

class Evaluate(unittest.TestCase):
    def test_single_rat(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):
        game = Game()
        rat = Rat(game)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)


if __name__ == '__main__':
     unittest.main()

# if __name__ == '__main__':
#     game = Game()
#     rat1 = Rat(game)
#     rat2 = Rat(game)
#     print(rat1.attack)
#     print(rat2.attack)
#     with Rat(game) as rat3:
#         print(rat3.attack)
#         print(rat2.attack)
#     print(rat1.attack)
#     print(rat2.attack)
