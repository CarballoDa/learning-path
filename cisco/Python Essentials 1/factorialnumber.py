def validate_int(number: int) -> bool:
    """
    Validate that the input is an integer.

    Args:
        number (int): value to validate

    Raises:
        TypeError: if the value is not an integer

    Returns:
        bool: True if validation succeeds

    Examples:
        >>> validate_int(0)
        True
        >>> validate_int(3)
        True
        >>> validate_int(5688)
        True
        >>> validate_int('a')
        Traceback (most recent call last):
            ...
        TypeError: Number must be integer
        >>> validate_int({'a'})
        Traceback (most recent call last):
            ...
        TypeError: Number must be integer
        >>> validate_int(['a'])
        Traceback (most recent call last):
            ...
        TypeError: Number must be integer
    """
    if not isinstance(number, int):
        raise TypeError("Number must be integer")
    return True

def validate_positive(number: int) -> bool:
    """
    Validate that the number is zero or greater.

    Args:
        number (int): value to validate

    Raises:
        ValueError: if the number is negative

    Returns:
        bool: True if validation succeeds
        
    Examples:
        >>> validate_positive(0)
        True
        >>> validate_positive(3)
        True
        >>> validate_positive(-8)
        Traceback (most recent call last):
            ...
        ValueError: Number must be greater than or equal to zero
        >>> validate_positive(-30)
        Traceback (most recent call last):
            ...
        ValueError: Number must be greater than or equal to zero
    """
    if number < 0:
        raise ValueError("Number must be greater than or equal to zero")
    return True

def get_factorial(number: int) -> int:
    """
    Calculate the factorial of a non‑negative integer n.

    Args:
        number (int): value to calculate

    Returns:
        int: result
        
    Examples:
        >>> get_factorial(0)
        1
        >>> get_factorial(4)
        24
        >>> get_factorial(1)
        1
        >>> get_factorial(5)
        120
    """
    result = 1
    for index in range(2, number + 1):
        result *= index
    return result

def factorial(number: int) -> int:
    """
    Validate input and calculate factorial.

    Args:
        number (int): value to calculate

    Returns:
        int: factorial result

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(10)
        3628800
        >>> factorial(-3)
        Traceback (most recent call last):
            ...
        ValueError: Number must be greater than or equal to zero
        >>> factorial('a')
        Traceback (most recent call last):
            ...
        TypeError: Number must be integer
    """
    validate_int(number)
    validate_positive(number)
    return get_factorial(number)

# ====================================
# Rapid, direct execution tests
# ====================================

def main():
    # Quick tests
    print(factorial(5))
    print(factorial(4))
    print(factorial(1))

# ============================
# Direct execution block
# ============================
if __name__ == "__main__":
    main()