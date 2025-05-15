from color_point import ColorPoint, PointException  # Import ColorPoint and custom exception class

class AdvancedPoint(ColorPoint):
    """
    An extension of ColorPoint that supports restricted color values,
    property decorators for coordinates and color, and utility methods
    such as creating from a tuple and calculating distances.
    """

    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]

    def __init__(self, x, y, color):
        """
        Initialize an AdvancedPoint with x, y coordinates and a restricted color.

        :param x: int or float - x-coordinate
        :param y: int or float - y-coordinate
        :param color: str - color string, must be in the COLORS list
        :raises PointException: if color is not in allowed COLORS
        :return: None
        """
        if color not in self.COLORS:
            raise PointException(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Get the x-coordinate of the point.

        :param: None
        :return: int or float - x-coordinate
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the point.

        :param value: int or float - new x-coordinate
        :return: None
        """
        self._x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the point.

        :param: None
        :return: int or float - y-coordinate
        """
        return self._y

    @property
    def color(self):
        """
        Get the color of the point.

        :param: None
        :return: str - color string
        """
        return self._color

    @classmethod
    def add_color(cls, color):
        """
        Add a new valid color to the class-level COLORS list.

        :param color: str - new color to add
        :return: None
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Create an AdvancedPoint instance from a coordinate tuple and optional color.

        :param coordinate: tuple - (x, y) coordinates
        :param color: str - optional color string (default is "red")
        :return: AdvancedPoint - new instance created from tuple and color
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculate the Euclidean distance between two AdvancedPoint instances.

        :param p1: AdvancedPoint - first point
        :param p2: AdvancedPoint - second point
        :return: float - Euclidean distance between p1 and p2
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Calculate the Euclidean distance from this point to another point.

        :param p: AdvancedPoint - another point to measure distance to
        :return: float - Euclidean distance between self and p
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

# Example usage
AdvancedPoint.add_color("rojo")  # Add a new valid color to the COLORS list
p = AdvancedPoint(1, 2, "rojo")  # Create an instance with the new color
print(p.x)
print(p)
print(p.distance_orig())  # Uses inherited method from Point

p2 = AdvancedPoint.from_tuple((3, 2))  # Create a point from a tuple
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))  # Static method: distance between two points
print(p.distance_to_other(p2))  # Instance method: distance to another point