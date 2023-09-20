import sys, os

import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tailwindall.util as util
import tailwindall.classes_lib.classes as classes
import tailwindall.maths_lib.angles as angles



class Shape(classes.BaseObject):
    def __init__(self, points: list):
        self.points = points

        self.points = ShapeSorter.sort(self)

        self.name = ShapeName.find(self)

    def __str__(self) -> str:
        return super().__str__()

class ShapeName(classes.BaseObject):
    @classmethod
    def find(cls, shape: Shape) -> str:
        points = shape.points

        return util.null

class ShapeSorter(classes.BaseObject):
    @classmethod
    def sort(cls, shape: Shape) -> list:
        """
        Sorts a shape in a clockwise direction with trigonometry.
        :param shape:
        :return:
        """
        return sorted(shape.points, key=lambda point: angles.angle_between_lines(point, shape.points[0], (
        shape.points[0][0], shape.points[0][1] + 1), shape.points[0]))



def get_shape_from_points(points: list) -> Shape:
    """
    Returns a shape from a list of points.
    """
    return Shape(points)


if util.is_main_thread(__name__):
    print(get_shape_from_points([(0, 0), (1, 0), (1, 1), (0, 1)]))
