import game
import minimax

def play_game():
    game_instance = game.Game()
    while True:
        game_instance.print_board()
        print("Enter your move (row and column numbers, 0-2):")
        row = int(input("Row: "))
        col = int(input("Col: "))
        if game_instance.board[row][col] != 0:
            print("Invalid move, try again.")
            continue
        game_instance.board[row][col] = 2  # Human's move

        winner = game_instance.check_winner()
        if winner == 2:
            print("You win!")
            break
        elif winner == 0:
            print("It's a draw!")
            break

        # AI's turn
        best_score = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if game_instance.board[i][j] == 0:  # Empty cell
