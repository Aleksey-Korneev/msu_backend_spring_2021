"""This module contains tests for TicTacGame class."""

import unittest
from tictac import TicTacGame
import sys


correct_output = """Ход игрока X.
row = col = Ход игрока X.
row = col = Недопустимые координаты.
Ход игрока X.
row = col = Недопустимые координаты.
Ход игрока X.
row = col = Недопустимые координаты.
Ход игрока X.
row = col = Некорректный ввод.
Ход игрока X.
row = col = Некорректный ввод.
Ход игрока X.
row = col = Некорректный ввод.
Ход игрока X.
row = col = Некорректный ввод.
Ход игрока X.
row = col = """


class TestTicTacGame(unittest.TestCase):
    """
    Test class for TicTacGame class.
    """

    def setUp(self):
        self.game = TicTacGame()

    def test_init(self):
        self.assertEqual(self.game.board_size, 3)
        self.assertListEqual(self.game.board, [[" "] * 3 for _ in range(3)])
        self.assertEqual(self.game.player, "X")

    def test_switch_player(self):
        player = self.game.player
        self.game.switch_player()
        if player == "X":
            self.assertEqual(self.game.player, "O")
        else:
            self.assertEqual(self.game.player, "X")
        new_game = TicTacGame()
        new_game.switch_player()
        self.assertEqual(new_game.player, "O")
        new_game.switch_player()
        self.assertEqual(new_game.player, "X")

    def test_update(self):
        self.game = TicTacGame()
        self.game.update("1", "1")
        self.assertListEqual(
            self.game.board,
            [[" ", " ", " "], [" ", "X", " "], [" ", " ", " "]],
        )
        self.assertEqual(self.game.player, "X")
        self.game.switch_player()
        self.game.update("0", "0")
        self.assertListEqual(
            self.game.board,
            [["O", " ", " "], [" ", "X", " "], [" ", " ", " "]],
        )
        self.assertEqual(self.game.player, "O")

    def test_victory(self):
        self.game = TicTacGame()
        self.assertEqual(self.game.is_victory(), False)
        for row in range(3):
            self.game = TicTacGame()
            for col in range(3):
                self.game.update(str(row), str(col))
            self.assertEqual(self.game.is_victory(), True)
            self.assertEqual(self.game.is_draw(), False)

        for col in range(3):
            self.game = TicTacGame()
            for row in range(3):
                self.game.update(str(row), str(col))
            self.assertEqual(self.game.is_victory(), True)
            self.assertEqual(self.game.is_draw(), False)

        self.game = TicTacGame()
        self.game.update("0", "0")
        self.game.update("1", "1")
        self.game.update("2", "2")
        self.assertEqual(self.game.is_victory(), True)
        self.assertEqual(self.game.is_draw(), False)

        self.game = TicTacGame()
        self.game.update("0", "2")
        self.game.update("1", "1")
        self.game.update("2", "0")
        self.assertEqual(self.game.is_victory(), True)
        self.assertEqual(self.game.is_draw(), False)

    def test_draw(self):
        self.game = TicTacGame()
        self.game.update("0", "0")  # 1
        self.game.switch_player()
        self.game.update("0", "1")  # 2
        self.game.switch_player()
        self.game.update("0", "2")  # 3
        self.game.switch_player()
        self.game.update("1", "0")  # 4
        self.game.switch_player()
        self.game.update("1", "1")  # 5
        self.game.switch_player()
        self.game.update("1", "2")  # 6
        self.game.switch_player()
        self.game.update("2", "1")  # 7
        self.game.switch_player()
        self.game.update("2", "0")  # 8
        self.game.switch_player()
        self.game.update("2", "2")  # 9
        self.assertEqual(self.game.is_draw(), True)

    # TODO
    def test_input(self):
        stdin = sys.stdin
        sys.stdin = open("input.txt", "r")
        stdout = sys.stdout
        sys.stdout = open("output.txt", "w")

        self.game = TicTacGame()
        self.assertEqual(self.game.update(*self.game.input()), True)
        for _ in range(7):
            self.assertEqual(self.game.update(*self.game.input()), False)
        self.assertEqual(self.game.update(*self.game.input()), True)

        sys.stdin.close()
        sys.stdin = stdin
        sys.stdout.close()
        sys.stdout = stdout

        with open("output.txt", "r") as output:
            self.assertEqual(correct_output, output.read())


if __name__ == "__main__":
    unittest.main()
