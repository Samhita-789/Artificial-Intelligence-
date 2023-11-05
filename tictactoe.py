import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def computer_move(board):
    # Magic square positions
    magic_square = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

    # Try to find the best move using the magic square
    best_move = None
    best_score = -1

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                score = magic_square[row][col]
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    print("Welcome to Tic Tac Toe against the computer!")

    while True:
        print_board(board)

        if player == 'X':
            row = int(input(f"Player {player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, 2): "))
        else:
            print("Computer is thinking...")
            row, col = computer_move(board)

        if board[row][col] == ' ':
            board[row][col] = player

            if is_winner(board, player):
                print_board(board)
                if player == 'X':
                    print(f"Player {player} wins! Congratulations!")
                else:
                    print("Computer wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                player = 'O' if player == 'X' else 'X'
        else:
            print("That position is already occupied. Try again.")

if __name__ == "__main__":
    main()
