# ===============
# Main functions
# ===============

def caesar(text: str, shift: int) -> str:
    """Recibe una cadena de caracateres alfanuméricos y el punto de inicio de la tabla de codificación

    Args:
        text (str): Cadena de texto
        shift (int): Punto de partida tabla de cifrado, positivo o negativo

    Returns:
        str: texto codificado o descodificado (segun valor positivo om negativo de shitf)
        
    Examples:
        >>> caesar("davidCarball0", 2)
        fcxkfEctdcnn0
        >>> caesar("fcxkfEctdcnn0", -2)
        davidCarball0
    """
    
    translated = []
    for char in text:
        if char.isnumeric() or char == " ":
            translated.append(char)
            continue

        if char.isupper():
            starts = ord('A')
        else:
            starts = ord('a')

        # Normalizar, aplicar shift y modular
        code = ord(char) - starts
        code = (code + shift) % 26
        code = code + starts

        translated.append(chr(code))
    return ''.join(translated)

def cipher_me(text: str, shift: int) -> str:
    """Recibe una cadena de caracateres alfanuméricos y el punto de inicio de la tabla de codificación

    Args:
        text (str): Cadena de texto
        shift (int): Punto de partida tabla de cifrado. Se pasa como positivo.

    Returns:
        str: texto codificado de función caesar
        
    Examples:
        >>> cipher_me("davidCarball0", 2)
        fcxkfEctdcnn0
        >>> cipher_me("potueing8876ecc", 5)
        utyzjnsl8876jhh
    """
    return caesar(text, shift)

def uncipher_me(text: str, shift: int) -> str:
    """Recibe una cadena de caracateres alfanuméricos y el punto de inicio de la tabla de codificación

    Args:
        text (str): Cadena de texto
        shift (int): Punto de partida tabla de cifrado. Se pasa como negativo.

    Returns:
        str: texto descodificado de función caesar
        
    Examples:
        >>> uncipher_me("fcxkfEctdcnn0", -2)
        davidCarball0
        >>> uncipher_me("utyzjnsl8876jhh", 5)
        potueing8876ecc
    """
    return caesar(text, -shift)

# ====================================
# Rapid, direct execution tests
# ====================================

def main():
    """Ejecuta pruebas rápidas de validación."""
    while True: 
        txt = input('Ingresa un texto a codificar con el método Caesar: ').strip()
        if txt.lower() == 'exit':
            break
        if len(txt) == 0:
            raise ValueError("El texto no puede estar vacío")
        if not isinstance(txt, str):
            raise TypeError("Valor de texto ha de ser un texto válido")
        
        shift = int(input('Ingresa un valor de cifrado de 1 a 25: '))
        if not isinstance(shift, int):
            raise TypeError("Valor de inicio traducción ha de ser un número")
        if shift == 0 or abs(shift) == 25:
            raise ValueError("El valor de shift debe estar entre -25 y 25, excluyendo 0")
        
        
        txt_translated = cipher_me(txt, shift)
        txt_untranslated = uncipher_me(txt_translated, shift)
        print(f"Texto cifrado -> {txt_translated}")
        print(f"Texto descifrado -> {txt_untranslated}")
        
    print('Ejecución cerrada con comando exit')
    
# ============================
# Direct execution block
# ============================

if __name__ == '__main__':
    main()