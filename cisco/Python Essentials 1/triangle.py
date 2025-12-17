# ==========================
# Funciones
# ==========================

def validate_sides(a: float, b: float, c: float) -> bool:
    """
    Check if all sides are over zero

    Args:
        a (float): Triangle side a
        b (float): Triangle side b
        c (float): Triangle side c

    Returns:
        bool: True if all sides are over zero. False otherwise.
        
    Examples:
        Valid Cases:
        >>> validate_sides(1, 1, 1)
        True
        >>> validate_sides(2, 2, 3)
        True
        >>> validate_sides(3, 2.5, 2)
        True

        Invalid Cases:
        >>> validate_sides(1, 1, 0)
        False
        >>> validate_sides(1, 0, 3)
        False
        >>> validate_sides(0, 0, 0)
        False
    """
    return a > 0 and b > 0 and c > 0

def is_a_triangle(a: float, b: float, c: float) -> bool:
    """
    Check if all sides forms a triangle

    Args:
        a (float): Triangle side a
        b (float): Triangle side b
        c (float): Triangle side c

    Returns:
        bool: True if it is a triangle, False if it is not a triangle
    
    Examples:
        Valid Cases:
        >>> is_a_triangle(1, 1, 1)
        True
        >>> is_a_triangle(2, 2, 3)
        True
        >>> is_a_triangle(3, 2.5, 2)
        True

        Invalid Cases:
        >>> is_a_triangle(1, 1, 3)
        False
        >>> is_a_triangle(1, 2, 3)
        False
        >>> is_a_triangle(1, 0.5, 2)
        False
    """
    if not validate_sides(a, b, c):
        return False
    return a + b > c and a + c > b and b + c > a

def is_a_right_triangle(a: float, b: float, c: float) -> bool:
    """
    Check if all sides forms a triangle rectangle

    Args:
        a (float): Triangle side a
        b (float): Triangle side b
        c (float): Triangle side c
        
    Returns:
        bool: True if it is a triangle rectangle, False if it is not
    
    Examples:
        Valid Cases:
        >>> is_a_right_triangle(2.5, 1.5, 2)
        True
        >>> is_a_right_triangle(10, 6, 8)
        True
        >>> is_a_right_triangle(5, 3, 4)
        True

        Invalid Cases:
        >>> is_a_right_triangle(1, 1, 3)
        False
        >>> is_a_right_triangle(1, 2, 3)
        False
        >>> is_a_right_triangle(1, 0.5, 2)
        False
    """
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    return False
 
def heron(a: float, b: float, c: float) -> float | bool:
    """
    Calculate triangle area

    Args:
        a (float): Triangle side a
        b (float): Triangle side b
        c (float): Triangle side c

    Returns:
        float | bool: Area if valid, False otherwise.
        
    Examples:
        Valid Cases:
        >>> heron(3, 4, 5)
        6.0
        >>> heron(6, 4, 5)
        9.921567416492215
        >>> heron(5, 4, 4)
        7.806247497997997

        Invalid Cases:
        >>> heron(1, 0, 0)
        False
        >>> heron(0, 2, 5.6)
        False
        >>> heron(0, 0.5, 0)
        False
    """
    if not is_a_triangle(a, b, c):
        return False
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_triangle(a: float, b: float, c: float) -> float | bool:
    """
    Checks if it is a valid triangle and returns its area

    Args:
        a (float): Triangle side a
        b (float): Triangle side b
        c (float): Triangle side c

    Returns:
        float | bool: area or False otherwise
        
    Examples:
        Valid Cases:
        >>> area_of_triangle(3, 4, 5)
        6.0
        >>> area_of_triangle(6, 4, 5)
        9.921567416492215
        >>> area_of_triangle(5, 4, 4)
        7.806247497997997

        Invalid Cases:
        >>> area_of_triangle(1, 0, 3)
        False
        >>> area_of_triangle(1, 0, 0)
        False
        >>> area_of_triangle(0, 0, 0)
        False
    """
    if not is_a_triangle(a, b, c):
        return False
    return heron(a, b, c)

# ====================================
# Pruebas rápidas de ejecución directa
# ====================================
def main():
    print("Triangle Main Tests:")
    print(is_a_triangle(1, 1, 1))
    print(is_a_triangle(1, 1, 3))
    print(is_a_triangle(1, 0, 3))    
    print(is_a_right_triangle(5, 3, 4))
    print(is_a_right_triangle(1, 3, 4))
    print(area_of_triangle(1., 1., 2. ** .5))
    
def user_input():
    a = float(input('Side A length: '))
    b = float(input('Side B length: '))
    c = float(input('Side C length: '))

    if is_a_triangle(a, b, c):
        print("Yes, this is a triangle.")
        print(f"Area = {area_of_triangle(a, b, c):.2f}")
        if is_a_right_triangle(a, b, c):
            print("It is also a right triangle.")
    else:
        print("It is not a triangle.")
    
# ============================
# Bloque de ejecución directa
# ============================
if __name__ == "__main__":
    main()
    user_input()