class Game:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]

        # Check if the game is a draw
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return 0

        return -1  # Game is not over

    def print_board(self):
        print(" " + " | ".join(str(cell) for cell in self.board[0]))
        print("---+---+---")
        print(" " + " | ".join(str(cell) for cell in self.board[1]))
        print("---+---+---")
        print(" " + " | ".join(str(cell) for cell in self.board[2]))
