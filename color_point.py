import random  # To generate random coordinates and random colors
from point import Point  # Import the Point class from a separate file

class PointException(Exception):
    """
    Custom exception class to handle invalid Point inputs.

    This exception is raised when invalid values are provided for Point coordinates,
    such as non-numeric types.
    """

    def __init__(self, *args):
        """
        Initialize the PointException.

        :param args: optional error message(s)
        :return: None
        """
        super().__init__(*args)

class ColorPoint(Point):
    """
    Extends the Point class by adding a color attribute.

    ColorPoint instances represent points in 2D space with an associated color.
    Input validation ensures x and y are numeric.
    """

    def __init__(self, x, y, color):
        """
        Initialize a ColorPoint with x, y coordinates and a color.

        :param x: int or float - the x-coordinate
        :param y: int or float - the y-coordinate
        :param color: str - the color associated with the point
        :raises PointException: if x or y is not a number (int or float)
        :return: None
        """
        if not isinstance(x, (int, float)):
            raise PointException("x must be a number")
        if not isinstance(y, (int, float)):
            raise PointException("y must be a number")

        super().__init__(x, y)  # Initialize base Point attributes
        self.color = color      # Assign color attribute

    def __str__(self):
        """
        Provide a human-readable string representation of the ColorPoint.

        :param: None
        :return: str - formatted string showing color and coordinates like "<color: x, y>"
        """
        return f"<{self.color}: {self.x}, {self.y}>"

# Example usage:
p = ColorPoint(1, 2, "red")  # Instantiate a ColorPoint
p.color = "rojo"             # Modify its color
p.x = 200                    # Modify its x value

print(p.distance_orig())     # Use inherited method to get distance from origin
print(p)                     # Use ColorPoint’s __str__

# The following code to create and sort random ColorPoints is commented out:
# colors = ("red", "green", "blue", "yellow", "black", "magneta",
#           "cyan", "white", "burgundy", "periwinkle", "marsala")
# color_points = []  # List to store 10 random ColorPoint instances
# for i in range(10):
#     color_points.append(
#         ColorPoint(random.randint(-10, 10),
#                    random.randint(-10, 10),
#                    random.choice(colors)))
# print(color_points)
# color_points.sort()  # Sort based on distance from origin (inherited __gt__)
# print(color_points)
