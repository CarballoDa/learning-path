VALID_DAYS = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]


class WeekDayError(Exception):
    """
    Custom exception raised when an invalid weekday name is provided.
    """
    pass


class Weeker:
    """
    A class that represents a weekday and allows shifting it forward or backward.

    Attributes:
        __day (int): Index of the current weekday in VALID_DAYS.

    Examples:
        >>> w = Weeker("Lun")
        >>> print(w)
        Lun
        >>> w.add_days(3)
        >>> print(w)
        Jue
        >>> w.substract_days(5)
        >>> print(w)
        Sab
        >>> Weeker("Lunes")
        Traceback (most recent call last):
            ...
        WeekDayError: Sorry, request can not be processed.
    """

    def __init__(self, day: str) -> None:
        """
        Initializes the Weeker with a valid weekday name.

        Args:
            day (str): A valid weekday name in Spanish (e.g., "Lun", "Mar", ...).

        Raises:
            WeekDayError: If the provided day is not in VALID_DAYS.
        """
        if day not in VALID_DAYS:
            raise WeekDayError("Sorry, request can not be processed.")
        self.__day = VALID_DAYS.index(day)

    def __str__(self) -> str:
        """
        Returns the current weekday as a string.

        Returns:
            str: The name of the current weekday.

        Examples:
            >>> str(Weeker("Vie"))
            'Vie'
        """
        return VALID_DAYS[self.__day]

    def add_days(self, n: int) -> None:
        """
        Advances the weekday by n days.

        Args:
            n (int): Number of days to move forward.

        Examples:
            >>> w = Weeker("Dom")
            >>> w.add_days(2)
            >>> str(w)
            'Mar'
        """
        self.__day = (self.__day + n) % 7

    def substract_days(self, n: int) -> None:
        """
        Moves the weekday backward by n days.

        Args:
            n (int): Number of days to move backward.

        Examples:
            >>> w = Weeker("Mar")
            >>> w.substract_days(4)
            >>> str(w)
            'Vie'
        """
        self.__day = (self.__day - n) % 7