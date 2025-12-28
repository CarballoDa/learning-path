import math


class Point:
    """
    Represents a point in a 2D Cartesian coordinate system.

    Attributes:
        __x (float): X coordinate.
        __y (float): Y coordinate.

    Examples:
        >>> p = Point(3, 4)
        >>> p.getx(), p.gety()
        (3, 4)
        >>> p.distance_from_xy(0, 0)
        5.0
        >>> p2 = Point(6, 8)
        >>> p.distance_from_point(p2)
        5.0
    """

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """
        Initializes a Point with given x and y coordinates.

        Args:
            x (float): X coordinate. Defaults to 0.0.
            y (float): Y coordinate. Defaults to 0.0.
        """
        self.__x = x
        self.__y = y

    def getx(self) -> float:
        """
        Returns the X coordinate.

        Returns:
            float: The X value.

        Examples:
            >>> Point(5, 2).getx()
            5
        """
        return self.__x

    def gety(self) -> float:
        """
        Returns the Y coordinate.

        Returns:
            float: The Y value.

        Examples:
            >>> Point(5, 2).gety()
            2
        """
        return self.__y

    def distance_from_xy(self, x: float, y: float) -> float:
        """
        Computes the Euclidean distance from this point to another (x, y).

        Args:
            x (float): X coordinate of the target point.
            y (float): Y coordinate of the target point.

        Returns:
            float: The distance between the two points.

        Examples:
            >>> Point(0, 0).distance_from_xy(3, 4)
            5.0
        """
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point: "Point") -> float:
        """
        Computes the Euclidean distance from this point to another Point instance.

        Args:
            point (Point): The target point.

        Returns:
            float: The distance between the two points.

        Examples:
            >>> p1 = Point(1, 1)
            >>> p2 = Point(4, 5)
            >>> p1.distance_from_point(p2)
            5.0
        """
        return self.distance_from_xy(point.getx(), point.gety())


# ====================================
# Rapid, direct execution tests
# ====================================

if __name__ == "__main__":
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(2, 0))