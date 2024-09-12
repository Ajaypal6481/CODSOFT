import math

def minimax(game, depth, is_maximizing, alpha, beta):
    winner = game.check_winner()
    if winner == 1:  # AI wins
        return 1
    elif winner == 2:  # Human wins
        return -1
    elif winner == 0:  # Draw
        return 0

    if is_maximizing:  # AI's turn
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if game.board[i][j] == 0:  # Empty cell
                    game.board[i][j] = 1  # AI's move
                    score = minimax(game, depth + 1, False, alpha, beta)
                    game.board[i][j] = 0  # Undo move
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:  # Human's turn
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if game.board[i][j] == 0:  # Empty cell
                    game.board[i][j] = 2  # Human's move
                    score = minimax(game, depth + 1, True, alpha, beta)
                    game.board[i][j] = 0  # Undo move
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score
