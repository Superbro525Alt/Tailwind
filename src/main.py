import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/lib")

from window import Window
from widgets import *

def onTick(_window : Window, *args, **kwargs):
    print("Tick")

if __name__ == "__main__":
    props = util.WindowProperties(dynamic_scaling=True, dev_resolution=util.resolution(1920, 1080))

    window = Window(None, "Project Creator", props, False, debug=True)

    project_type = Dropdown(window, ["Python"], util.Style.empty(), {}, {})

    window.add_widget(project_type, util.PlaceData(0.5, 0.1, util.CenterAnchor().get_anchor()))

    git_origin = Entry(window, "Git Origin", util.Style.empty(), {}, {})

    window.add_widget(git_origin, util.PlaceData(0.5, 0.2, util.CenterAnchor().get_anchor()))

    window.main_loop()

