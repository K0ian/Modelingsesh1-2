import random  # Import random module to generate random integers

# Class --> blueprint for creating objects that share the same structure but have different values.
# Magic Method --> Special built-in function  w/ double underscores defining how an object behaves in operations like printing, adding, etc.

class Point:
    """
    Represents a point in 2D Cartesian coordinate system.

    The Point class stores x and y coordinates and supports operations such as
    computing distance from origin and comparing points based on that distance.
    """

    def __init__(self, x, y):
        """
        Initialize a Point object with x and y coordinates.

        :param x: int or float - the x position on the axis
        :param y: int or float - the y position on the axis
        :return: None
        """
        self.x = x  # define x attribute via self.x
        self.y = y  # and assign the value y to it

    def __str__(self):
        """
        Return a human-readable string representation of the point.

        :param self: Point - the instance itself
        :return: str - formatted string like "Point (x, y)"
        """
        return f"Point ({self.x}, {self.y})"

    def __repr__(self):
        """
        Return an official string representation of the point, useful for debugging and printing lists.

        :param self: Point - the instance itself
        :return: str - same string as __str__
        """
        return self.__str__()  # use the same way of printing as str

    def distance_orig(self):
        """
        Calculate the Euclidean distance of the point from the origin (0,0).

        Uses the Pythagorean theorem: sqrt(x^2 + y^2).

        :param self: Point - the instance itself
        :return: float - Euclidean distance from origin
        """
        return (self.x**2 + self.y**2)**0.5  # square root of the sum of squares

    def __gt__(self, other):
        """
        Compare this point with another based on their distances from the origin.

        :param self: Point - this instance
        :param other: Point - another Point instance to compare
        :return: bool - True if this point is farther from origin than other
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance


if __name__ == "__main__":
    """
    Main block to run example/test code when script is executed directly.
    """

    # instantiate points with fixed coordinates
    p = Point(1, 2)
    p2 = Point(2, 3)
    p4 = Point(4.4, -55)

    print(f"p.x={p.x} and p.y={p.y}")  # Access and print coordinates
    print(f"p4.x={p4.x} and p4.y={p4.y}")  # Print coordinates of another point

    p.x = 20  # Change the x value of point p
    print(f"p.x={p.x} and p.y={p.y}")  # Print updated point

    print(p)  # Print string representation of point p

    # Create a list of 5 random points
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10, 10),  # x value
                            random.randint(-10, 10)))  # y value

    print("I got these 5 random points:")  # Show list before sorting
    print(points)  # Print list using __repr__

    p = Point(3, 4)  # Create a new point to test distance
    print(p.distance_orig())  # expect 5 answer (3-4-5 triangle)

    p2 = Point(1, 1)  # Create another point to compare
    print(f"I am comparing p > p2: {p > p2}")  # Expect True since p is farther

    print("the sorted list of points is:")  # Sorting based on distance from origin
    points.sort()
    print(points)