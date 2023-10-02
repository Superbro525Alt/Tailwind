import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pyglet
import tailwindall.util as util

def init():
    paths = []
    for file in os.listdir(os.path.join(util.path(), "nerd_fonts")):
        if file.endswith(".ttf"):
            pyglet.font.add_file(os.path.join(util.path(), "nerd_fonts", file))
            paths.append(os.path.join(util.path(), "nerd_fonts", file))

    return paths
