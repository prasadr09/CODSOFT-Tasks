import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Tic Tac Toe - Unbeatable AI")

# Initialize variables
current_player = "X"
board = [""] * 9  # Empty board

# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
            return board[combo[0]]
    if "" not in board:
        return "Draw"
    return None

# Minimax algorithm for optimal AI moves
def minimax(board, is_maximizing):
    winner = check_winner()
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

# Find the best move for the AI
def find_best_move():
    best_score = float('-inf')
    best_move = -1
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Function to handle button clicks
def handle_click(index):
    global current_player
    if board[index] == "" and not check_winner():
        board[index] = current_player
        buttons[index].config(text=current_player)
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            if current_player == "O":
                ai_move()

# AI makes its move
def ai_move():
    best_move = find_best_move()
    if best_move != -1:
        board[best_move] = "O"
        buttons[best_move].config(text="O")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        else:
            global current_player
            current_player = "X"

# Reset the game board
def reset_board():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    for button in buttons:
        button.config(text="")

# Create the game grid
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: handle_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Run the application
root.mainloop()
