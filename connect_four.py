ROWS = 6
COLUMNS = 7

board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]


def print_board(board):
    """Print the board as a grid in the terminal."""
    print("  " + "   ".join(str(column) for column in range(1, COLUMNS + 1)))
    for row in board:
        print("| " + " | ".join(str(cell) for cell in row) + " |")


def make_move(board, column, player):
    """Place a player's piece in a 1-based column; return False if it is full."""
    if not isinstance(column, int) or not 1 <= column <= COLUMNS:
        raise ValueError(f"Column must be an integer between 1 and {COLUMNS}.")
    if player not in (1, 2):
        raise ValueError("Player must be 1 or 2.")

    column -= 1
    for row in reversed(board):
        if row[column] == 0:
            row[column] = player
            return True

    return False
