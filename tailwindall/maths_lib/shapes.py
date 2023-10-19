import math
import sys, os
import random
import threading
from time import sleep
from typing import Any, Tuple, List
import pygame
from numpy import ndarray

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tailwindall.util as util
import tailwindall.classes_lib.classes as classes
import tailwindall.maths_lib.angles as angles
import tailwindall.maths_lib.lines as lines
import tailwindall.popup as popup

class Shape(classes.BaseObject):
    def __init__(self, points: list, rules: classes.Rules = None, *args, **kwargs):
        self.points = points

        self.kwargs = kwargs

        [self.calculate() for _ in range(5)]



        self.name, self.proofs = ShapeName.find(self, rules)

        self.rules = rules

    def calculate(self) -> None:
        s = ShapeSorter.sort(self, self.kwargs.get("clockwise", True))

        self.points: list[float] = s[0]
        self.angles: list[float] = s[1]
        self.sides: list[float] = s[2]

        del s

    def __str__(self) -> str:
        return super().__str__()

    def data(self):
        #print(self.proofs, self.name)
        return f"""{self.rules.get_text(self.proofs)}""", f"Shape - {self.name} - Proofs:"


class ShapeName(classes.BaseObject):
    @classmethod
    def find(cls, shape: Shape, rules: classes.Rules = None) -> tuple[str, list[int]]:
        points = shape.points
        if rules is not None:

            PROOFS: list[dict[str: int, str: str] | None] = []

            # if parallel sides

            print(shape.angles)
            if shape.angles[0] == shape.angles[2] and shape.angles[1] == shape.angles[3]:
                PROOFS.append({"id": 1, "data": "AB, CD"})
            elif shape.angles[0] == shape.angles[1] and shape.angles[2] == shape.angles[3]:
                PROOFS.append({"id": 1, "data": "BA, CD"})
            elif shape.angles[0] == shape.angles[3] and shape.angles[1] == shape.angles[2]:
                PROOFS.append({"id": 1, "data": "DA, BC"})
            elif shape.angles[0] == shape.angles[1] and shape.angles[2] == shape.angles[3]:
                PROOFS.append({"id": 1, "data": "AB, CD"})



            # if 2 pairs of parallel sides
            if shape.angles[0] == shape.angles[2] and shape.angles[1] == shape.angles[3]:
                PROOFS.append({"id": 2, "data": "AB, BC, CD, DA"})
            elif shape.angles[0] == shape.angles[1] and shape.angles[2] == shape.angles[3]:
                PROOFS.append({"id": 2, "data": "AB, BC, CD, DA"})




            # if all sides are equal
            if shape.sides.count(shape.sides[0]) == 4:
                PROOFS.append({"id": 3, "data": f"AB, BC, CD, DA = {shape.sides[0]}"})

            # if all angles 90
            if shape.angles.count(90) == 4:
                PROOFS.append({"id": 4, "data": "ABC, BCD, CDA, DAB = 90"})

            # if 2 of adjacent equal sides
            if shape.sides[0] == shape.sides[1] and shape.sides[2] == shape.sides[3]:
                PROOFS.append({"id": 5, "data": "AB = BC and CD = DA"})
            elif shape.sides[0] == shape.sides[3] and shape.sides[1] == shape.sides[2]:
                PROOFS.append({"id": 5, "data": "AB = DA and BC = CD"})
            elif shape.sides.count(shape.sides[0]) == 4:
                PROOFS.append({"id": 5, "data": "AB = BC and CD = DA"})

            try:
                # if diagonals intersect on another at 90
                # 1. get the 2 points of each diagonal
                diagonal1 = [shape.points[0], shape.points[2]]
                diagonal2 = [shape.points[1], shape.points[3]]

                # 2. get the midpoint of each diagonal
                midpoint1 = ((diagonal1[0][0] + diagonal1[1][0]) / 2, (diagonal1[0][1] + diagonal1[1][1]) / 2)
                midpoint2 = ((diagonal2[0][0] + diagonal2[1][0]) / 2, (diagonal2[0][1] + diagonal2[1][1]) / 2)



                # if diagonals are perpendicular
                if angles.get_angle_from_lines((shape.points[0], shape.points[2]), (shape.points[1], shape.points[3])) == 90:
                    PROOFS.append({"id": 6, "data": "AC, BD"})
                elif angles.get_angle_from_lines((shape.points[1], shape.points[3]), (shape.points[0], shape.points[2])) == 90:
                    PROOFS.append({"id": 6, "data": "AC, BD"})



                # if one diagonal bicects the other
                intersection_point = lines.line_intersection(diagonal1, diagonal2)
                if intersection_point[0] == 'lines do not intersect':
                    raise ZeroDivisionError

                if intersection_point == midpoint1 or intersection_point == midpoint2:
                    PROOFS.append({"id": 7, "data": "AC, BD"})

                if intersection_point == midpoint1 and intersection_point == midpoint2:
                    PROOFS.append({"id": 8, "data": "AC, BD"})

                # if one diagonals line intersects the mid point of the other diagonal
                # we already have all of tje required variables from the previous proof
                # if distance1 == 0:
                #     if midpoint2[0] == point_of_intersection[0] and midpoint2[1] == point_of_intersection[1]:
                #         PROOFS.append({"id": 7, "data": "AC, BD"})
                # elif distance2 == 0:
                #     if midpoint1[0] == point_of_intersection[0] and midpoint1[1] == point_of_intersection[1]:
                #         PROOFS.append({"id": 7, "data": "AC, BD"})
                #
                #
                # # if both diagonals bisect each other
                # if distance1 == 0 and distance2 == 0:
                #     if midpoint1[0] == point_of_intersection[0] and midpoint1[1] == point_of_intersection[1]:
                #         if midpoint2[0] == point_of_intersection[0] and midpoint2[1] == point_of_intersection[1]:
                #             PROOFS.append({"id": 8, "data": "AC, BD"})

            except ZeroDivisionError:
                popup.ErrorBox("Error", "Its a line...")

            print(angles.get_angle_from_lines((shape.points[1], shape.points[3]), (shape.points[1], shape.points[2])), angles.get_angle_from_lines((shape.points[1], shape.points[3]), (shape.points[1], shape.points[0])))
            if angles.get_angle_from_lines((shape.points[0], shape.points[2]), (shape.points[0], shape.points[3])) == angles.get_angle_from_lines((shape.points[0], shape.points[1]), (shape.points[0], shape.points[2])):
                PROOFS.append({"id": 9, "data": "AC, BD"})
            elif angles.get_angle_from_lines((shape.points[1], shape.points[2]), (shape.points[1], shape.points[3])) == angles.get_angle_from_lines((shape.points[1], shape.points[3]), (shape.points[1], shape.points[0])):
                PROOFS.append({"id": 9, "data": "AC, BD"})

            if angles.get_angle_from_lines((shape.points[0], shape.points[2]), (shape.points[0], shape.points[3])) == angles.get_angle_from_lines((shape.points[0], shape.points[1]), (shape.points[0], shape.points[2])) and angles.get_angle_from_lines((shape.points[1], shape.points[2]), (shape.points[1], shape.points[3])) == angles.get_angle_from_lines((shape.points[1], shape.points[3]), (shape.points[1], shape.points[0])):
                PROOFS.append({"id": 10, "data": "AC, BD"})

            if lines.length((shape.points[0], shape.points[2])) == lines.length((shape.points[1], shape.points[3])):
                PROOFS.append({"id": 11, "data": "AC = BD"})
            # find if one diagonal bisects the vertex angles through which it passes.
            # # to do this, we need to find the vertex angles
            # vertex_angles = []
            # for i in range(len(shape.angles)):
            #     try:
            #         vertex_angles.append(shape.angles[i] + shape.angles[i + 1])
            #     except IndexError:
            #         vertex_angles.append(shape.angles[i] + shape.angles[0])
            #
            # # if one diagonal bisects the vertex angles through which it passes
            # midpoint_AC = ((shape.points[0][0] + shape.points[2][0]) / 2, (shape.points[0][1] + shape.points[2][1]) / 2)
            # midpoint_BD = ((shape.points[1][0] + shape.points[3][0]) / 2, (shape.points[1][1] + shape.points[3][1]) / 2)
            #
            # if angles.does_diagonal_bisect(midpoint_AC, diagonal1) or angles.does_diagonal_bisect(midpoint_BD, diagonal2):
            #     PROOFS.append({"id": 9, "data": "AC, BD"})
            #
            # # Both diagonals bisect the vertex angles through which they pass
            # if angles.does_diagonal_bisect(midpoint_AC, diagonal1) and angles.does_diagonal_bisect(midpoint_BD, diagonal2):
            #     PROOFS.append({"id": 10, "data": "AC, BD"})
            #
            # # Diagonals are equal in length
            # if shape.sides[0] == shape.sides[2] and shape.sides[1] == shape.sides[3]:
            #     PROOFS.append({"id": 11, "data": "AC = BD"})

            out = rules.get_result(PROOFS)
            if out is not None:
                return out, PROOFS
            print("No shape found")
            return util.null, PROOFS
        else:
            #print("No rules found")
            return util.null, []


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
        #points = sorted(shape.points, key=lambda point: angles.angle_between_lines(point, shape.points[0], (
        #    shape.points[0][0], shape.points[0][1] + 1), shape.points[0]), reverse=clockwise)

        points = sorted(shape.points, key=lambda point: angles.get_angle_from_lines((point, shape.points[0]), (point, (point[0], point[1] + 1))), reverse=clockwise)

        for i in range(len(points)):
            try:
                _angles.append(round(angles.get_angle_from_lines((points[i], points[i + 1]), (points[i], points[i - 1])), 2))
            except IndexError:
                _angles.append(round(angles.get_angle_from_lines((points[i], points[0]), (points[i], points[i - 1])), 2))

        _sides: list[float] = []

        for i in range(len(points)):
            try:
                _sides.append(round(math.sqrt((points[i][0] - points[i + 1][0]) ** 2 + (points[i][1] - points[i + 1][1]) ** 2), 2))
            except IndexError:
                _sides.append(round(math.sqrt((points[i][0] - points[0][0]) ** 2 + (points[i][1] - points[0][1]) ** 2), 2))

        return points, _angles, _sides

