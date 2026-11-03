ROWS = 6
COLUMNS = 7

board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]


def print_board(board):
    """Print the board as a grid in the terminal."""
    print("  " + "   ".join(str(column) for column in range(1, COLUMNS + 1)))
    for row in board:
        print("| " + " | ".join(str(cell) for cell in row) + " |")
