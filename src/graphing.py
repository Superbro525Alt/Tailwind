import PIL.Image
import matplotlib
import matplotlib.pyplot as plt
import util, tkinter, customtkinter
import widgets
from PIL import Image, ImageTk

class GraphOptions:
    def __init__(self, xLabel, yLabel, xData, yData, title, size):
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.xData = xData
        self.yData = yData
        self.title = title
        self.size = size

class Graph:
    def __init__(self, data: GraphOptions, master):
        self.master = master
        try:
            self.graph = plt.figure(data.size)
            self.graph.suptitle(data.title)
            self.graph.add_subplot().set_xlabel(data.xLabel)
            self.graph.add_subplot().set_ylabel(data.yLabel)
            self.graph.add_subplot().plot(data.xData, data.yData)
        except Exception as e:
            print(f"Failed to create graph: {e}")

    def display(self):
        self.graph.savefig("graph.png")
        img = customtkinter.CTkImage(PIL.Image.open("graph.png"))
        return widgets.Image(master=self.master, image=img)



