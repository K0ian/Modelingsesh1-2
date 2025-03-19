import random
from point import Point

class PointException(Exception):
    pass

class ColorPoint(Point):
    def __init__(self, x, y, color):
        # raise an exception if we try to have not a number
        if not isinstance(x, (int, float)):
            raise PointException("x must be a number")
        if not isinstance(y, (int, float)):
            raise PointException("y must be a number")
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1, "jane", "red")
print(p.distance_orig())
print(p)
# colors = ("red", "green", "blue", "yellow", "black", "magneta" ,
#           "cyan", "white", "burgundy", "periwinkle", "marsala")
# color_points = []
# for i in range(10):
#     color_points.append(
#         ColorPoint(random.randint(-10, 10),
#                    random.randint(-10, 10),
#                    random.choice(colors)))
#
# print(color_points)
# color_points.sort()
# print(color_points)
