import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/lib")

import util
from window import Window
from widgets import *

if __name__ == "__main__":
    window = Window("styles/style.css", "window", {"file": True})
    window.add_widget(Button(style={}, properties={"text": "Test Button"}, binds={}, master=window()), {"place": {"relx": 0.5, "rely": 0.5, "anchor": util.NorthWestAnchor().get_anchor()}})
    window.main_loop()
