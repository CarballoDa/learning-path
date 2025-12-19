# ===============
# Modules and functions importations
# ===============


from numbers_processor import sum_nums_v2 as sum_nums


# ===============
# Main functions
# ===============


def validate_data_is_num(data) -> None:
    """ Valida que el texto contenga mínimo 8 dígitos. En caso contrario gestiona las excepciones oportunas.

        Args:
            data (str): Texto para validar

        Returns:
            None
            
        Examples:

    """
    if not data:
        raise ValueError("Error: no se ingresó ningún valor.")
    if len(data) != 8:
        raise ValueError("Error: el parámetro es demasiado corto.")
    if not data.isdigit():
        raise ValueError("Error: el parámetro debe contener solo dígitos. Se admiten espacios.")

def remove_spaces(text: str) -> str:
    """Recibe un texto y devuelve el texto eliminando todos los espacios, tabulaciones o saltos de linea

        Args:
            text (str): Texto para limpiar espacios

        Returns:
            str: Texto sin espacios
            
        Examples:
            >>> remove_spaces("Hola que tal")
            'Holaquetal'
            >>> remove_spaces("4 56 236     ")
            '456236'
            >>> remove_spaces("Hola\nmundo")
            'Holamundo'
    """
    return "".join(text.split())


def get_digit_of_life(number: str) -> int:
    """Recibe un texto que contiene una fecha de nacimiento en formato AAAA MM DD 
        y devuelve el valor entero resultante de sumar todos los digitos.

        Args:
            number (str): Texto con fecha de nacimiento

        Returns:
            int: Devuelve el dígito resultante de sumar repetidamente los dígitos hasta obtener un único número
            
        Examples:
            >>> get_digit_of_life("1984 06 10")
            2
            >>> get_digit_of_life("1984 03 24")
            4
    """
    number = remove_spaces(number)
    validate_data_is_num(number)
    while len(number) > 1:
        number = str(sum_nums(number))
    return int(number)


# ====================================
# Rapid, direct execution tests
# ====================================


def main():
    """Inicia un bucle interactivo para solicitar la fecha de cumpleaños al usuario
    y mostrar la suma de sus dígitos. 
    Se realizan validaciones sobre los datos introducidos.
    Se cierra ingresando 'exit' en lugar de una secuencia numérica.
    """
    while True: 
        numbers = input('Ingresa la fecha de tu cumpleaños en formato AÑO MES DIA: ').strip()
        if numbers.lower() == 'exit':
            break
        print(f"Digito de la vida de {numbers} = {get_digit_of_life(numbers)}")
        
    print('Ejecución cerrada con comando exit')
    

# ============================
# Direct execution block
# ============================


if __name__ == "__main__":
    main()
