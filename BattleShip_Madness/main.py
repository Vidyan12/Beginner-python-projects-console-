import random


def print_board(board):
    """
    Print the game board.
    """
    for row in board:
        print(" ".join(row))


def random_row(board):
    """
    Generate a random row index for placing a ship.
    """
    return random.randint(0, len(board) - 1)


def random_col(board):
    """
    Generate a random column index for placing a ship.
    """
    return random.randint(0, len(board[0]) - 1)


def place_ship(board):
    """
    Place a battleship on the board.
    """
    ship_row = random_row(board)
    ship_col = random_col(board)
    return ship_row, ship_col


def player_guess():
    """
    Get player's guess for the row and column.
    """
    guess_row = int(input("Guess Row (1-5): ")) - 1
    guess_col = int(input("Guess Col (1-5): ")) - 1
    return guess_row, guess_col


def update_board(board, row, col, symbol):
    """
    Update the game board with the result of a player's guess.
    """
    board[row][col] = symbol


def play_battleship():
    """
    Main function to run the Battleship game.
    """
    print("Welcome to Battleship Game!")
    print("Try to sink the hidden battleship on the board.")
    print("You have 6 turns to find it. Good luck!\n")

    while True:
        # Set up the game board
        board = [["O"] * 5 for _ in range(5)]

        # Place the battleship
        ship_row, ship_col = place_ship(board)

        for turn in range(6):
            print(f"\nTurn {turn + 1}")

            # Get player's guess
            guess_row, guess_col = player_guess()

            # Check the guess
            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sunk my battleship!")
                break
            else:
                if 0 <= guess_row < 5 and 0 <= guess_col < 5:
                    if board[guess_row][guess_col] == "X":
                        print("You bombed that place already.")
                    else:
                        print("You missed my battleship!")
                        update_board(board, guess_row, guess_col, "X")
                else:
                    print("Oops, that's not even in the ocean.")

            # Print the updated board
            print_board(board)

            # Check if it's the last turn
            if turn == 6:
                print("\nGame Over! The battleship was located at:")
                print(f"Row: {ship_row + 1}, Col: {ship_col + 1}")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing Battleship! Goodbye!")
            break


if __name__ == "__main__":
    play_battleship()
