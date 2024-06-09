class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print("|".join([cell if cell != '' else ' ' for cell in row]))
            print("-" * 5)
    
    def is_full(self):
        for row in self.board:
            if '' in row:
                return False
        return True
    
    def winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != '':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != '':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
            return self.board[0][2]
        return None
    
    def available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    moves.append((i, j))
        return moves

    def make_move(self, row, col, player):
        if self.board[row][col] == '':
            self.board[row][col] = player
            return True
        return False

    def undo_move(self, row, col):
        self.board[row][col] = ''

def minimax(game, depth, is_maximizing):
    winner = game.winner()
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif game.is_full():
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for move in game.available_moves():
            game.make_move(move[0], move[1], 'X')
            score = minimax(game, depth + 1, False)
            game.undo_move(move[0], move[1])
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in game.available_moves():
            game.make_move(move[0], move[1], 'O')
            score = minimax(game, depth + 1, True)
            game.undo_move(move[0], move[1])
            best_score = min(score, best_score)
        return best_score

def best_move(game):
    best_score = -float('inf')
    move = None
    for m in game.available_moves():
        game.make_move(m[0], m[1], 'X')
        score = minimax(game, 0, False)
        game.undo_move(m[0], m[1])
        if score > best_score:
            best_score = score
            move = m
    return move

def play_game():
    game = TicTacToe()
    current_player = 'X'
    
    while not game.is_full() and game.winner() is None:
        game.print_board()
        if current_player == 'X':
            row, col = best_move(game)
        else:
            print(f"Player {current_player}'s turn.")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        
        if game.make_move(row, col, current_player):
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print("Invalid move. Try again.")
    
    game.print_board()
    winner = game.winner()
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

play_game()