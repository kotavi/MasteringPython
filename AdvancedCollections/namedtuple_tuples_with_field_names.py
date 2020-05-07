from collections import namedtuple

Point = namedtuple("Points", ['x', 'y', 'z'])
point_a = Point(1, 2, 3)
print(point_a)
point_b = Point(4, 5, 6)
print(point_b)
