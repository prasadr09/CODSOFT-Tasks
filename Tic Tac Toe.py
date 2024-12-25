import random

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '


# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)


# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


# Function to check if the board is full (draw condition)
def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)


# Minimax Algorithm
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, PLAYER_X):
        return 1
    if check_win(board, PLAYER_O):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


# Function to find the best move for the AI
def best_move(board):
    best_val = float('-inf')
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)

    return move


# Function to play the Tic-Tac-Toe game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human move (Player O)
        print("\nYour move (Player O):")
        row, col = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())

        if board[row][col] == EMPTY:
            board[row][col] = PLAYER_O
        else:
            print("Invalid move! Try again.")
            continue

        print_board(board)

        # Check if human wins
        if check_win(board, PLAYER_O):
            print("Congratulations! You won!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        # AI move (Player X)
        print("\nAI's move (Player X):")
        row, col = best_move(board)
        board[row][col] = PLAYER_X
        print(f"AI chooses: {row} {col}")

        print_board(board)

        # Check if AI wins
        if check_win(board, PLAYER_X):
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break


# Run the game
play_game()
