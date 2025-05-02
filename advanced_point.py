from color_point import ColorPoint, PointException  # Import ColorPoint and custom exception class

class AdvancedPoint(ColorPoint):
    """
    An extension of ColorPoint that supports restricted color values,
    property decorators, and additional utility methods.
    """
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]

    def __init__(self, x, y, color):
        """
        Initialize an AdvancedPoint with coordinates and a valid color.
        :param x: x-coordinate (int or float)
        :param y: y-coordinate (int or float)
        :param color: string representing the color
        :raises PointException: if color not in allowed COLORS list
        """
        if color not in self.COLORS:
            raise PointException(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property  # shortcut for calling a function without needing to say p.x() instead calling it p.x
    def x(self):
        """
        Getter for x-coordinate.
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Setter for x-coordinate.
        """
        self._x = value

    @property
    def y(self):
        """
        Getter for y-coordinate.
        """
        return self._y

    @property
    def color(self):
        """
        Getter for color.
        """
        return self._color

    @classmethod
    def add_color(cls, color):
        """
        Adds a new valid color for our class.
        :param color: new color to add to the valid COLORS list
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Create a new point from a tuple rather than 2 individual values.
        :param coordinate: a tuple (x, y)
        :param color: optional color string (default "red")
        :return: AdvancedPoint instance
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Static method to calculate distance between two points.
        :param p1: first point (AdvancedPoint)
        :param p2: second point (AdvancedPoint)
        :return: Euclidean distance as float
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Instance method to calculate distance to another point.
        :param p: another point
        :return: Euclidean distance as float
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5


AdvancedPoint.add_color("rojo")
p = AdvancedPoint(1, 2, "rojo")  # Create an instance with the new color
print(p.x)
print(p)  # Uses __str__ inherited from ColorPoint
print(p.distance_orig())
p2 = AdvancedPoint.from_tuple((3, 2))
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))  # Static method: distance between two points
print(p.distance_to_other(p2))
