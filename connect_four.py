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


def run_gui():
    """Run the Connect Four game with a FreeSimpleGUI interface."""
    try:
        import FreeSimpleGUI as sg
    except ImportError as error:
        raise RuntimeError(
            "FreeSimpleGUI is required to run the graphical game. "
            "Install it with: pip install FreeSimpleGUI"
        ) from error

    game_board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
    layout = [
        [sg.Text("Player 1's turn", key="status", justification="center", expand_x=True)],
        [
            sg.Button(
                str(column),
                key=f"column_{column}",
                size=(4, 1),
            )
            for column in range(1, COLUMNS + 1)
        ],
    ]
    for row_index in range(ROWS):
        layout.append(
            [
                sg.Button(
                    "●",
                    key=f"cell_{row_index}_{column_index}",
                    size=(4, 2),
                    button_color=("#B0BEC5", "#1565C0"),
                    disabled=True,
                )
                for column_index in range(COLUMNS)
            ]
        )

    window = sg.Window("Connect Four", layout, finalize=True)
    current_player = 1

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED:
            break

        column = int(event.removeprefix("column_"))
        if not make_move(game_board, column, current_player):
            window["status"].update(f"Column {column} is full. Choose another.")
            window[event].update(disabled=True)
            continue

        row_index = next(
            row_index
            for row_index, row in enumerate(game_board)
            if row[column - 1] != 0
        )
        piece_color = "#E53935" if current_player == 1 else "#FDD835"
        window[f"cell_{row_index}_{column - 1}"].update(
            button_color=("#FFFFFF", piece_color)
        )

        if game_board[0][column - 1] != 0:
            window[event].update(disabled=True)

        game_state = check_game_state(game_board)
        if game_state == "draw":
            window["status"].update("It's a draw!")
        elif game_state in (1, 2):
            window["status"].update(f"Player {game_state} wins!")
        else:
            current_player = 3 - current_player
            window["status"].update(f"Player {current_player}'s turn")
            continue

        for next_column in range(1, COLUMNS + 1):
            window[f"column_{next_column}"].update(disabled=True)

    window.close()


if __name__ == "__main__":
    run_gui()
