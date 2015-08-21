import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, v):
        newCoordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(newCoordinates)

    def minus(self, v):
        newCoordinates =  [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(newCoordinates)

    def scalar(self, c):
        newCoordinates =  [c * x for x in self.coordinates]
        return Vector(newCoordinates)

    def magnitude(self):
        result = [x * x for x in self.coordinates]
        return math.sqrt(sum(result))

    def direction(self):
        try:
            magnitude = self.magnitude()
            return self.scalar(1./magnitude)
        except ZeroDivisionError:
            raise ValueError('Zero Vector')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates