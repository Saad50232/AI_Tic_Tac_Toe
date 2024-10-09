import random

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the game is a draw
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to get all available moves on the board
def get_available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

# AI move function to make moves for 'O'
def ai_move(board):
    # Try to find a winning move
    for move in get_available_moves(board):
        row, col = move
        board[row][col] = "O"
        if check_winner(board, "O"):
            return
        board[row][col] = " "  # Undo move

    # Try to block the player 'X'
    for move in get_available_moves(board):
        row, col = move
        board[row][col] = "X"
        if check_winner(board, "X"):
            board[row][col] = "O"
            return
        board[row][col] = " "  # Undo move

    # If no winning or blocking move, pick a random move
    row, col = random.choice(get_available_moves(board))
    board[row][col] = "O"

# Main function to play Tic-Tac-Toe
def play_tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Human player starts first

    while True:
        print_board(board)

        if current_player == "X":
            # Get human player input
            row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter col (0, 1, 2): "))

            # Check for valid move
            if board[row][col] == " ":
                board[row][col] = current_player
            else:
                print("Cell already occupied! Try again.")
                continue
        else:
            # AI plays
            print("AI is making a move...")
            ai_move(board)

        # Check for win or draw
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_tic_tac_toe()
