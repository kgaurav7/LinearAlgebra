__author__ = 'Kumar_Garg'

from vector.vector import Vector

v1 = Vector([8.218, -9.341])
v2 = Vector([-1.129, 2.111])
print v1.plus(v2)

v3 = Vector([7.119, 8.215])
v4 = Vector([-8.223, 0.878])
print v3.minus(v4)

v5 = Vector([1.671, -1.012, -0.318])
print v5.scalar(7.41)

v6 = Vector([-0.221, 7.437])
print v6.magnitude()

v7 = Vector([8.813, -1.331, -6.247])
print v7.magnitude()

v8 = Vector([5.581, -2.136])
print v8.direction()

v9 = Vector([1.996, 3.108, -4.554])
print v9.direction()
