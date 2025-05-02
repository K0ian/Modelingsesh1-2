import random  # To generate random coordinates and random colors
from point import Point  # Import the Point class from a separate file

class PointException(Exception):
    """
    Custom exception class to handle invalid Point inputs.
    """
    pass

class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        Initialize a ColorPoint, which extends Point by adding a color attribute.
        :param x: x-coordinate (int or float)
        :param y: y-coordinate (int or float)
        :param color: string representing the color
        :raises PointException: if x or y is not a number
        """
        # raise an exception if we try to have not a number
        if not isinstance(x, (int, float)):
            raise PointException("x must be a number")
        if not isinstance(y, (int, float)):
            raise PointException("y must be a number")

        super().__init__(x, y) # replaces the self.x and self.y
        self.color = color  # Assign color attribute

    def __str__(self):
        """
        Return a readable string showing color and coordinates.
        :return: formatted string "<color: x, y>"
        """
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1, 2, "red")  # Instantiate a ColorPoint
p.color = "rojo"             # Modify its color
p.x = 200                    # Modify its x value

print(p.distance_orig())     # Use inherited method to get distance from origin
print(p)                     # Use ColorPoint’s __str__

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
