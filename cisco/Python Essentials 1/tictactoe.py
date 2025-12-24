from random import randrange

HORIZONTAL_DIVIDER = "+-------+-------+-------+"
VERTICAL_DIVIDER = "|"
USER_PIECE = "O"
MACHINE_PIECE = "X"
BOARD_POS_LOCATIONS = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}

def print_horizontal_divider():
    """Prints a horizontal line that separates the rows of the board."""
    print(HORIZONTAL_DIVIDER)
    
def print_vertical_divider():
    """Prints a vertical line that separates the columns of the board."""
    print("{0}       {0}       {0}       {0}".format(VERTICAL_DIVIDER))
    
def print_cells_in_row(cells):
    """Prints a horizontal row of the board with the pieces in their respective positions.
    
    Args:
        cells (list): The pieces located in the row's cells.
    Returns:
        None
    """
    print("{0}   {1}   {0}   {2}   {0}   {3}   {0}".format(VERTICAL_DIVIDER, cells[0], cells[1], cells[2]))
    
def print_row(cells, top=False, bottom=False):
    """Prints a row of the board, including horizontal dividers if required.
    
    Args:
        cells (list): The pieces located in the row's cells.
        top (bool): Indicates whether a horizontal divider should be printed at the top.
        bottom (bool): Indicates whether a horizontal divider should be printed at the bottom.
    Returns:
        None    
    """
    if top:
        print_horizontal_divider()
    print_vertical_divider()
    print_cells_in_row(cells)
    print_vertical_divider()
    if bottom:
        print_horizontal_divider()

def display_board(board):
    """Prints the complete Tic Tac Toe board.
    
    Args:
        board (list): The current state of the Tic Tac Toe board.
    Returns:
        None
    """
    print_row(board[0], top=True, bottom=False)
    print_row(board[1], top=True, bottom=True)
    print_row(board[2], top=False, bottom=True)
    
def check_movement(movement, board):
    """Checks whether the move entered by the user is valid.
    
    Args:
        movement (int): The move entered by the user.
        board (list): The current state of the Tic Tac Toe board.
    Returns:
        bool: True if the move is valid, False otherwise.
    """
    available_cells = make_list_of_free_fields(board)
    if BOARD_POS_LOCATIONS[movement] in available_cells:
        return True
    return False

def make_movement(movement, board, sign):
    """Executes a move on the board.
    
    Args:
        movement (int): The move entered by the user.
        board (list): The current state of the Tic Tac Toe board.
        sign (str): The player's piece ('X' or 'O').
    Returns:
        list: The updated board after the move.
    """
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if BOARD_POS_LOCATIONS[movement] == (row_index, cell_index):
                board[row_index][cell_index] = sign
                return board

def enter_move(board):
    """Prompts the user to enter a move and updates the board accordingly.
    
    Args:
        board (list): The current state of the Tic Tac Toe board.
    Returns:
        list: The updated board after the user's move.
    """
    try:
        movement = int(input("Ingresa tu movimiento: "))
        if movement < 1 or movement > 9:
            print("Por favor ingresa un número entero entre 1 y 9.")
            return enter_move(board)
    except TypeError:
        print("Por favor ingresa un número entero entre 1 y 9.")
        return enter_move(board)
    except ValueError:
        print("Por favor ingresa un número entero entre 1 y 9.")
        return enter_move(board)
    
    if not check_movement(movement, board):
        print("Movimiento inválido. La celda ya está ocupada.")
        return enter_move(board)
    
    return make_movement(movement, board, USER_PIECE)
    
def make_list_of_free_fields(board):
    """Creates a list of all free cells on the board.
    
    Args:
        board (list): The current state of the Tic Tac Toe board.
    Returns:
        list: A list of tuples representing the positions (row, column) of free cells.
    """
    free_cells = []
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell != 'X' and cell != 'O':
                free_cells.append((row_index, cell_index))
    return free_cells

def victory_for(board, sign):
    """Determines whether the player using the specified piece has won the game.
    
    Args:
        board (list): The current state of the Tic Tac Toe board.
        sign (str): The player's piece ('X' or 'O').
    Returns:
        bool: True if the player has won, False otherwise.
    """
    indexes_with_sign = []
    sign_by_index = ''
    for row_index, row in enumerate(board):
        if len(set(row)) == 1 and row[0] == sign:
            return True
        else:
            for cell_index, cell in enumerate(row):
                if cell == sign:
                    indexes_with_sign.append(cell_index + 1)
                    sign_by_index = sign         
    
    if len(indexes_with_sign) == 3 and len(set(indexes_with_sign)) == 1 and sign_by_index == sign:
        return True
    return False

def draw_move(board):
    """Executes the machine's move and updates the board based on its decision.
    
    Args:
        board (list): The current state of the Tic Tac Toe board.
    Returns:
        list: The updated board after the machine's move.
    """
    movement = randrange(1, 10)
    if not check_movement(movement, board):        
        return draw_move(board)
        
    print("Mi movimiento: {}".format(movement))
    return make_movement(movement, board, MACHINE_PIECE)


# ====================================
# Quick tests for direct execution
# ====================================
def main():
    """
    Main Tic Tac Toe game
    Game initialized with the machine making the first move in the center position (5)
    """
    game = [ [str(3 * j + i + 1) for i in range(3)] for j in range(3) ]
    game[1][1] = 'X'
    winer = None
    print("Tic Tac Toe - Nuevo Juego")
    display_board(game)
    while len(make_list_of_free_fields(game)) > 0 and winer is None:
        game = enter_move(game)
        display_board(game)
        if victory_for(game, USER_PIECE):
            winer = USER_PIECE
        game = draw_move(game)
        display_board(game)
        if victory_for(game, MACHINE_PIECE):
            winer = MACHINE_PIECE

    if winer == USER_PIECE:
        print("¡Has ganado!")
    elif winer == MACHINE_PIECE:
        print("¡He ganado!")
    else:
        print("¡Empate!")
    
# ============================
# Direct execution block
# ============================
if __name__ == "__main__":
    main()