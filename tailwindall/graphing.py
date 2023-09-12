

import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import PIL.Image
import matplotlib
import matplotlib.pyplot as plt
import tailwindall.util as util, datetime
import tailwindall.widgets as widgets

GRAPH_TYPES = ["line", "bar", "scatter"]

class GraphOptions:
    def __init__(self, xLabel, yLabel, title, size: util.ImageScale):
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.title = title
        self.size = size

class Graph:
    def display(self):
        self.graph.savefig(f"{self.createdAt}.png")
        return widgets.Image(window=self.master, image=f"{self.createdAt}.png", options={"file": True, "scale": self.options.size})

class LineGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
        self.master = window
        self.options = options
        self.xData = xData
        self.yData = yData
        self.createdAt = datetime.datetime.now().__str__().strip().replace(":", "").replace("-", "").replace(".", "").replace(" ", "")

        try:
            self.graph = plt.figure(options.size.width)
            # make a line graph
            plt.plot(self.xData, self.yData)
            plt.xlabel(self.options.xLabel)
            plt.ylabel(self.options.yLabel)
            plt.title(self.options.title)



        except Exception as e:
            print(f"Failed to create graph: {e}")


class BarGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
        self.master = window
        self.options = options
        self.xData = xData
        self.yData = yData
        self.createdAt = datetime.datetime.now().__str__().strip().replace(":", "").replace("-", "").replace(".", "").replace(" ", "")

        try:
            self.graph = plt.figure(options.size.width)
            # make a line graph
            plt.bar(self.xData, self.yData)
            plt.xlabel(self.options.xLabel)
            plt.ylabel(self.options.yLabel)
            plt.title(self.options.title)

        except Exception as e:
            print(f"Failed to create graph: {e}")

class ScatterGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
        self.master = window
        self.options = options
        self.xData = xData
        self.yData = yData
        self.createdAt = datetime.datetime.now().__str__().strip().replace(":", "").replace("-", "").replace(".", "").replace(" ", "")

        try:
            self.graph = plt.figure(options.size.width)
            # make a line graph
            plt.scatter(self.xData, self.yData)
            plt.xlabel(self.options.xLabel)
            plt.ylabel(self.options.yLabel)
            plt.title(self.options.title)

        except Exception as e:
            print(f"Failed to create graph: {e}")

class PieGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
        self.master = window
        self.options = options
        self.xData = xData
        self.yData = yData
        self.createdAt = datetime.datetime.now().__str__().strip().replace(":", "").replace("-", "").replace(".", "").replace(" ", "")

        try:
            self.graph = plt.figure(options.size.width)
            # make a line graph
            plt.pie(self.xData, labels=self.yData)
            plt.xlabel(self.options.xLabel)
            plt.ylabel(self.options.yLabel)
            plt.title(self.options.title)

        except Exception as e:
            print(f"Failed to create graph: {e}")

class HistogramGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
        self.master = window
        self.options = options
        self.xData = xData
        self.yData = yData
        self.createdAt = datetime.datetime.now().__str__().strip().replace(":", "").replace("-", "").replace(".", "").replace(" ", "")

        try:
            self.graph = plt.figure(options.size.width)
            # make a line graph
            plt.hist(self.xData, yData)
            plt.xlabel(self.options.xLabel)
            plt.ylabel(self.options.yLabel)
            plt.title(self.options.title)

        except Exception as e:
            print(f"Failed to create graph: {e}")

class BoxPlotGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
        self.master = window
        self.options = options
        self.xData = xData
        self.yData = yData
        self.createdAt = datetime.datetime.now().__str__().strip().replace(":", "").replace("-", "").replace(".", "").replace(" ", "")

        try:
            self.graph = plt.figure(options.size.width)
            # make a line graph
            plt.boxplot(self.xData, yData)
            plt.xlabel(self.options.xLabel)
            plt.ylabel(self.options.yLabel)
            plt.title(self.options.title)

        except Exception as e:
            print(f"Failed to create graph: {e}")

class AreaGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
        self.master = window
        self.options = options
        self.xData = xData
        self.yData = yData
        self.createdAt = datetime.datetime.now().__str__().strip().replace(":", "").replace("-", "").replace(".", "").replace(" ", "")

        try:
            self.graph = plt.figure(options.size.width)
            # make a line graph
            plt.stackplot(self.xData, yData)
            plt.xlabel(self.options.xLabel)
            plt.ylabel(self.options.yLabel)
            plt.title(self.options.title)

        except Exception as e:
            print(f"Failed to create graph: {e}")