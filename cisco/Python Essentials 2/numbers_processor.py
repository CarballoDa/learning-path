# ===============
# Main functions
# ===============

def sum_nums(numbers: str) -> int:
    """Recibe una secuencia de numeros y devuelve la suma de ellos

    Args:
        numbers (str): Secuencia numérica recibida

    Returns:
        int: Suma de la secuencia numérica recibida usando un bucle y una variable de acumulación
        
    Examples:
        >>> sum_nums("123")
        6
        >>> sum_nums("444")
        12
    """
    total = 0
    for digit in numbers:
        total += int(digit)
    return total

def sum_nums_v2(numbers: str) -> int:
    """Recibe una secuencia de numeros y devuelve la suma de ellos

    Args:
        numbers (str): Secuencia numérica recibida

    Returns:
        int: Suma de la secuencia numérica recibida usando un bucle y la funcion sum()
        
    Examples:
        >>> sum_nums_v2("123")
        6
        >>> sum_nums_v2("444")
        12
    """
    return sum(int(n) for n in numbers)

def start_request():
    """Inicia un bucle interactivo para solicitar secuencias numéricas al usuario
    y mostrar la suma de sus dígitos. Se cierra ingresando 'exit' en lugar de una secuencia numérica.
    """
    while True: 
        numbers = input('Ingresa una secuencia de números mayores o iguales a 1 que serán sumados: ').strip()
        if numbers.lower() == 'exit':
            break
        if not numbers:
            print("Error: no se ingresó ningún número.")
            continue    
        if not numbers.isnumeric():
            print("Error: la secuencia ha de contener solo números.")
            continue
        
        print(f"Suma de secuencia {numbers} = {sum_nums(numbers)}")
        
    print('Ejecución cerrada con comando exit')

# ====================================
# Rapid, direct execution tests
# ====================================

def main():
    """Ejecuta pruebas rápidas de validación."""
    print("Tests sum_nums:")
    assert sum_nums("56789103") == 39
    assert sum_nums("444") == 12
    assert sum_nums("123") == 6
    print("✔ sum_nums OK")

    print("Tests sum_nums_v2:")
    assert sum_nums_v2("56789103") == 39
    assert sum_nums_v2("444") == 12
    assert sum_nums_v2("123") == 6
    print("✔ sum_nums_v2 OK")


# ============================
# Direct execution block
# ============================
if __name__ == "__main__":
    main()
    start_request()
    