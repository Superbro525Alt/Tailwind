import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pyglet
import tailwindall.util as util
import tailwindall.logger as logger

def init():
    paths = []
    try:
        for file in os.listdir(os.path.join(util.path(), "nerd_fonts")):
            if file.endswith(".ttf"):
                pyglet.font.add_file(os.path.join(util.path(), "nerd_fonts", file))
                paths.append(os.path.join(util.path(), "nerd_fonts", file))
    except Exception as e:
        logger.error(f"An error occurred while loading fonts: {e}")

    return paths
