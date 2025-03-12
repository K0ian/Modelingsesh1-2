import random

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x # define x attribute via self.x
        self.y = y # and assign the value x to it

    def __str__(self):
        """
        Magic Method that
        :param self:
        :return: Point (x,y)
        """

        return f"Point ({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__() # use the same way of printing as str
    def distance_orig(self):
        return (self.x**2 + self.y**2)**0.5 # square root of the sum of x

# now we need to instantiate it!
p = Point(1, 2) # p is an instance of 1 and 2
p2 = Point(2, 3)
p4 = Point(4.4, -55)
print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
p.x = 20
print(f"p.x={p.x} and p.y={p.y}")
print(p)
# Create a list of 5 random points
points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10), # x value
                        random.randint(-10, 10))) # y value
print("I got these 5 random points:")
for p in points:
    print(p)