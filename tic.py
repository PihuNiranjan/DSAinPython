# Tic Tac Toe game in Python

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check for a tie
def check_tie(board):
    return all([cell != " " for row in board for cell in row])

# Function to get the player's move
def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move // 3][move % 3] == " ":
                return move // 3, move % 3
            else:
                print("This cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Enter a number between 1 and 9.")

# Main function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
