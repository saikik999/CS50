import random
import numpy as np

class MinesweeperBoard:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = np.zeros((height, width), dtype=int)
        self.visible_board = np.full((height, width), -1, dtype=int)  # -1 means unrevealed

        self._place_mines()
        self._calculate_adjacent_mines()

    def _place_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            row = random.randint(0, self.height - 1)
            col = random.randint(0, self.width - 1)
            if self.board[row][col] != -1:  # -1 represents a mine
                self.board[row][col] = -1
                mines_placed += 1

    def _calculate_adjacent_mines(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == -1:
                    continue
                self.board[row][col] = self._count_adjacent_mines(row, col)

    def _count_adjacent_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(self.height, row + 2)):
            for c in range(max(0, col - 1), min(self.width, col + 2)):
                if self.board[r][c] == -1:
                    count += 1
        return count

    def reveal(self, row, col):
        if self.visible_board[row][col] != -1:
            return  # already revealed
        if self.board[row][col] == -1:
            return -1  # hit a mine
        self.visible_board[row][col] = self.board[row][col]
        if self.board[row][col] == 0:
            for r in range(max(0, row - 1), min(self.height, row + 2)):
                for c in range(max(0, col - 1), min(self.width, col + 2)):
                    if self.visible_board[r][c] == -1:
                        self.reveal(r, c)

    def is_won(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.visible_board[row][col] == -1 and self.board[row][col] != -1:
                    return False
        return True

    def print_visible_board(self):
        for row in range(self.height):
            print(" ".join(str(self.visible_board[row][col]) if self.visible_board[row][col] != -1 else "?" for col in range(self.width)))
        print()

class MinesweeperAI:
    def __init__(self, board):
        self.board = board

    def play(self):
        while not self.board.is_won():
            self.board.print_visible_board()
            move = self._find_move()
            if move:
                row, col = move
                if self.board.reveal(row, col) == -1:
                    print(f"Hit a mine at ({row}, {col})! Game over.")
                    self.board.print_visible_board()
                    return
            else:
                print("No safe moves found. Game over.")
                self.board.print_visible_board()
                return
        print("You won!")

    def _find_move(self):
        for row in range(self.board.height):
            for col in range(self.board.width):
                if self.board.visible_board[row][col] == -1:
                    return row, col
        return None

width, height, num_mines = 10, 10, 10
board = MinesweeperBoard(width, height, num_mines)
ai = MinesweeperAI(board)
ai.play()
