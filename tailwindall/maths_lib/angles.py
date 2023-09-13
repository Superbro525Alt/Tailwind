import math, numpy as np

def angle_between_lines(line1_start, line1_end, line2_start, line2_end):
    return np.degrees(np.arccos(np.dot((line1_end - line1_start), (line2_end - line2_start)) / (
            np.linalg.norm(line1_end - line1_start) * np.linalg.norm(line2_end - line2_start))))
