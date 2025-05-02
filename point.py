import random  # Import random module to generate random integers

# Class --> blueprint for creating objects that share the same structure but have different values.
# Magic Method --> Special built-in function  w/ double underscores defining how an object behaves in operations like printing, adding, etc.

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x # define x attribute via self.x
        self.y = y # and assign the value x to it

    def __str__(self): # to make the output more readable
        """
        Magic Method that
        :param self:
        :return: Point (x,y)
        """
        return f"Point ({self.x}, {self.y})"

    def __repr__(self):
        """
        Magic Method used when printing lists or inspecting objects in a console.
        :param self:
        :return: Point (x,y) same as __str__
        """
        return self.__str__() # use the same way of printing as str

    def distance_orig(self):
        """
        Calculate the distance of the point from the origin using the Pythagorean theorem.
        :param self:
        :return: Euclidean distance from origin
        """
        return (self.x**2 + self.y**2)**0.5 # square root of the sum of x

    def __gt__(self, other):
        """
        Magic Method that compares two points based on their distance from the origin.
        :param other: another Point object
        :return: True if self is farther from origin than other
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

if __name__ == "__main__":
    """
    Main block to run test code when the script is executed directly.
    """

    # now we need to instantiate it!
    p = Point(1, 2) # p is an instance of 1 and 2
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
        points.append(Point(random.randint(-10, 10), # x value
                            random.randint(-10, 10))) # y value

    print("I got these 5 random points:")  # Show list before sorting
    print(points)  # Print list using __repr__

    p = Point(3, 4)  # Create a new point to test distance
    print(p.distance_orig()) # expect 5 answer

    p2 = Point(1, 1)  # Create another point to compare
    print(f"I am comparing p > p2: {p>p2}") # I expect to have True

    print("the sorted list of points is:")  # Sorting based on distance from origin
    points.sort()
    print(points)