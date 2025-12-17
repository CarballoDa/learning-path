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
    """Imprime una línea horizontal que separa las filas del tablero."""
    print(HORIZONTAL_DIVIDER)
    
def print_vertical_divider():
    """Imprime una línea vertical que separa las columnas del tablero."""
    print("{0}       {0}       {0}       {0}".format(VERTICAL_DIVIDER))
    
def print_cells_in_row(cells):
    """Imprime una fila horizontal del tablero con las piezas en sus respectivas posiciones.
    Args:
        cells (list): Las piezas en las celdas de la fila.
    Returns:
        None
    """
    print("{0}   {1}   {0}   {2}   {0}   {3}   {0}".format(VERTICAL_DIVIDER, cells[0], cells[1], cells[2]))
    
def print_row(cells, top=False, bottom=False):
    """Imprime una fila del tablero, incluyendo los divisores horizontales si es necesario.
    Args:
        cells (list): Las piezas en las celdas de la fila.
        top (bool): Indica si se debe imprimir un divisor horizontal en la parte superior.
        bottom (bool): Indica si se debe imprimir un divisor horizontal en la parte inferior.
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
    """Imprime el tablero completo de Tic Tac Toe.
    Args:
        board (list): El estado actual del tablero de Tic Tac Toe.
    Returns:
        None
    """
    print_row(board[0], top=True, bottom=False)
    print_row(board[1], top=True, bottom=True)
    print_row(board[2], top=False, bottom=True)
    
def check_movement(movement, board):
    """Verifica si el movimiento ingresado por el usuario es válido.
    Args:
        movement (int): El movimiento ingresado por el usuario.
        board (list): El estado actual del tablero de Tic Tac Toe.
    Returns:
        bool: True si el movimiento es válido, False en caso contrario.
    """
    available_cells = make_list_of_free_fields(board)
    if BOARD_POS_LOCATIONS[movement] in available_cells:
        return True
    return False

def make_movement(movement, board, sign):
    """Realiza el movimiento del usuario en el tablero.
    Args:
        movement (int): El movimiento ingresado por el usuario.
        board (list): El estado actual del tablero de Tic Tac Toe.
        sign (str): La pieza del jugador que mueve ('X' o 'O').
    Returns:
        list: El estado actualizado del tablero después del movimiento del usuario.
    """
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if BOARD_POS_LOCATIONS[movement] == (row_index, cell_index):
                board[row_index][cell_index] = sign
                return board

def enter_move(board):
    """Solicita al usuario que ingrese su movimiento y actualiza el tablero en consecuencia.
    Args:
        board (list): El estado actual del tablero de Tic Tac Toe.
    Returns:
        list: El estado actualizado del tablero después del movimiento del usuario.
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
    """Crea una lista de todas las celdas libres en el tablero.
    Args:
        board (list): El estado actual del tablero de Tic Tac Toe.
    Returns:
        list: Una lista de tuplas que representan las posiciones (fila, columna) de las celdas libres.
    """
    free_cells = []
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell != 'X' and cell != 'O':
                free_cells.append((row_index, cell_index))
    return free_cells

def victory_for(board, sign):
    """Determina si el jugador con la pieza especificada ha ganado el juego.
    Args:
        board (list): El estado actual del tablero de Tic Tac Toe.
        sign (str): La pieza del jugador ('X' o 'O').
    Returns:
        bool: True si el jugador ha ganado, False en caso contrario.
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
    """Ejecuta el modivimiento de la máquina y redefine el tablero acorde a su decisión.
    Args:
        board (list): El estado actual del tablero de Tic Tac Toe.
    Returns:
        list: El estado actualizado del tablero después del movimiento de la máquina.
    """
    movement = randrange(1, 10)
    if not check_movement(movement, board):        
        return draw_move(board)
        
    print("Mi movimiento: {}".format(movement))
    return make_movement(movement, board, MACHINE_PIECE)

"""
Juego principal de Tic Tac Toe
game inicial con primer movimiento realizado por la máquina en la posición central (5)
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