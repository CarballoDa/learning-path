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

def fibonacci(number: int) -> int:
    """
    Calculates the Fibonacci value for a specific number.

    Args:
        number (int): position in the Fibonacci sequence

    Returns:
        int: Fibonacci value at position n (0 if number < 1)

    Examples:
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
        >>> fibonacci(3)
        2
        >>> fibonacci(5)
        5
        >>> fibonacci(9)
        34
        >>> fibonacci(12)
        144
    """
    if number < 1:
        return 0
    elif number < 3:
        return 1
    
    prev, curr = 1, 1
    for _ in range(3, number + 1):
        prev, curr = curr, prev + curr
    return curr

def fibonacci_recur(number: int) -> int:
    """
    Calculates the Fibonacci value for a specific number using recursivity.

    Args:
        number (int): position in the Fibonacci sequence

    Returns:
        int: Fibonacci value at position n (0 if number < 1)

    Examples:
        >>> fibonacci_recur(1)
        1
        >>> fibonacci_recur(2)
        1
        >>> fibonacci_recur(3)
        2
        >>> fibonacci_recur(5)
        5
        >>> fibonacci_recur(9)
        34
        >>> fibonacci_recur(12)
        144
    """
    if number < 1:
        return 0
    elif number < 3:
        return 1
    
    return fibonacci_recur(number - 1) + fibonacci_recur(number - 2)

def get_fibonacci(number: int) -> int:
    """
    Validate input and return the Fibonacci number.

    Args:
        number (int): index of fibonacci series number

    Returns:
        int: Fibonacci value at position n
        
    Examples:
        >>> get_fibonacci(0)
        0
        >>> get_fibonacci(1)
        1
        >>> get_fibonacci(3)
        2
        >>> get_fibonacci(5)
        5
        >>> get_fibonacci(9)
        34
        >>> get_fibonacci(-3)
        Traceback (most recent call last):
            ...
        ValueError: Number must be greater than or equal to zero
        >>> get_fibonacci('a')
        Traceback (most recent call last):
            ...
        TypeError: Number must be integer
    """
    validate_int(number)
    validate_positive(number)
    return fibonacci(number)

# ====================================
# Rapid, direct execution tests
# ====================================

def main():
    # Quick tests
    print(get_fibonacci(5))
    print(get_fibonacci(4))
    print(get_fibonacci(10))

# ============================
# Direct execution block
# ============================
if __name__ == "__main__":
    main()