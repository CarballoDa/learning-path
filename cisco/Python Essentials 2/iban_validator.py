"""Un número de cuenta compatible con IBAN consta de:

Código de país de dos letras tomado del estándar ISO 3166-1
Dos dígitos de verificación utilizados para realizar las verificaciones de validez: pruebas rápidas y simples, pero no totalmente confiables, que muestran si un número es inválido (distorsionado por un error tipográfico) o válido.
El número de cuenta real (hasta 30 caracteres alfanuméricos, la longitud de esa parte depende del país)."""

IBAN_BY_COUNTRY = {
    "AL": 28,  # Albania
    "AD": 24,  # Andorra
    "AT": 20,  # Austria
    "AZ": 28,  # Azerbaijan
    "BE": 16,  # Belgium
    "BH": 22,  # Bahrain
    "BA": 20,  # Bosnia and Herzegovina
    "BR": 29,  # Brazil
    "BG": 22,  # Bulgaria
    "CR": 22,  # Costa Rica
    "HR": 21,  # Croatia
    "CY": 28,  # Cyprus
    "CZ": 24,  # Czech Republic
    "DK": 18,  # Denmark
    "DO": 28,  # Dominican Republic
    "EE": 20,  # Estonia
    "FO": 18,  # Faroe Islands
    "FI": 18,  # Finland
    "FR": 27,  # France
    "GE": 22,  # Georgia
    "DE": 22,  # Germany
    "GI": 23,  # Gibraltar
    "GR": 27,  # Greece
    "GL": 18,  # Greenland
    "GT": 28,  # Guatemala
    "HU": 28,  # Hungary
    "IS": 26,  # Iceland
    "IE": 22,  # Ireland
    "IL": 23,  # Israel
    "IT": 27,  # Italy
    "JO": 30,  # Jordan
    "KZ": 20,  # Kazakhstan
    "KW": 30,  # Kuwait
    "LV": 21,  # Latvia
    "LB": 28,  # Lebanon
    "LI": 21,  # Liechtenstein
    "LT": 20,  # Lithuania
    "LU": 20,  # Luxembourg
    "MK": 19,  # North Macedonia
    "MT": 31,  # Malta
    "MR": 27,  # Mauritania
    "MU": 30,  # Mauritius
    "MD": 24,  # Moldova
    "MC": 27,  # Monaco
    "ME": 22,  # Montenegro
    "NL": 18,  # Netherlands
    "NO": 15,  # Norway
    "PK": 24,  # Pakistan
    "PL": 28,  # Poland
    "PS": 29,  # Palestine
    "PT": 25,  # Portugal
    "QA": 29,  # Qatar
    "RO": 24,  # Romania
    "SM": 27,  # San Marino
    "SA": 24,  # Saudi Arabia
    "RS": 22,  # Serbia
    "SK": 24,  # Slovakia
    "SI": 19,  # Slovenia
    "ES": 24,  # Spain
    "SE": 24,  # Sweden
    "CH": 21,  # Switzerland
    "TN": 24,  # Tunisia
    "TR": 26,  # Turkey
    "UA": 29,  # Ukraine
    "AE": 23,  # United Arab Emirates
    "GB": 22,  # United Kingdom
    "VG": 24,  # Virgin Islands
}

DIFF_BTW_ORD_IBAN = 55

# ===============
# Main functions
# ===============

def check_length(iban: str) -> bool:
    """Calcula la longitud en base al código de país y compara para ver si es correcta.

    Args:
        iban (str): cadena alfanumérica. Los dos primeros caracteres identifican el código de país.

    Returns:
        bool: True si la longitud es correcta. False en caso contrario.
        
    Examples:
        >>> check_length("ES9121000418450200051332")  # España
        True
        >>> check_length("DE89370400440532013000")   # Alemania
        True
        >>> check_length("DE8397040044053201300")    # Alemania - longitud incorrecta
        False
    """
    return len(iban) == IBAN_BY_COUNTRY[iban[0:2]]


