from point import Point

class ColorPoint(Point):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1, 2, "red")
print(p)