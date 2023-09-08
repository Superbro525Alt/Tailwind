import statistics
import bases

class VenDiagram(bases.Diagram):
    def __init__(self, data):
        super().__init__(data)

        print(self.data)

    def display(self):
        return None