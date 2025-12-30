##########################################

"""
Crea una clase SimpleCounter que:
- Reciba un número n
- Itere desde 0 hasta n (incluido)
- Use __iter__() y __next__()
"""

class SimpleCounter:
    def __init__(self, n) -> None:
        self.__index = 0
        self.__limit = n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index > self.__limit:
            raise StopIteration
        value = self.__index
        self.__index += 1
        return value
    

"""for x in SimpleCounter(3):
    print(x)"""
    
##########################################

"""
Crea una clase ReverseList que:
- Reciba una lista
- Itere sus elementos desde el último hasta el primero
"""

class ReverseList:
    def __init__(self, the_list):
        self._list = the_list
        self._index = len(the_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return self._list[self._index]
    
    
"""
for x in ReverseList([10, 20, 30]):
    print(x)"""
    
##########################################

"""
Crea una clase StepIterator que:
- Reciba una lista y un número step
- Devuelva elementos saltando de step en step
"""

class StepIterator:
    def __init__(self, the_list, step=1):
        self._list = the_list
        self._step = step
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._list):
            raise StopIteration
        value = self._list[self._index]
        self._index += self._step
        return value
    
    
"""for x in StepIterator([1,2,3,4,5,6], 2):
    print(x)"""
    
##########################################

"""
Crea una clase Circular que:
- Reciba una lista y un número n
- Devuelva los elementos de la lista en orden circular durante n iteraciones
"""

class Circular:
    def __init__(self, the_list, n):
        self._list = the_list
        self._limit = n
        self._count = 0
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count >= self._limit:
            raise StopIteration
        value = self._list[self._index]
        self._index = (self._index + 1) % len(self._list)
        self._count += 1
        return value
    
"""   
for x in Circular(["A","B","C"], 5):
    print(x)"""
    
##########################################

"""
Crea una clase InfiniteEvenNumbers que:
- Empiece en 0
- Devuelva números pares infinitamente
- No se usa en un for (porque sería infinito)
"""

class InfiniteEvenNumbers:
    def __init__(self) -> None:
        self.__starts_with = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.__starts_with
        self.__starts_with += 2
        return value


"""evens = InfiniteEvenNumbers()
print(next(evens))  # 0
print(next(evens))  # 2
print(next(evens))  # 4"""

##########################################

"""
Concepto: iteradores que vuelven a empezar cuando llegan al final.
Crea una clase RestartingIterator que:
- Reciba una lista
- Itere sus elementos normalmente
- Pero cuando llegue al final, vuelva a empezar desde el principio
- Se detenga después de n elementos totales
"""

class RestartingIterator:
    def __init__(self, the_list, n) -> None:
        self.__index = 0
        self.__the_list = the_list
        self.__limit = n
        self.__counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):        
        if self.__counter >= self.__limit:
            raise StopIteration
        if self.__index == len(self.__the_list):
            self.__index = 0
        value = self.__the_list[self.__index]
        self.__index += 1
        self.__counter += 1
        return value
    
    
"""it = RestartingIterator(["A", "B", "C"], 7)
print([x for x in it])"""

##########################################

"""
Concepto: iteradores que transforman datos dinámicamente.
Crea una clase MapIterator que:
- Reciba una lista y una función
- Devuelva cada elemento transformado por esa función
"""


class MapIterator:
    def __init__(self, the_list, the_function) -> None:
        self.__the_list = the_list
        self.__the_function = the_function
        self.__index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index >= len(self.__the_list):
            raise StopIteration
        value = self.__the_function(self.__the_list[self.__index])
        self.__index += 1
        return value


def square(x): return x * x

def is_even(x): return True if x % 2 == 0 else False

def is_odd(x): return False if x % 2 == 0 else True


"""it = MapIterator([1, 2, 3, 4], square) # Aqui pasamos la funcion completa, no solo el nombre (no es un string, es una funcion)
print([x for x in it])
del it

it = MapIterator([1, 2, 3, 4], is_even) # Aqui pasamos la funcion completa, no solo el nombre (no es un string, es una funcion)
print([x for x in it])
del it

it = MapIterator([1, 2, 3, 4], is_odd) # Aqui pasamos la funcion completa, no solo el nombre (no es un string, es una funcion)
print([x for x in it])
del it"""

##########################################

"""
Concepto: iteradores que sincronizan múltiples secuencias.
Crea una clase ZipIterator que:
• 	Reciba dos listas
• 	Devuelva tuplas con elementos emparejados
• 	Se detenga cuando una de las dos listas termine
"""

class ZipIterator:
    def __init__(self, list_a, list_b) -> None:
        self.__list_a = list_a
        self.__list_b = list_b
        self.__index = 0 
        self.__limit = min(len(list_a), len(list_b))
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index >= self.__limit:
            raise StopIteration
        value = (self.__list_a[self.__index], self.__list_b[self.__index])
        self.__index += 1
        return value
        
    
"""it = ZipIterator([1, 2, 3], ["a", "b"])
print([x for x in it])"""

##########################################

"""
Concepto: iteradores que generan ventanas deslizantes (muy usado en análisis de datos).
Crea una clase WindowIterator que:
- Reciba una lista y un tamaño de ventana k
- Devuelva listas con ventanas consecutivas de tamaño k
"""

class WindowIterator:
    def __init__(self, the_list, k) -> None:
        self.__the_list = the_list
        self.__window_size = k
        self.__index = 0
        self.__limit = len(self.__the_list)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index + self.__window_size > self.__limit:
            raise StopIteration
        value = self.__the_list[self.__index:self.__index + self.__window_size]
        self.__index += 1
        return value


"""it = WindowIterator([1,2,3,4,5], 3)
print([x for x in it])"""

##########################################

"""
Concepto: iteradores infinitos con estado complejo.
Crea una clase FibonacciIterator que:
- Genere números de Fibonacci infinitamente
- Se use solo con next()
"""

class FibonacciIterator:
    def __init__(self):
        self._prev = 0
        self._curr = 1
        self._first = True

    def __iter__(self):
        return self

    def __next__(self):
        # First call → return 0
        if self._first:
            self._first = False
            return self._prev

        # Second call → return 1
        value = self._curr

        # Update Fibonacci state
        self._prev, self._curr = self._curr, self._prev + self._curr

        return value

fib = FibonacciIterator()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
print(next(fib))  # 2
print(next(fib))  # 3