from color_point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]
    def __init__(self, x, y, color):
        if color not in self.COLORS:
            raise PointException(f"Invalid color, must be one of {self.COLORS}")
        super().__init__(x, y, color)

p = AdvancedPoint(1, 2, "rojo")
print(p)
print(p.distance_orig())

