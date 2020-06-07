import math


class Point(object):
    def __init__(self, point_x=0.0, point_y=0.0):
        """Create x and y attributes. Defaults are 0.0"""
        self.x_axis = point_x
        self.y_axis = point_y

    def sum(self, point_instance):
        """Vector sum of self and a Point return a Point instance"""
        new_point = self.x_axis + point_instance.x_axis, self.y_axis + point_instance.y_axis
        return new_point

    def distance(self, point_instance):
        """Distance between self and a Point"""
        x_diff = self.x_axis - point_instance.x_axis
        y_diff = self.y_axis - point_instance.y_axis

        return math.sqrt(x_diff ** 2 + y_diff ** 2)

    def __str__(self):
        return "x axis: {:.2f} \ny axis: {:.2f} ".format(self.x_axis, self.y_axis)


def main():
    point1 = Point(7, 9)
    point2 = Point(3, 5)
    print(point1)
    print("sum: {}".format(point1.sum(point2)))
    print("distance: {:.2f}".format(point2.distance(point1)))


main()
