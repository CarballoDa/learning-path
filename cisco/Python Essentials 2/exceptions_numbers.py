"""
1. Algunas excepciones integradas abstractas de Python son:

ArithmeticError,
BaseException,
LookupError.

2. Algunas excepciones integradas concretas de Python son:

AssertionError,
ImportError,
IndexError,
KeyboardInterrupt,
KeyError,
MemoryError,
OverflowError.

"""
print(float("1, 3"))





def read_int(prompt, min, max):
    try:
        number = int(input(prompt))
    except ValueError:
        print("Error: entrada incorrecta")
        exit()
    
    if not min < number < max:
        print(f"Error: el valor no está dentro del rango permitido ({str(min)}..{str(max)})")
        exit()
        
    return number
    

v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)
print("El número es:", v)