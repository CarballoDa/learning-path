# ===============
# Main functions
# ===============

def find_word(find: str, source: str) -> bool:
    """Recibe un texto a buscar y otro donde buscar. Busca que los caracteres de find estén entre los caracteres de source.

    Args:
        find (str): texto a buscar
        source (str): texto donde buscar

    Returns:
        bool: True si los caracteres de find están en source. False en caso contrario
        
    Examples:
        >>> find_word("Tesla", "Ten animals I slam in a net")
        True
        >>> find_word("120", "123567890")
        True
        >>> find_word("Men", "El sol si que luce")
        False
    """
    find = find.lower()
    source = source.lower()

    pos = 0
    for char in find:
        pos = source.find(char, pos)
        if pos == -1:
            return False
        pos += 1

    return True


# ====================================
# Rapid, direct execution tests
# ====================================

def main():
    """Ejecuta pruebas rápidas de validación."""
    while True: 
        find = input('Ingresa la cadena que se de ha de buscar: ').strip()
        if find.lower() == 'exit':
            break
        if len(find) == 0:
            print("Error: la cadena a buscar no puede estar vacía.")
            continue
        source = input('Ingresa la cadena donde se ha de buscar: ').strip()
        if len(source) == 0:
            print("Error: la cadena donde buscar no puede estar vacía.")
            continue
        if len(source) < len(find):
            print("Error: la cadena a buscar no puede ser mayor que la cadena donde buscar.")
            continue
        
        print(f"¿Está {find} en {source}?... {find_word(find, source)}")
        
    print('Ejecución cerrada con comando exit')
    
# ============================
# Direct execution block
# ============================

if __name__ == '__main__':
    main()