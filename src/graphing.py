import PIL.Image
import matplotlib
import matplotlib.pyplot as plt
import util, tkinter, customtkinter
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
            self.type = type

class Graph:
    def __init__(self, data: GraphOptions, master):
        self.master = master
        self.data = data
        try:
            self.graph = plt.figure(data.size.width)
            self.graph.suptitle(data.title)
            self.graph.add_subplot().set_xlabel(data.xLabel)
            self.graph.add_subplot().set_ylabel(data.yLabel)
            self.graph.add_subplot().plot(data.xData, data.yData)
        except Exception as e:
            print(f"Failed to create graph: {e}")

    def display(self):
        self.graph.savefig("graph.png")
        return widgets.Image(master=self.master, image="graph.png", options={"file": True, "scale": self.data.size})



