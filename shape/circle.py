from math import sqrt

class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def __contains__(self, other):
        dist = sqrt((other[0]-self.centre[0]) ** 2 + (other[1]-self.centre[1]) ** 2)
        if dist<self.radius:
            return True
        return False

