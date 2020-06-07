import math


class Point(object):
    def __init__(self, point_x=0, point_y=0):
        self.x_axis = point_x
        self.y_axis = point_y

    def sum(self, point_instance):
        return self.x_axis + point_instance.x_axis, self.y_axis + point_instance.y_axis

    def distance(self, point_instance):
        x_diff = self.x_axis - point_instance.x_axis
        y_diff = self.y_axis - point_instance.y_axis

        return math.sqrt(x_diff ** 2 + y_diff ** 2)


def main():
    point1 = Point(7, 9)
    point2 = Point(3, 5)
    print(point1.sum(point2))
    print(point2.distance(point1))



main()
