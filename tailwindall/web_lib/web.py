import os, sys

from tailwindall.web_lib import components

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from flask import Flask

import tailwindall.web_lib.tw as tw

import tailwindall.util as util



class Website:
    def __init__(self, name, port, debug=False):
        self.name = name
        self.port = port
        self.debug = debug

        self.app = Flask(self.name)

        self._routes = []

        self._onTick = None

    def run(self):
        self.app.run(port=self.port)

    def route(self, path, page):
        self._routes.append((path, page))

        @self.app.route(path, endpoint=path.split("/")[-1])
        def wrapper():
            return page()


class Page:
    def __init__(self, children, stylesheet=None, _tw=None):
        self.children = children

        if stylesheet is None:
            self.stylesheet = ""

        else:
            with open(stylesheet, "r") as f:
                self.stylesheet = f.read()

        if _tw is None:
            self._tw = ""

        else:
            with open(_tw, "r") as f:
                self.tw = tw.parse(f.read())

    def __call__(self, *args, **kwargs):
        ret = ""
        for child in self.children:
            ret += str(child)
            ret += "\n"

        ret += f"<style>{self.stylesheet}</style>\n"
        ret += f"<script>{self._tw}</script>"
        return ret

class WebServer:
    def __init__(self):
        pass