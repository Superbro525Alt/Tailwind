import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/lib")

import util
from window import Window
from widgets import *
import graphing

if __name__ == "__main__":
    #window = Window(None, "window")
    #window.add_widget(Button(style={}, properties={"text": "Test Button"}, binds={}, window=window), {"place": {"relx": 0.5, "rely": 0.5, "anchor": util.NorthWestAnchor().get_anchor()}})
    #window.add_widget(Label(style={}, properties={"text": "Test Label"}, binds={}, window=window), {"place": {"relx": 0, "rely": 0, "anchor": util.WestAnchor.get_anchor()}})
    #graph = graphing.Graph(graphing.GraphOptions("x", "y", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "graph", util.ImageScale(500, 500), "line"), window)
    #window.add_widget(graph.display(), {"place": {"relx": 0.5, "rely": 0.5, "anchor": util.CenterAnchor().get_anchor()}})
    #graph2 = graphing.Graph(graphing.GraphOptions("x", "r", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "graph1", util.ImageScale(500, 500), "line"), window)
    #window.add_widget(graph2.display(), {"place": {"relx": 0, "rely": 0.5, "anchor": util.CenterAnchor().get_anchor()}})
    #window.main_loop()
    pass