def get_random_point(current_points: list[tuple[float, float]]) -> tuple[float, float]:
    """
    Returns a random point.
    :param current_points: The current points.

    :return: A random point.
    """
    point = random.randint(1, 4), random.randint(1, 4)
    if point in current_points:
        return get_random_point(current_points)
    else:
        return point

def get_shape_from_points(points: list, rules: classes.Rules = None, *args, **kwargs) -> Shape:
    """
    Returns a shape from a list of points.

    :param points: The points of the shape.
    :param args: The arguments.
    :param kwargs: The keyword arguments.
    :return: A shape.
    """
    if points == []:
        points = []
        for i in range(4):
            # get a point with get_random_point until it is not in the list
            p = get_random_point(points)

            points.append(p)
    return Shape(points, rules, args, kwargs)

if util.is_main_thread(__name__):
    constants = classes.Constants({"CARTESIAN_PLANE_SIZE": 1000, "CARTESIAN_PLANE_GAP": 50})
    rules = classes.Rules({
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11): "Square",
        (1, 2, 3, 5, 6, 7, 8, 9, 10): "Rhombus",
        (1, 2, 4, 7, 8, 9, 10, 11): "Rectangle",
        (1, 2, 7, 8): "Parallelogram",
        (5, 6, 7, 9): "Kite",
        (1): "Trapezium"
    })
    pygame.init()

    screen = pygame.display.set_mode((500, 500))

    screen.fill((255, 255, 255))

    pygame.display.set_caption("Maths CAT Investigation")

    #shape = get_shape_from_points(points=[], clockwise=False)
    shape = get_shape_from_points(points=[(2, 2), (2, 4), (5, 2), (5, 4)], clockwise=False)

    def get_new_shape():
        global shape
        shape = get_shape_from_points(points=[], clockwise=False)
        sleep(5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        try:  # render a cartesian plane
            for i in range(0, int(constants.get_value("CARTESIAN_PLANE_SIZE")), int(constants.get_value("CARTESIAN_PLANE_GAP"))):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, constants.get_value("CARTESIAN_PLANE_SIZE")))
                pygame.draw.line(screen, (0, 0, 0), (0, i), (constants.get_value("CARTESIAN_PLANE_SIZE"), i))

            # draw the shape on the plane# shape = get_shape_from_points(points = [(1, 1), (2, 1), (2, 2), (1, 2)], clockwise = False)


            # draw lines between the points
            for i in range(len(shape.points)):
                try:
                    pygame.draw.line(screen, (0, 0, 255), (shape.points[i][0] * constants.get_value("CARTESIAN_PLANE_GAP"), shape.points[i][1] * constants.get_value("CARTESIAN_PLANE_GAP")),
                                     (shape.points[i + 1][0] * constants.get_value("CARTESIAN_PLANE_GAP"), shape.points[i + 1][1] * constants.get_value("CARTESIAN_PLANE_GAP")), 10)
                except IndexError:
                    pygame.draw.line(screen, (0, 0, 255), (shape.points[i][0] * constants.get_value("CARTESIAN_PLANE_GAP"), shape.points[i][1] * constants.get_value("CARTESIAN_PLANE_GAP")),
                                     (shape.points[0][0] * constants.get_value("CARTESIAN_PLANE_GAP"), shape.points[0][1] * constants.get_value("CARTESIAN_PLANE_GAP")), 10)

            for point in shape.points:
                pygame.draw.circle(screen, (255, 0, 0), (point[0] * constants.get_value("CARTESIAN_PLANE_GAP"), point[1] * constants.get_value("CARTESIAN_PLANE_GAP")), 10)

            # show angles
            for i in range(len(shape.angles)):  # display each angle on the corresponding point
                font = pygame.font.Font(None, 20)
                text = font.render(str(shape.angles[i]), True, (0, 0, 0))
                screen.blit(text, (shape.points[i][0] * constants.get_value("CARTESIAN_PLANE_GAP") + 10, shape.points[i][1] * constants.get_value("CARTESIAN_PLANE_GAP") + 10))

            # show sides
            for i in range(len(shape.sides)):  # display each angle on the corresponding side in the center
                font = pygame.font.Font(None, 20)
                text = font.render(str(shape.sides[i]), True, (0, 0, 0))
                try:
                    screen.blit(text, ((shape.points[i][0] * constants.get_value("CARTESIAN_PLANE_GAP") + shape.points[i + 1][0] * constants.get_value("CARTESIAN_PLANE_GAP")) / 2,
                                       (shape.points[i][1] * constants.get_value("CARTESIAN_PLANE_GAP") + shape.points[i + 1][1] * constants.get_value("CARTESIAN_PLANE_GAP")) / 2))
                except IndexError:
                    screen.blit(text, ((shape.points[i][0] * constants.get_value("CARTESIAN_PLANE_GAP") + shape.points[0][0] * constants.get_value("CARTESIAN_PLANE_GAP")) / 2,
                                       (shape.points[i][1] * constants.get_value("CARTESIAN_PLANE_GAP") + shape.points[0][1] * constants.get_value("CARTESIAN_PLANE_GAP")) / 2))

            # display the name of the shape at the top of the screen

            font = pygame.font.Font(None, 50)
            text = font.render(shape.name if shape.name is not None else "None", True, (0, 0, 0))
            screen.blit(text, (0, 0))

            pygame.display.update()
        except Exception as e:
            raise e

        t = threading.Thread(target=get_new_shape, daemon=True)
        t.start()
        t.join()
