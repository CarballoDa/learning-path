# ====================
# External Functions
# ====================

def format_time(h: int, m: int, s: int) -> str:
    """
    Formats hours, minutes, and seconds into a zero-padded string "hh:mm:ss".

    Args:
        h (int): Hours (0-23)
        m (int): Minutes (0-59)
        s (int): Seconds (0-59)

    Returns:
        str: Time formatted as "hh:mm:ss"

    Examples:
        >>> format_time(5, 7, 9)
        '05:07:09'
        >>> format_time(12, 30, 0)
        '12:30:00'
    """
    return f"{h:02}:{m:02}:{s:02}"



# ================
# My Timer Class
# ================


class Timer:
    """
    A class that represents a 24-hour timer with second-level precision.
    It allows moving forward or backward by one second.

    Examples:
        >>> t = Timer(23, 59, 59)
        >>> print(t)
        23:59:59
        >>> t.next_second()
        >>> print(t)
        00:00:00
        >>> t.prev_second()
        >>> print(t)
        23:59:59
    """

    def __init__(self, h: int = 0, m: int = 0, s: int = 0) -> None:
        """
        Initializes a new Timer instance.

        Args:
            h (int): Hours (0-23). Defaults to 0.
            m (int): Minutes (0-59). Defaults to 0.
            s (int): Seconds (0-59). Defaults to 0.

        Raises:
            ValueError: If any value is out of range.

        Examples:
            >>> t = Timer(12, 30, 45)
            >>> print(t)
            12:30:45
            >>> Timer(25, 0, 0)
            Traceback (most recent call last):
                ...
            ValueError: Hours must be in range 0-23
        """
        if not (0 <= h <= 23): raise ValueError("Hours must be in range 0-23")
        if not (0 <= m <= 59): raise ValueError("Minutes must be in range 0-59")
        if not (0 <= s <= 59): raise ValueError("Seconds must be in range 0-59")
        self.__hours = h
        self.__minutes = m
        self.__seconds = s

    def __str__(self) -> str:
        """
        Returns the timer as a formatted string "hh:mm:ss".

        Returns:
            str: The current time of the timer.

        Examples:
            >>> str(Timer(1, 2, 3))
            '01:02:03'
        """
        return format_time(self.__hours, self.__minutes, self.__seconds)

    def next_second(self) -> None:
        """
        Advances the timer by one second.
        Rolls over to 00:00:00 after 23:59:59.

        Examples:
            >>> t = Timer(23, 59, 59)
            >>> t.next_second()
            >>> str(t)
            '00:00:00'
        """
        total = self.__hours * 3600 + self.__minutes * 60 + self.__seconds + 1
        total %= 86400
        self.__hours, rem = divmod(total, 3600)
        self.__minutes, self.__seconds = divmod(rem, 60)

    def prev_second(self) -> None:
        """
        Moves the timer back by one second.
        Rolls back to 23:59:59 from 00:00:00.

        Examples:
            >>> t = Timer(0, 0, 0)
            >>> t.prev_second()
            >>> str(t)
            '23:59:59'
        """
        total = self.__hours * 3600 + self.__minutes * 60 + self.__seconds - 1
        total %= 86400
        self.__hours, rem = divmod(total, 3600)
        self.__minutes, self.__seconds = divmod(rem, 60)
        

# ====================================
# Rapid, direct execution tests
# ====================================


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)