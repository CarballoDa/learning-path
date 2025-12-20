# ===============
# Main functions
# ===============

def is_palindrome(text: str) -> bool:
    """Recibe un texto y comprueba si es un palíndromo

    Args:
        text (str): texto a comprobar, se trata todo como minusculas y se obvian los espacios

    Returns:
        bool: True si es un palindromo. False en caso contrario
        
    Examples:
        >>> is_palindrome("Ten animals I slam in a net")
        True
        >>> is_palindrome("1221")
        True
        >>> is_palindrome("El sol si que luce")
        False
        >>> is_palindrome("")
        False
    """
    if len(text) == 0:
        return False
    return text.lower().replace(" ", "") == text.lower().replace(" ", "")[::-1]


# ====================================
# Rapid, direct execution tests
# ====================================

def main():
    """Ejecuta pruebas rápidas de validación."""
    while True: 
        txt = input('Ingresa un texto a ver si es un palindromo: ')
        if txt.lower() == 'exit':
            break

        print(f"¿El texto {txt} es palindromo? -> {is_palindrome(txt)}")
        
    print('Ejecución cerrada con comando exit')
    
# ============================
# Direct execution block
# ============================

if __name__ == '__main__':
    main()