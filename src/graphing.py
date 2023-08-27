import os

import PIL.Image
import matplotlib
import matplotlib.pyplot as plt
import util, datetime
import widgets

GRAPH_TYPES = ["line"]

class GraphOptions:
    def __init__(self, xLabel, yLabel, xData, yData, title, size: util.ImageScale, type: str):
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.xData = xData
        self.yData = yData
        self.title = title
        self.size = size

        if not type.lower() in GRAPH_TYPES:
            self.type = None
            raise ValueError(f"Invalid type: {type.lower()}. Must be {', '.join(GRAPH_TYPES)}")
        else:
            self.type = type.lower()

class Graph:
    def __init__(self, data: GraphOptions, window):
        self.master = window
        self.data = data
        self.createdAt = datetime.datetime.now().__str__().strip().replace(":", "").replace("-", "").replace(".", "").replace(" ", "")

        try:
            self.graph = plt.figure(data.size.width)
            if self.data.type == "line":
                self.graph.suptitle(data.title)
                self.graph.add_subplot().set_xlabel(data.xLabel)
                self.graph.add_subplot().set_ylabel(data.yLabel)
                self.graph.add_subplot().plot(data.xData, data.yData)

        except Exception as e:
            print(f"Failed to create graph: {e}")

    def display(self):
        self.graph.savefig(f"{self.createdAt}.png")
        return widgets.Image(window=self.master, image=f"{self.createdAt}.png", options={"file": True, "scale": self.data.size})





