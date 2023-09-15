import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from flask import Flask


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
    def __init__(self, children):
        self.children = children

    def __call__(self, *args, **kwargs):
        ret = ""
        for child in self.children:
            ret += str(child)
            ret += "\n"
        return ret

class WebServer:
    def __init__(self):
        pass