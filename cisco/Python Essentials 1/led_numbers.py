NUMBERS_TO_LED_BIG = {
    0: [
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ],
    1: [
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  "
    ],
    2: [
        "#####",
        "    #",
        "    #",
        "    #",
        "#####",        
        "#    ",
        "#    ",
        "#    ",
        "#####"
    ],
    3: [
        "#####",
        "    #",
        "    #",
        "    #",
        "#####",
        "    #",
        "    #",
        "    #",
        "#####"
    ],
    4: [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#####",
        "    #",
        "    #",
        "    #",
        "    #"
    ],
    5: [
        "#####",
        "#    ",
        "#    ",
        "#    ",
        "#####",
        "    #",
        "    #",
        "    #",
        "#####"
    ],
    6: [
        "#####",
        "#    ",
        "#    ",
        "#    ",
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ],
    7: [
        "#####",
        "    #",
        "    #",
        "    #",
        "    #",
        "    #",
        "    #",
        "    #",
        "    #"
    ],
    8: [
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#####",        
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ],
    9: [
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#####",
        "    #",
        "    #",
        "    #",
        "#####"
    ]
}

def print_leds(number):
    """
    Prints a number using a large LED-style representation.

    Each digit is displayed using ASCII characters, similar to
    what you might see on a digital display. Multiple digits
    are printed side by side.

    Args:
        number (int): A non-negative integer to be displayed.

    Raises:
        ValueError: If the number is negative.

    Doctest:
        Valid case:
        Print a single digit.
        >>> print_leds(2)
        ##### 
            #
            #
            #
        ##### 
        #     
        #     
        #     
        #####

        Print multiple digits.
        >>> print_leds(10)
          #   #####
          #   #   #
          #   #   #
          #   #   #
          #   #   #
          #   #   #
          #   #   #
          #   #   #
          #   #####

        Invalid case:
        >>> print_leds(-1)
        Traceback (most recent call last):
            ...
        ValueError: Error: debe ser un numero entero positivo mayor o igual que cero
    """
    if number < 0:
        raise ValueError('Error: debe ser un numero entero positivo mayor o igual que cero')
    
    digits = list(str(number))
    height = len(next(iter(NUMBERS_TO_LED_BIG.values())))

    for row in range(height):
        print(" ".join(NUMBERS_TO_LED_BIG[int(d)][row] for d in digits))
        

# ====================================
# Quick tests for direct execution
# ====================================
def main():
    print_leds(9081726354)
    print_leds("abcd")
    
# ============================
# Direct execution block
# ============================
if __name__ == "__main__":
    main()