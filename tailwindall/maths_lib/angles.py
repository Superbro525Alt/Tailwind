import math, numpy as np

from numpy import ndarray


def angle_between_lines(point: tuple, line1: tuple, line2: tuple, origin: tuple) -> ndarray:
    """
    Returns the angle between two lines.
    :param point:
    :param line1:
    :param line2:
    :param origin:
    :return:
    """
    return np.degrees(np.arctan2(point[1] - origin[1], point[0] - origin[0]) - np.arctan2(line1[1] - origin[1],
                                                                                          line1[0] - origin[0]) - (
                              np.arctan2(line2[1] - origin[1], line2[0] - origin[0]) - np.arctan2(
                          point[1] - origin[1], point[0] - origin[0])))


def get_angle_from_lines(line1: tuple[tuple[float, float], tuple[float, float]],
                         line2: tuple[tuple[float, float], tuple[float, float]]) -> float:
    """
    Returns the angle between two lines.
    :param line1: -> tuple[tuple[float, float], tuple[float, float]]
    :param line2: -> tuple[tuple[float, float], tuple[float, float]]
    :return:
    """

    return abs(math.degrees(math.atan2(line2[1][1] - line2[0][1], line2[1][0] - line2[0][0]) - math.atan2(
        line1[1][1] - line1[0][1], line1[1][0] - line1[0][0])) % 360 - 360)
