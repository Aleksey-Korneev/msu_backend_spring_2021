"""TicTacGame class is defined in this module."""

import os

# import sys


class TicTacGame:
    """
    Tic-tac-toe console game.
    """

    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [[" "] * board_size for _ in range(board_size)]
        self.player = "X"

    def show_board(self):
        print("-" * (self.board_size * 2 + 1))
        for row in self.board:
            print("", *row, sep="|", end="|\n")
            print("-" * (self.board_size * 2 + 1))
        print()

    def input(self):
        print(f"Ход игрока {self.player}.")
        row = input("row = ")
        col = input("col = ")
        os.system("clear")
        return (row, col)

    def validate_input(self, row, col):
        self.switch = True
        if not (row.isdigit() and col.isdigit()):
            print("Некорректный ввод.")
            self.switch = False
            return False

        row = int(row)
        col = int(col)

        bs = self.board_size
        if row < 0 or row >= bs or col < 0 or col >= bs:
            print("Недопустимые координаты.")
            self.switch = False
            return False
        if self.board[row][col] != " ":
            print("Эта клетка уже занята.")
            self.switch = False
            return False

        return row, col

    def update(self, row, col):
        res = self.validate_input(row, col)
        if not res:
            return False
        self.board[res[0]][res[1]] = self.player
        return True

    def switch_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def is_victory(self):
        # TODO: переписать для поля произвольного размера
        # Текущая реализация функции рассчитана на поле 3x3
        win = [self.player] * self.board_size
        for line in self.board:
            if line == win:
                return True

        for line in map(list, zip(*self.board)):
            if line == win:
                return True

        if [self.board[i][i] for i in range(self.board_size)] == win:
            return True

        if [
            self.board[i][self.board_size - 1 - i]
            for i in range(self.board_size)
        ] == win:
            return True

        return False

    def is_draw(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def start_game(self, board_size=3):
        os.system("clear")

        while True:
            self.show_board()

            if self.update(*self.input()):
                if self.is_victory():
                    self.show_board()
                    print(f"Игрок {self.player} победил!")
                    break
                if self.is_draw():
                    self.show_board()
                    print("Ничья!")
                    break

                if self.switch:
                    self.switch_player()


if __name__ == "__main__":
    # board_size = 3 if len(sys.argv) == 1 else max(3, int(sys.argv[1]))
    board_size = 3
    game = TicTacGame(board_size)
    game.start_game()
