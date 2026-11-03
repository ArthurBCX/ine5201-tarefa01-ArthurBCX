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


def check_game_state(board):
    """Return the winning player, 'draw' if the board is full, or None."""
    directions = ((0, 1), (1, 0), (1, 1), (1, -1))

    for row_index, row in enumerate(board):
        for column_index, player in enumerate(row):
            if player == 0:
                continue

            for row_step, column_step in directions:
                if all(
                    0 <= row_index + step * row_step < len(board)
                    and 0 <= column_index + step * column_step < len(board[row_index + step * row_step])
                    and board[row_index + step * row_step][column_index + step * column_step] == player
                    for step in range(1, 4)
                ):
                    return player

    if all(cell != 0 for row in board for cell in row):
        return "draw"

    return None
