from typing import overload

import customtkinter, tkinter

NULL = None
null = NULL

class Types:
    @classmethod
    def are_list_items_same(cls, this: list, other: list):
        ret = []
        if len(this) != len(other):
            raise ValueError(f"Lists are not the same length: This -> {len(this)} & Other -> {len(other)}")
        for i in range(len(this)):
            if cls.is_type(this[i], other[i]):
                ret.append(True)
            else:
                ret.append(False)

        return ret

    @classmethod
    def is_class_same(cls, this: object, other: object):
        ret = {}
        for key in list(this.__dict__.keys()):
            if hasattr(other, key):
                if other.__dict__[key] == this.__dict__[key]:
                    ret[key] = True
                else:
                    ret[key] = False
            else:
                ret[key] = null

        return ret


    @classmethod
    def is_type(cls, this, other):
        return type(this) == type(other)

    @classmethod
    def is_instance(cls, this, other):
        return isinstance(this, other)

    @classmethod
    def widget_type(cls, this):
        if this == customtkinter.CTkButton:
            return "button"
        elif this == customtkinter.CTkLabel:
            return "label"
        elif this == customtkinter.CTkEntry:
            return "entry"
        elif this == customtkinter.CTkFrame:
            return "frame"
        elif this == customtkinter.CTkCanvas:
            return "canvas"
        elif this == customtkinter.CTk:
            return "window"
        else:
            return "unknown"



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

class ImageScale:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __call__(self, *args, **kwargs):
        return self.width, self.height


def exec_list(functions, final=None):
    for func in functions:
        func()

    if final is not None:
        final()

class Style:
    def __init__(self, classes, tags, ids):
        self.classes = classes
        self.tags = tags
        self.ids = ids

    @classmethod
    def empty(cls):
        return cls({}, {}, {})

class Resizable:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    @classmethod
    def empty(cls):
        return cls()
class WindowProperties:
    def __init__(self, size=None, resizable=Resizable.empty(), appearance_mode=None, default_color_theme=None, widget_scaling=None, window_scaling=None, css_file=None):
        self.size = size
        self.resizable = resizable
        self.appearance_mode = appearance_mode
        self.default_color_theme = default_color_theme
        self.widget_scaling = widget_scaling
        self.window_scaling = window_scaling
        self.css_file = css_file

    @classmethod
    def empty(cls):
        return cls()

class PlaceData:
    def __init__(self, relx: float, rely: float, anchor: EmptyAnchor):
        self.relx = relx
        self.rely = rely
        self.anchor = anchor

def is_main_thread(name):
    return name == "__main__"

def run_tests(tests):
    print("Testing...")
    passed = 0
    for i in range(len(tests)):
        try:
            print(f"Tests: {i+1}. Passed: {passed}. Running Test {i + 1}...")
            tests[i]()
            passed += 1
        except Exception as e:
            print(f"Test {i + 1} failed: {e}")

    print("===============================")
    print(f"Tests: {i+1}. Passed: {passed}.")
    print("===============================")


    if i + 1 == passed:
        print("All tests passed!")
    else:
        if i + 1 - passed == 1:
            print(f"{i + 1 - passed} test failed.")
        else:
            print(f"{i + 1 - passed} tests failed.")
