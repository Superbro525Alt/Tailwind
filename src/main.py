import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/lib")

import util
from window import Window

if __name__ == "__main__":
    #window = Window("""h1 {color: red;}
    #h2 {color: blue;}
    #.test {color: green;}
    #test {color: black;}""", "window")
    window = Window("styles/style.css", "window", {"file": True})
