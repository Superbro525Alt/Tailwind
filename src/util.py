import customtkinter, tkinter

def _is(this, other):
    return isinstance(this, other)

def read_file(file, options={}):
    # read a file and return its contents
    try:
        with open(file, "r") as f:
            if options["strip"] if "strip" in options else False:
                return f.read().strip()
            if options["lines"] if "lines" in options else False:
                return f.readlines()
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("File not found: " + file)

def _pass():
    return

class EmptyAnchor:
    def __init__(self, anchor):
        self._anchor = anchor

class CenterAnchor:
    @staticmethod
    def get_anchor():
        return tkinter.CENTER
class NorthAnchor:
    @staticmethod
    def get_anchor():
        return tkinter.N
class NorthEastAnchor:
    @staticmethod
    def get_anchor():
        return tkinter.NE
class EastAnchor:
    @staticmethod
    def get_anchor():
        return tkinter.E
class SouthEastAnchor:
    @staticmethod
    def get_anchor():
        return tkinter.SE
class SouthAnchor:
    @staticmethod
    def get_anchor():
        return tkinter.S
class WestAnchor:
    @staticmethod
    def get_anchor():
        return tkinter.W
class NorthWestAnchor:
    @staticmethod
    def get_anchor():
        return tkinter.NW