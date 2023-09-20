import os, sys

from tailwindall.web_lib import components

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from flask import Flask, make_response

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

        self.route_plain("/_tw/_style/_default.css", tw.DEFAULT_CSS, "text/css")

    def run(self, dev=True):
        if dev:
            self.app.run(port=self.port, debug=True)
        else:
            self.app.run(port=self.port)

    def route(self, path, page):
        self._routes.append((path, page))

        @self.app.route(path, endpoint=path.split("/")[-1])
        def wrapper():
            return page()

    def route_plain(self, path, page, _type="text/javascript"):
        self._routes.append((path, page))

        @self.app.route(path, endpoint=path.split("/")[-1])
        def wrapper():
            resp = make_response(page)
            resp.mimetype = _type
            return resp

class Page:
    def __init__(self, children, parent, name, stylesheet=None, _tw=None):
        self.children = children
        self.parent = parent

        self.name = name

        if stylesheet is None:
            self.stylesheet = ""

        else:
            with open(stylesheet, "r") as f:
                tw.parse(f.read(), parent)

        if _tw is None:
            self._tw = ""

        else:
            with open(_tw, "r") as f:
                tw.parse(f.read(), parent)

    def __call__(self, *args, **kwargs):
        ret = ""
        for child in self.children:
            ret += str(child)
            ret += "\n"

        ret += f'<link rel="stylesheet" href="/_tw/_style/_main.css" type="text/css">\n'
        ret += f'<script src="/_tw/_main.js" type="module"></script>'
        ret += f'<link rel="stylesheet" href="/_tw/_style/_default.css" type="text/css">\n'
        ret += f"<title>{self.name}</title>"
        return ret

class WebServer:
    def __init__(self):
        pass