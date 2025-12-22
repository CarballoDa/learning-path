# ===============
# Constants vars
# ===============


VALIDATOR = set(range(1, 10))


BOARD_SIZE = 9


SUDOKU_RIGHT_BOARD = [
                [2, 9, 5, 7, 4, 3, 8, 6, 1],
                [4, 3, 1, 8, 6, 5, 9, 2, 7],
                [8, 7, 6, 1, 9, 2, 5, 4, 3],
                [3, 8, 7, 4, 5, 9, 2, 1, 6],
                [6, 1, 2, 3, 8, 7, 4, 9, 5],
                [5, 4, 9, 2, 1, 6, 7, 3, 8],
                [7, 6, 3, 5, 2, 4, 1, 8, 9],
                [9, 2, 8, 6, 7, 1, 3, 5, 4],
                [1, 5, 4, 9, 3, 8, 6, 7, 2]
            ]

    
SUDOKU_WRONG_BOARD = [
            [1, 9, 5, 7, 4, 3, 8, 6, 2],
            [4, 3, 1, 8, 6, 5, 9, 2, 7],
            [8, 7, 6, 1, 9, 2, 5, 4, 3],
            [3, 8, 7, 4, 5, 9, 2, 1, 6],
            [6, 1, 2, 3, 8, 7, 4, 9, 5],
            [5, 4, 9, 2, 1, 6, 7, 3, 8],
            [7, 6, 3, 5, 2, 4, 1, 8, 9],
            [9, 2, 8, 6, 7, 1, 3, 5, 4],
            [2, 5, 4, 9, 3, 8, 6, 7, 1]
        ]


# ===============
# Main functions
# ===============


def validate_rows(sudoku: list) -> bool:
    """
    Valida que cada fila del tablero contenga los números del 1 al 9.

    Args:
        sudoku (list): lista con la configuración del tablero de sudoku

    Returns:
        bool: True si es un tablero válido. False en caso contrario
        
    Examples:
        >>> validate_rows(SUDOKU_RIGHT_BOARD)
        True
        >>> validate_rows(SUDOKU_WRONG_BOARD)
        False
    """
    for row in sudoku:
        if VALIDATOR != set(row):
            return False
    return True


def validate_columns(sudoku: list) -> bool:
    """
    Valida que cada columna del tablero contenga los números del 1 al 9.

    Args:
        sudoku (list): lista con la configuración del tablero de sudoku

    Returns:
        bool: True si es un tablero válido. False en caso contrario
        
    Examples:
        >>> validate_columns(SUDOKU_RIGHT_BOARD)
        True
        >>> validate_columns(SUDOKU_WRONG_BOARD)
        False
    """
    for column_index in range(BOARD_SIZE):
        column = [row[column_index] for row in sudoku] 
        if set(column) != VALIDATOR:
            return False
    return True


def validate_quadrants(sudoku: list) -> bool:
    """
    Valida que cada cuadrante 3x3 contenga los números del 1 al 9.

    Args:
        sudoku (list): lista con la configuración del tablero de sudoku

    Returns:
        bool: True si es un tablero válido. False en caso contrario
        
    Examples:
        >>> validate_quadrants(SUDOKU_RIGHT_BOARD)
        True
        >>> validate_quadrants(SUDOKU_WRONG_BOARD)
        False
    """
    for row_start in (0, 3, 6):
        for col_start in (0, 3, 6):
            quadrant = []
            for row_index in range(row_start, row_start + 3):
                quadrant.extend(sudoku[row_index][col_start:col_start + 3])
            if set(quadrant) != VALIDATOR:
                return False     
    return True


def validate_sudoku(sudoku: list) -> bool:
    """
    Valida un tablero de sudoku comprobando filas, columnas y cuadrantes.

    Args:
        sudoku (list): lista con la configuración del tablero de sudoku

    Returns:
        bool: True si es un tablero válido. False en caso contrario
        
    Examples:
        >>> validate_sudoku(SUDOKU_RIGHT_BOARD)
        True
        >>> validate_sudoku(SUDOKU_WRONG_BOARD)
        False
    """
    
    return validate_rows(sudoku) and validate_columns(sudoku) and validate_quadrants(sudoku)


# ====================================
# Rapid, direct execution tests
# ====================================

def main():
    """Ejecuta pruebas rápidas de validación, complementarias a doctests."""
    
    print(f"Tablero 1 - ¿válido?: {validate_sudoku(SUDOKU_RIGHT_BOARD)}")
    print(f"Tablero 2 - ¿válido?: {validate_sudoku(SUDOKU_WRONG_BOARD)}")
    
    assert validate_sudoku(SUDOKU_RIGHT_BOARD) is True, "Debería devolver True"
    assert validate_sudoku(SUDOKU_WRONG_BOARD) is False, "Debería devolver False"

    print("Pruebas completadas correctamente.")

    
# ============================
# Direct execution block
# ============================

if __name__ == '__main__':
    main()