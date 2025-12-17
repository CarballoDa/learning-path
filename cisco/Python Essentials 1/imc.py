# ==========================
# Constantes globales
# ==========================

POUND_TO_KG = 0.45359237
FOOT_TO_METER = 0.3048
INCH_TO_METER = 0.0254

# ==========================
# Funciones
# ==========================

def lb_to_kg(lb: float) -> float:
    """
    Convierte libras a kilogramos.

    Args:
        lb (float): Peso en libras.

    Returns:
        float: Peso equivalente en kilogramos.
        
    Doctest:
        Casos válidos: 
        Converir 1 libra a kilogramos.    
        >>> lb_to_kg(1)
        0.45359237
    """
    return lb * POUND_TO_KG

def feet_inches_to_meters(ft: float, inch: float = 0.0) -> float:
    """
    Convierte pies y pulgadas a metros.

    Args:
        ft (float): Número de pies.
        inch (float, opcional): Número de pulgadas. Por defecto 0.0.

    Returns:
        float: Altura equivalente en metros.
        
    Doctest:
        Casos válidos:
        Converir 1 ft y 1 inch a metros.    
        >>> feet_inches_to_meters(1, 1)
        0.3302
        
        Converir 6 ft y 0 inch a metros.    
        >>> feet_inches_to_meters(6)
        1.8288000000000002
    
    """
    return ft * FOOT_TO_METER + inch * INCH_TO_METER

def validate_values(weight: float, height: float):
    """
    Valida los valores de peso y altura.

    Args:
        weight (float): Peso en kilogramos.
        height (float): Altura en metros.

    Raises:
        ValueError: Si los valores están fuera de rango (peso <20 o >200, altura <1.0 o >2.5).
         
    Doctest:
        Casos válidos:
        >>> validate_values(70, 1.75)
        True
        >>> validate_values(20, 1.0)
        True
        >>> validate_values(200, 2.5)
        True

        Casos inválidos:
        >>> validate_values(25, 0.5)
        Traceback (most recent call last):
            ...
        ValueError: Valores fuera de rango para peso o altura

        >>> validate_values(300, 1.8)
        Traceback (most recent call last):
            ...
        ValueError: Valores fuera de rango para peso o altura
    
    """
    if not (1.0 <= height <= 2.5 and 20 <= weight <= 200):
        raise ValueError("Valores fuera de rango para peso o altura")
    return True

def bmi(weight: float, height: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        weight (float): Peso en kilogramos.
        height (float): Altura en metros.

    Returns:
        float: Valor del IMC.

    Doctest:
        Casos válidos:
        >>> bmi(52.5, 1.65)
        19.283746556473833

        >>> bmi(70, 1.75)
        22.857142857142858

        Casos inválidos (fuera de rango):
        >>> bmi(10, 1.8)
        Traceback (most recent call last):
            ...
        ValueError: Valores fuera de rango para peso o altura

        >>> bmi(80, 3.0)
        Traceback (most recent call last):
            ...
        ValueError: Valores fuera de rango para peso o altura
    """
    validate_values(weight, height)    
    return weight / height ** 2

# ====================================
# Pruebas rápidas de ejecución directa
# ====================================
def main():
    # Se limita la salida a dos decimales con :.2f
    print(f"1) w = 52.5, h = 1.65 → BMI = {bmi(52.5, 1.65):.2f}")
    print(f"2) BMI = {bmi(weight=lb_to_kg(176), height=feet_inches_to_meters(5, 7)):.2f}")
    
# ============================
# Bloque de ejecución directa
# ============================
if __name__ == "__main__":
    main()