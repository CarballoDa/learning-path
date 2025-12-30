"""
A collection of custom iterator classes used for educational purposes.
Each iterator demonstrates a different iteration pattern or behavior.
"""


class SimpleCounter:
    """
    A simple iterator that counts from 0 up to a given limit (inclusive).

    Args:
        n (int): The maximum number to count to.

    Examples:
        >>> list(SimpleCounter(3))
        [0, 1, 2, 3]
    """

    def __init__(self, n) -> None:
        self.__index = 0
        self.__limit = n

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next number in the sequence.

        Raises:
            StopIteration: When the counter exceeds the limit.

        Examples:
            >>> it = SimpleCounter(2)
            >>> next(it)
            0
            >>> next(it)
            1
            >>> next(it)
            2
            >>> next(it)
            Traceback (most recent call last):
                ...
            StopIteration
        """
        if self.__index > self.__limit:
            raise StopIteration
        value = self.__index
        self.__index += 1
        return value


class ReverseList:
    """
    An iterator that yields elements of a list in reverse order.

    Args:
        the_list (list): The list to iterate backwards.

    Examples:
        >>> list(ReverseList([10, 20, 30]))
        [30, 20, 10]
    """

    def __init__(self, the_list):
        self._list = the_list
        self._index = len(the_list)

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next element in reverse order.

        Raises:
            StopIteration: When all elements have been returned.
        """
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return self._list[self._index]


class StepIterator:
    """
    An iterator that returns elements from a list, skipping by a given step.

    Args:
        the_list (list): The list to iterate.
        step (int): Step size between elements.

    Examples:
        >>> list(StepIterator([1,2,3,4,5,6], 2))
        [1, 3, 5]
    """

    def __init__(self, the_list, step=1):
        self._list = the_list
        self._step = step
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next stepped element.

        Raises:
            StopIteration: When the index exceeds the list length.
        """
        if self._index >= len(self._list):
            raise StopIteration
        value = self._list[self._index]
        self._index += self._step
        return value


class Circular:
    """
    An iterator that loops through a list in circular order for a fixed number of iterations.

    Args:
        the_list (list): The list to iterate circularly.
        n (int): Total number of values to produce.

    Examples:
        >>> list(Circular(["A","B","C"], 5))
        ['A', 'B', 'C', 'A', 'B']
    """

    def __init__(self, the_list, n):
        self._list = the_list
        self._limit = n
        self._count = 0
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next circular element.

        Raises:
            StopIteration: When the total number of iterations is reached.
        """
        if self._count >= self._limit:
            raise StopIteration
        value = self._list[self._index]
        self._index = (self._index + 1) % len(self._list)
        self._count += 1
        return value


class InfiniteEvenNumbers:
    """
    An infinite iterator that yields even numbers starting from 0.

    Examples:
        >>> it = InfiniteEvenNumbers()
        >>> next(it)
        0
        >>> next(it)
        2
        >>> next(it)
        4
    """

    def __init__(self) -> None:
        self.__starts_with = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next even number.

        Note:
            This iterator never stops.
        """
        value = self.__starts_with
        self.__starts_with += 2
        return value


class RestartingIterator:
    """
    An iterator that restarts from the beginning of the list when reaching the end,
    stopping only after producing a fixed number of elements.

    Args:
        the_list (list): The list to iterate circularly.
        n (int): Total number of values to produce.

    Examples:
        >>> list(RestartingIterator(["A","B","C"], 7))
        ['A', 'B', 'C', 'A', 'B', 'C', 'A']
    """

    def __init__(self, the_list, n) -> None:
        self.__index = 0
        self.__the_list = the_list
        self.__limit = n
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next element, restarting when reaching the end.

        Raises:
            StopIteration: When the total number of iterations is reached.
        """
        if self.__counter >= self.__limit:
            raise StopIteration
        if self.__index == len(self.__the_list):
            self.__index = 0
        value = self.__the_list[self.__index]
        self.__index += 1
        self.__counter += 1
        return value


class MapIterator:
    """
    An iterator that applies a transformation function to each element of a list.

    Args:
        the_list (list): The list to iterate.
        the_function (callable): A function applied to each element.

    Examples:
        >>> list(MapIterator([1,2,3], lambda x: x * 2))
        [2, 4, 6]
    """

    def __init__(self, the_list, the_function) -> None:
        self.__the_list = the_list
        self.__the_function = the_function
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Applies the function to the next element.

        Raises:
            StopIteration: When all elements have been processed.
        """
        if self.__index >= len(self.__the_list):
            raise StopIteration
        value = self.__the_function(self.__the_list[self.__index])
        self.__index += 1
        return value


class ZipIterator:
    """
    An iterator that pairs elements from two lists, stopping when the shortest ends.

    Args:
        list_a (list): First list.
        list_b (list): Second list.

    Examples:
        >>> list(ZipIterator([1,2,3], ["a","b"]))
        [(1, 'a'), (2, 'b')]
    """

    def __init__(self, list_a, list_b) -> None:
        self.__list_a = list_a
        self.__list_b = list_b
        self.__index = 0
        self.__limit = min(len(list_a), len(list_b))

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next paired tuple.

        Raises:
            StopIteration: When one of the lists ends.
        """
        if self.__index >= self.__limit:
            raise StopIteration
        value = (self.__list_a[self.__index], self.__list_b[self.__index])
        self.__index += 1
        return value


class WindowIterator:
    """
    An iterator that yields sliding windows of size k from a list.

    Args:
        the_list (list): The list to iterate.
        k (int): Window size.

    Examples:
        >>> list(WindowIterator([1,2,3,4,5], 3))
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    """

    def __init__(self, the_list, k) -> None:
        self.__the_list = the_list
        self.__window_size = k
        self.__index = 0
        self.__limit = len(self.__the_list)

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next sliding window.

        Raises:
            StopIteration: When no more windows fit.
        """
        if self.__index + self.__window_size > self.__limit:
            raise StopIteration
        value = self.__the_list[self.__index:self.__index + self.__window_size]
        self.__index += 1
        return value


class FibonacciIterator:
    """
    An infinite iterator that generates Fibonacci numbers.

    Examples:
        >>> fib = FibonacciIterator()
        >>> next(fib)
        0
        >>> next(fib)
        1
        >>> next(fib)
        1
        >>> next(fib)
        2
        >>> next(fib)
        3
    """

    def __init__(self):
        self._prev = 0
        self._curr = 1
        self._first = True

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next Fibonacci number.

        Note:
            This iterator never stops.
        """
        if self._first:
            self._first = False
            return self._prev

        value = self._curr
        self._prev, self._curr = self._curr, self._prev + self._curr
        return value