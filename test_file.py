import unittest

from game_node import *
from connect_four import *


class TestGame(unittest.TestCase):

    def test_winning_check_1(self):
        board1 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['X', 'X', 'X', ' ', ' ', ' ', ' ']]

        game = ConnectFour(0, "Jerry", "Lester", board=board1)
        result = game.winning_check()
        self.assertEqual(result, TOKEN_2)

    def test_heuristic_1(self):
        board1 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['O', 'O', ' ', ' ', ' ', ' ', ' ']]

        board2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['O', 'O', 'O', ' ', ' ', ' ', ' ']]

        game1 = ConnectFour(1, "Jerry", difficulty=1, board=board1)
        game2 = ConnectFour(1, "Jerry", difficulty=1, board=board2)
        result1 = heuristic(game1, COMPUTER_NAME, COMPUTER_NAME)
        result2 = heuristic(game2, COMPUTER_NAME, COMPUTER_NAME)
        self.assertGreater(result1, result2)

    def test_heuristic_2(self):
        board1 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['X', 'X', ' ', ' ', ' ', ' ', ' ']]

        game1 = ConnectFour(1, "Jerry", difficulty=1, board=board1)
        result1 = heuristic(game1, COMPUTER_NAME, COMPUTER_NAME)
        self.assertNotEqual(result1, 0)

    def test_heuristic_3(self):

        board2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['O', 'O', 'O', ' ', ' ', ' ', ' ']]

        game2 = ConnectFour(1, "Jerry", difficulty=1, board=board2)
        # next player is Computer
        result2 = heuristic(game2, COMPUTER_NAME, "Jerry")
        self.assertGreaterEqual(result2, 200)

    def test_heuristic_4(self):

        board2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['O', 'O', 'O', ' ', ' ', ' ', ' ']]

        game2 = ConnectFour(1, "Jerry", difficulty=1, board=board2)
        # next player is Jerry
        result2 = heuristic(game2, COMPUTER_NAME, COMPUTER_NAME)
        self.assertLessEqual(result2, -200)


    def test_move_1(self):
        board1 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', 'X', 'O', ' ', ' '],
                  ['O', ' ', 'O', 'X', 'X', 'X', ' '],
                  ['O', 'O', 'X', 'X', 'O', 'X', ' ']]

        game1 = ConnectFour(1, "Jerry", difficulty=1, board=board1)
        game1.num_empty = 30  # input any number you want!
        move = find_next_move(game1, COMPUTER_NAME, 1)
        self.assertEqual(move, 3)
        move = find_next_move(game1, COMPUTER_NAME, 2)
        self.assertEqual(move, 3)
        # move = find_next_move(game1, COMPUTER_NAME, 3)
        # self.assertEqual(move, 3)
        # move = find_next_move(game1, COMPUTER_NAME, 4)
        # self.assertEqual(move, 3)

    def test_move_2(self):
        board1 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', 'O', 'X', 'O', 'O', ' ', ' '],
                  [' ', 'X', 'X', 'O', 'X', ' ', ' '],
                  ['X', 'O', 'X', 'X', 'O', 'O', 'O']]

        game1 = ConnectFour(1, "Jerry", difficulty=1, board=board1)
        game1.num_empty = 30  # input any number you want!
        move = find_next_move(game1, COMPUTER_NAME, 1)
        self.assertEqual(move, 2)

    def test_move_3(self):
        board1 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', 'O', ' ', ' '],
                  [' ', ' ', ' ', 'X', 'O', ' ', ' '],
                  [' ', ' ', ' ', 'X', 'X', ' ', ' '],
                  ['O', ' ', ' ', 'X', 'O', ' ', ' ']]

        game1 = ConnectFour(1, "Jerry", difficulty=1, board=board1)
        game1.num_empty = 30  # input any number you want!
        move = find_next_move(game1, COMPUTER_NAME, 1)
        self.assertEqual(move, 3)
        move = find_next_move(game1, COMPUTER_NAME, 2)
        self.assertEqual(move, 3)

    def test_move_4(self):
        board1 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', 'O', 'X', ' ', ' ', ' ', ' '],
                  [' ', 'X', 'X', 'O', ' ', ' ', ' '],
                  [' ', 'X', 'X', 'O', 'O', ' ', ' ']]

        game1 = ConnectFour(1, "Jerry", difficulty=1, board=board1)
        game1.num_empty = 30  # input any number you want!
        move = find_next_move(game1, COMPUTER_NAME, 1)
        self.assertEqual(move, 2)
        move = find_next_move(game1, COMPUTER_NAME, 2)
        self.assertEqual(move, 2)

if (__name__ == "__main__"):
    runner = unittest.TextTestRunner(verbosity=1)
    unittest.main(testRunner=runner, exit=False)
