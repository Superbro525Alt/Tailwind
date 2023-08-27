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

class ImageScale:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __call__(self, *args, **kwargs):
        return self.width, self.height