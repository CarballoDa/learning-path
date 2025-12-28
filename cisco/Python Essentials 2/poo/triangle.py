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


class Triangle:
    """
    Represents a triangle defined by three Point instances.

    Attributes:
        __a (Point): First vertex.
        __b (Point): Second vertex.
        __c (Point): Third vertex.

    Examples:
        >>> t = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
        >>> round(t.perimeter(), 2)
        12.0
        >>> str(t)
        '3.0, 5.0, 4.0'
    """

    def __init__(self, a: Point, b: Point, c: Point) -> None:
        """
        Initializes a Triangle with three Point objects.

        Args:
            a (Point): First vertex.
            b (Point): Second vertex.
            c (Point): Third vertex.
        """
        self.__a = a
        self.__b = b
        self.__c = c

    def __str__(self) -> str:
        """
        Returns a string representation of the triangle's side lengths.

        Returns:
            str: Comma-separated distances between the triangle's vertices.

        Examples:
            >>> Triangle(Point(0,0), Point(1,0), Point(0,1)).__str__()
            '1.0, 1.4142135623730951, 1.0'
        """
        return (
            f"{self.__a.distance_from_point(self.__b)}, "
            f"{self.__b.distance_from_point(self.__c)}, "
            f"{self.__c.distance_from_point(self.__a)}"
        )

    def perimeter(self) -> float:
        """
        Computes the perimeter of the triangle.

        Returns:
            float: The sum of the lengths of all three sides.

        Examples:
            >>> t = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
            >>> t.perimeter()
            12.0
        """
        return (
            self.__a.distance_from_point(self.__b)
            + self.__b.distance_from_point(self.__c)
            + self.__c.distance_from_point(self.__a)
        )


# ====================================
# Rapid, direct execution tests
# ====================================

if __name__ == "__main__":
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle)
    print(triangle.perimeter())