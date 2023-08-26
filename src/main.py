import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/lib")

import util
from window import Window
from widgets import *

if __name__ == "__main__":
    window = Window(None, "window")
    window.add_widget(Button(style={}, properties={}, binds={}, master=window()), {"place": {"relx": 0.5, "rely": 0.5, "anchor": util.NorthWestAnchor().get_anchor()}})
    window.main_loop()
