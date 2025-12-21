# ===============
# Main functions
# ===============

def are_anagrams(txt_a: str, txt_b: str) -> bool:
    """Recibe dos textos y comprueba si son anagramas

    Args:
        txt_a (str): primer texto a comprobar, se trata todo como minusculas y se obvian los espacios
        txt_b (str): segundo texto a comprobar, se trata todo como minusculas y se obvian los espacios

    Returns:
        bool: True si son anagramas. False en caso contrario
        
    Examples:
        >>> are_anagrams("Ten", "Net")
        True
        >>> are_anagrams("1221", "2121")
        True
        >>> are_anagrams("silent", "liston")
        False
        >>> are_anagrams("", "")
        False
    """
    if len(txt_a) == 0 and len(txt_b) == 0:
        return False
    return sorted(txt_a.lower().replace(" ", "")) == sorted(txt_b.lower().replace(" ", "")) 

# ====================================
# Rapid, direct execution tests
# ====================================

def main():
    """Ejecuta pruebas rápidas de validación."""
    while True: 
        txt_a = input('Ingresa el primer texto posible anagrama: ')
        if txt_a.lower() == 'exit':
            break
        
        txt_b = input('Ingresa el segundo texto posible anagrama: ')

        print(f"Los textos {txt_a} y {txt_b} son anagramas? -> {are_anagrams(txt_a, txt_b)}")
        
    print('Ejecución cerrada con comando exit')
    
# ============================
# Direct execution block
# ============================

if __name__ == '__main__':
    main()