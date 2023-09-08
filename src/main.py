import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/lib")

import util
from window import Window
from widgets import *
import graphing
import statistics_lib.diagrams as diagrams

if __name__ == "__main__":
    window = Window(None, "window", util.WindowProperties.empty(), False)
    # window.add_widget(Button(style=util.Style.empty(), properties={"text": "Test Button"}, binds={}, window=window))
    # window.add_widget(Label(style=util.Style.empty(), properties={"text": "Test Label"}, binds={}, window=window))
    graph = graphing.LineGraph([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010], [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3], graphing.GraphOptions("x", "y", "title", util.ImageScale(500, 500)), window)
    window.add_widget(graph.display(), util.PlaceData(0.5, 0.5, util.CenterAnchor().get_anchor()))
    # graph2 = graphing.Graph(graphing.GraphOptions("x", "r", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "graph1", util.ImageScale(500, 500), "line"), window)
    # window.add_widget(graph2.display(), util.PlaceData(0.5, 0.5, util.CenterAnchor().get_anchor()))
    # window.main_loop()

    #diagram = diagrams.VenDiagram(util.VenDiagramData(10, 10, 25))

    window.main_loop()

