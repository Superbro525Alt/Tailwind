import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import tailwindall.classes_lib.classes as classes

class WebManager(classes.BaseObject):
    def __init__(self):
        self._INDEX = 0

    @property
    def INDEX(self):
        return self._INDEX

    @INDEX.setter
    def INDEX(self, value):
        self._INDEX = value

    def __str__(self):
        return super().__str__()

manager = WebManager()

class Button:
    def __init__(self, text, onclick, classes=[]):
        self.text = text
        self.onclick = onclick

        self.classes = classes

    def __str__(self):
        return f"""<button onclick='{self.onclick}' class='{' '.join(self.classes) if self.classes != [] else 'default-button'}'>{self.text}</button>"""

class Text:
    def __init__(self, text, classes=[]):
        self.text = text

        self.classes = classes

    def __str__(self):
        return f"""<p class='{' '.join(self.classes) if self.classes != [] else 'default-text'}'>{self.text}</p>"""

class Input:
    def __init__(self, placeholder, classes=[]):
        self.placeholder = placeholder

        self.classes = classes

        self.index = manager.INDEX
        manager.INDEX += 1


    def __str__(self):
        return f"""<input id="input-{self.index}" class='{' '.join(self.classes) if self.classes != [] else 'default-input'}' placeholder='{self.placeholder}'></input>"""

    def get_input(self):
        return f"""document.getElementById('input-{self.index}').value"""

class Image:
    def __init__(self, src, classes=[]):
        self.src = src

        self.classes = classes

    def __str__(self):
        return f"""<img class='{' '.join(self.classes) if self.classes != [] else 'default-image'}' src='{self.src}'></img>"""

class Link:
    def __init__(self, text, href, classes=[]):
        self.text = text
        self.href = href

        self.classes = classes

    def __str__(self):
        return f"""<a href='{self.href}' class='{' '.join(self.classes) if self.classes != [] else 'default-link'}'>{self.text}</a>"""

class List:
    def __init__(self, items, classes=[]):
        self.items = items

        self.classes = classes

    def __str__(self):
        ret = f"""<ul class='{' '.join(self.classes) if self.classes != [] else 'default-list'}'>"""
        for item in self.items:
            ret += f"""<li>{item}</li>"""
        ret += "</ul>"
        return ret

class Table:
    def __init__(self, headers, rows, classes=[]):
        self.headers = headers
        self.rows = rows

        self.classes = classes

    def __str__(self):
        ret = f"""<table class='{' '.join(self.classes) if self.classes != [] else 'default-table'}'>"""
        ret += "<tr>"
        for header in self.headers:
            ret += f"""<th>{header}</th>"""
        ret += "</tr>"
        for row in self.rows:
            ret += "<tr>"
            for item in row:
                ret += f"""<td>{item}</td>"""
            ret += "</tr>"
        ret += "</table>"
        return ret

class Form:
    def __init__(self, action, method, classes=[]):
        self.action = action
        self.method = method

        self.classes = classes

    def __str__(self):
        return f"""<form action='{self.action}' method='{self.method}' class='{' '.join(self.classes) if self.classes != [] else 'default-form'}'></form>"""

class Div:
    def __init__(self, children, classes=[]):
        self.children = children

        self.classes = classes

    def __str__(self):
        ret = f"""<div class='{' '.join(self.classes) if self.classes != [] else 'default-div'}'>"""
        for child in self.children:
            ret += str(child)
        ret += "</div>"
        return ret

class Span:
    def __init__(self, children, classes=[]):
        self.children = children

        self.classes = classes

    def __str__(self):
        ret = f"""<span class='{' '.join(self.classes) if self.classes != [] else 'default-span'}'>"""
        for child in self.children:
            ret += str(child)
        ret += "</span>"
        return ret

class H1:
    def __init__(self, text, classes=[]):
        self.text = text

        self.classes = classes

    def __str__(self):
        return f"""<h1 class='{' '.join(self.classes) if self.classes != [] else 'default-h1'}'>{self.text}</h1>"""

class H2:
    def __init__(self, text, classes=[]):
        self.text = text

        self.classes = classes

    def __str__(self):
        return f"""<h2 class='{' '.join(self.classes) if self.classes != [] else 'default-h2'}'>{self.text}</h2>"""

class H3:
    def __init__(self, text, classes=[]):
        self.text = text

        self.classes = classes

    def __str__(self):
        return f"""<h3 class='{' '.join(self.classes) if self.classes != [] else 'default-h3'}'>{self.text}</h3>"""

class H4:
    def __init__(self, text, classes=[]):
        self.text = text

        self.classes = classes

    def __str__(self):
        return f"""<h4 class='{' '.join(self.classes) if self.classes != [] else 'default-h4'}'>{self.text}</h4>"""

class H5:
    def __init__(self, text, classes=[]):
        self.text = text

        self.classes = classes

    def __str__(self):
        return f"""<h5 class='{' '.join(self.classes) if self.classes != [] else 'default-h5'}'>{self.text}</h5>"""

class H6:
    def __init__(self, text, classes=[]):
        self.text = text

        self.classes = classes

    def __str__(self):
        return f"""<h6 class='{' '.join(self.classes) if self.classes != [] else 'default-h6'}'>{self.text}</h6>"""

class Br:
    def __init__(self):
        pass

    def __str__(self):
        return "<br>"

