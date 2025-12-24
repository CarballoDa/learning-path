# ==========================
# Global constants
# ==========================

POUND_TO_KG = 0.45359237
FOOT_TO_METER = 0.3048
INCH_TO_METER = 0.0254

# ==========================
# Functions
# ==========================

def lb_to_kg(lb: float) -> float:
    """
    Converts weight from pounds to kilograms.

    Args:
        lb (float): Weight in pounds.

    Returns:
        float: Equivalent weight in kilograms.
        
    Doctest:
        Valid cases:
        Convert 1 pound to kilograms.
        >>> lb_to_kg(1)
        0.45359237
    """
    return lb * POUND_TO_KG

def feet_inches_to_meters(ft: float, inch: float = 0.0) -> float:
    """
    Converts height given in feet and inches to meters.

    Args:
        ft (float): Number of feet.
        inch (float, optional): Number of inches. Defaults to 0.0.

    Returns:
        float: Equivalent height in meters.
        
    Doctest:
        Valid cases:
        Convert 1 foot and 1 inch to meters.
        >>> feet_inches_to_meters(1, 1)
        0.3302
        
        Convert 6 feet and 0 inches to meters.
        >>> feet_inches_to_meters(6)
        1.8288000000000002
    """
    return ft * FOOT_TO_METER + inch * INCH_TO_METER

def validate_values(weight: float, height: float):
    """
    Validates weight and height values.

    This function checks that weight and height fall within
    realistic ranges before performing calculations.

    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Raises:
        ValueError: If the values are out of range
        (weight < 20 or > 200, height < 1.0 or > 2.5).
         
    Doctest:
        Valid cases:
        >>> validate_values(70, 1.75)
        True
        >>> validate_values(20, 1.0)
        True
        >>> validate_values(200, 2.5)
        True

        Invalid cases:
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
    Calculates the Body Mass Index (BMI).

    The BMI is calculated using the formula:
    weight / height²

    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Returns:
        float: The calculated BMI value.

    Doctest:
        Valid cases:
        >>> bmi(52.5, 1.65)
        19.283746556473833

        >>> bmi(70, 1.75)
        22.857142857142858

        Invalid cases (out of range):
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
# Quick tests for direct execution
# ====================================
def main():
    # Output is limited to two decimal places using :.2f
    print(f"1) w = 52.5, h = 1.65 → BMI = {bmi(52.5, 1.65):.2f}")
    print(f"2) BMI = {bmi(weight=lb_to_kg(176), height=feet_inches_to_meters(5, 7)):.2f}")
    
# ============================
# Direct execution block
# ============================
if __name__ == "__main__":
    main()