def alter_iban(iban: str) -> str:
    """Coloca las cuatro primeras posiciones del IBAN al final del mismo.

    Args:
        iban (str): cadena alfanumérica.

    Returns:
        str: Retorna el IBAN modificado.
        
    Examples:
        >>> alter_iban("ES9121000418450200051332")
        '21000418450200051332ES91'
        >>> alter_iban("DE89370400440532013000")
        '370400440532013000DE89'
    """
    return iban[4:] + iban[0:4]


def get_chr_value(char: str) -> int:
    """Retorna el cálculo realizado sobre el ordinal del carácter.

    Args:
        char (str): carácter alfabético A - Z.

    Returns:
        int: Valor numérico correspondiente.
        
    Examples:
        >>> get_chr_value("A")
        10
        >>> get_chr_value("Z")
        35
    """
    return ord(char) - DIFF_BTW_ORD_IBAN


def iban_to_digits(iban: str) -> str:
    """Convierte un IBAN sustituyendo caracteres A - Z por valores numéricos.

    Args:
        iban (str): cadena alfanumérica.

    Returns:
        str: IBAN con todos los caracteres representados como números.
        
    Examples:
        >>> iban_to_digits("ES9121000418450200051332")
        '14289121000418450200051332'
        >>> iban_to_digits("DE89370400440532013000")
        '131489370400440532013000'
    """
    result = []
    for char in iban:
        if char.isalpha():
            result.append(str(get_chr_value(str(char).capitalize())))
        else:
            result.append(str(char))
    return ''.join(result)


def iban_residue(iban_digits: int) -> int:
    """Calcula el residuo de la división del IBAN digitalizado entre 97.

    Args:
        iban_digits (int): IBAN convertido a números.

    Returns:
        int: Residuo de IBAN digitalizado entre 97.
        
    Examples:
        >>> iban_residue(14289121000418450200051332)  # ES
        83
        >>> iban_residue(131489370400440532013000)    # DE - digitos modificados
        69
    """
    return int(iban_digits) % 97


def iban_verifier(iban: str = '') -> bool:
    """Realiza las validaciones necesarias sobre un IBAN.

    Args:
        iban (str): cadena alfanumérica.

    Returns:
        bool: True si es un IBAN válido. False en caso contrario.
        
    Examples:
        >>> iban_verifier("ES9121000418450200051332")
        True
        >>> iban_verifier("DE83970400440532013000")  # Alemania - dígito modificado
        False
    """
    if len(iban) == 0:
        print("Error: has ingresado un valor vacío.")
        return False
    if iban.isalpha() or iban.isnumeric():
        print("Error: debe contener letras y números.")
        return False
    if not check_length(iban):
        print(f"Error: la longitud del IBAN no es la correcta. Para COUNTRY CODE {iban[0:2]} ha de contener {IBAN_BY_COUNTRY[iban[0:2]]} caracteres.")
        return False
    
    iban_b = alter_iban(iban)
    iban_digits = iban_to_digits(iban_b)
    residue = iban_residue(int(iban_digits))
    
    return residue == 1

# ====================================
# Rapid, direct execution tests
# ====================================

def main():
    """Ejecuta pruebas rápidas de validación."""
    test_ibans = [
        "ES9121000418450200051332",  # España
        "DE89370400440532013000",    # Alemania
        "DE83970400440532013000",    # Alemania - digitos modificados
        "FR1420041010050500013M02606",  # Francia
        "GB29NWBK60161331926819",    # Reino Unido
        "IT60X0542811101000000123456",  # Italia        
        "FR1420041010050500013M06",  # Francia - longitud erronea
        "GB29NWBK6016133192819",    # Reino Unido - longitud erronea
        "IT60X054281123456",  # Italia - longitud erronea
        "24599988777887", # No simbolo de pais
        "tuirifkvmdjsddsajsadl", # solo letras
        ""
    ]

    for iban in test_ibans:
        result = iban_verifier(iban)
        print(f"-- IBAN: {iban} -> {'VÁLIDO' if result else 'INVÁLIDO'}")

# ============================
# Direct execution block
# ============================
if __name__ == "__main__":
    main()