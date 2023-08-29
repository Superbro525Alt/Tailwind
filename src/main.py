import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/lib")

import util
from window import Window
from widgets import *
import graphing
import statistics

if __name__ == "__main__":
    print(statistics.standard_deviation([1, 2, 3, 4, 5]))
    #window = Window(None, "window", util.WindowProperties.empty())
    #window.add_widget(Button(style=util.Style.empty(), properties={"text": "Test Button"}, binds={}, window=window))
    #window.add_widget(Label(style=util.Style.empty(), properties={"text": "Test Label"}, binds={}, window=window))
    #graph = graphing.Graph(graphing.GraphOptions("x", "y", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "graph", util.ImageScale(500, 500), "line"), window)
    #window.add_widget(graph.display(), util.PlaceData(0.5, 0.5, util.CenterAnchor().get_anchor()))
    #graph2 = graphing.Graph(graphing.GraphOptions("x", "r", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "graph1", util.ImageScale(500, 500), "line"), window)
    #window.add_widget(graph2.display(), util.PlaceData(0.5, 0.5, util.CenterAnchor().get_anchor()))
    #window.main_loop()

