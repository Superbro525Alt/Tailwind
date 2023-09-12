import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import tailwindall.bases as bases

class VenDiagram(bases.Diagram):
    def __init__(self, data):
        super().__init__(data)

        print(self.data)

    def display(self):
        return None