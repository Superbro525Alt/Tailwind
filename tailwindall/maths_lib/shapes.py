import math
import sys, os
from typing import Any, Tuple, List
import pygame
from numpy import ndarray

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tailwindall.util as util
import tailwindall.classes_lib.classes as classes
import tailwindall.maths_lib.angles as angles


class Shape(classes.BaseObject):
    def __init__(self, points: list, *args, **kwargs):
        self.points = points

        s = ShapeSorter.sort(self, kwargs.get("clockwise", True))

        self.points: list[float] = s[0]
        self.angles: list[float] = s[1]
        self.sides:  list[float] = s[2]

        del s

        self.name = ShapeName.find(self)

    def __str__(self) -> str:
        return super().__str__()


class ShapeName(classes.BaseObject):
    @classmethod
    def find(cls, shape: Shape) -> str:
        points = shape.points
        print(len(points))
        if len(points) == 4:
            # quadrilateral
            if shape.angles.count(90) == 4:
                return util.null
        print("No shape found")
        return util.null


class ShapeSorter(classes.BaseObject):
    @classmethod
    def sort(cls, shape: Shape, clockwise: bool = True) -> tuple[list[float], list[ndarray]]:
        """
        Sorts a shape in a clockwise direction with trigonometry.
        :param shape:
        :param clockwise:
        :return:
        """
        _angles = []
        points = sorted(shape.points, key=lambda point: angles.angle_between_lines(point, shape.points[0], (
            shape.points[0][0], shape.points[0][1] + 1), shape.points[0]), reverse=clockwise)

        for i in range(len(points)):
            try:
                _angles.append(angles.get_angle_from_lines((points[i], points[i + 1]), (points[i], points[i - 1])))
            except IndexError:
                _angles.append(angles.get_angle_from_lines((points[i], points[0]), (points[i], points[i - 1])))

        _sides: list[float] = []

        for i in range(len(points)):
            try:
                _sides.append(math.sqrt((points[i][0] - points[i + 1][0]) ** 2 + (points[i][1] - points[i + 1][1]) ** 2))
            except IndexError:
                _sides.append(math.sqrt((points[i][0] - points[0][0]) ** 2 + (points[i][1] - points[0][1]) ** 2))
        return points, _angles, _sides


def get_shape_from_points(points: list, *args, **kwargs) -> Shape:
    """
    Returns a shape from a list of points.

    :param points: The points of the shape.
    :param args: The arguments.
    :param kwargs: The keyword arguments.
    :return: A shape.
    """
    return Shape(points, args, kwargs)


if util.is_main_thread(__name__):

    pygame.init()

    screen = pygame.display.set_mode((500, 500))

    screen.fill((255, 255, 255))

    pygame.display.set_caption("Shape Sorter")

    # render a cartesian plane
    for i in range(0, 500, 100):
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 500))
        pygame.draw.line(screen, (0, 0, 0), (0, i), (500, i))


    # draw the shape on the plane
    shape = get_shape_from_points(points=[(4, 4), (1, 2), (1, 4), (4, 2)], clockwise=False)

    print(shape)

    for point in shape.points:
        pygame.draw.circle(screen, (255, 0, 0), (point[0] * 100, point[1] * 100), 5)

    # draw lines between the points
    for i in range(len(shape.points)):
        try:
            pygame.draw.line(screen, (0, 0, 255), (shape.points[i][0] * 100, shape.points[i][1] * 100),
                             (shape.points[i + 1][0] * 100, shape.points[i + 1][1] * 100))
        except IndexError:
            pygame.draw.line(screen, (0, 0, 255), (shape.points[i][0] * 100, shape.points[i][1] * 100),
                             (shape.points[0][0] * 100, shape.points[0][1] * 100))

    # show angles
    for i in range(len(shape.angles)):
        # display each angle on the corresponding point
        font = pygame.font.Font(None, 20)
        text = font.render(str(shape.angles[i]), True, (0, 0, 0))
        screen.blit(text, (shape.points[i][0] * 100 + 10, shape.points[i][1] * 100 + 10))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
