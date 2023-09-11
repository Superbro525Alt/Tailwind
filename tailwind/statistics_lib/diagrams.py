import tailwind.statistics_lib.statistics as statistics
import tailwind.bases as bases

class VenDiagram(bases.Diagram):
    def __init__(self, data):
        super().__init__(data)

        print(self.data)

    def display(self):
        return None