import os
import sys
from time import sleep

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/lib")

from tailwind.window import Window
from tailwind.widgets import *



if __name__ == "__main__":

    def onTick(_window: Window, *args, **kwargs):
        if create_git.get_value() == False:
            git_origin.show()
        else:
            git_origin.hide()
        
    props = util.WindowProperties(dynamic_scaling=True, dev_resolution=util.resolution(1920, 1080))

    window = Window(None, "Project Creator", props, False, debug=True, onTick=onTick)

    project_type = Dropdown(window, ["Python"], util.Style.empty(), {}, {})

    window.add_widget(project_type, util.PlaceData(0.3, 0.1, util.CenterAnchor().get_anchor()))

    create_git = Checkbox(window, "Create Repository", util.Style.empty(), {}, {})

    window.add_widget(create_git, util.PlaceData(0.7, 0.1, util.CenterAnchor().get_anchor()))

    git_origin = Entry(window, "Git Origin", util.Style.empty(), {}, {})

    window.add_widget(git_origin, util.PlaceData(0.5, 0.2, util.CenterAnchor().get_anchor()))

    git_origin.hide()

    window.main_loop()

