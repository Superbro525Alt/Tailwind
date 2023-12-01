import sys
import os


parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(parent_dir)))
sys.path.append(parent_dir)

import tailwindall.graphics_lib.graphics as graphics
import tailwindall.util as util
from tailwindall.graphics_lib import objects

win = graphics.PlatformerWindow("Test", util.resolution(800, 600), "white")

win.add_object(objects.Rectangle("blue", (50, 50), (50, 50), setup=True), True)

win.main_loop()
