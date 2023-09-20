import math, numpy as np

def angle_between_lines(point: tuple, line1: tuple, line2: tuple, origin: tuple) -> float:
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
                              np.arctan2(line2[1] - origin[1], line2[0] - origin[0]))) % 360 - 180