import styles
import widget
import widgets

import customtkinter

import util

class Window:
    def __init__(self, style, name, options={}):
        if "file" in options:
            self.style = styles.Styles.parse(style, True)
        else:
            self.style = styles.Styles.parse(style)

        self.name = name

        self._window = customtkinter.CTk()
        self._window.title(self.name)
        self._window.geometry("500x500" if "size" not in options else options["size"])
        self._window.resizable(False if "x-resizable" not in options else options["x-resizable"], False if "y-resizeable" not in options else options["y-resizable"])

        customtkinter.set_appearance_mode(self.style["appearance_mode"] if "appearance_mode" in self.style else "system")
        if "default_color_theme" in self.style: customtkinter.set_default_color_theme(self.style["default_color_theme"])
        customtkinter.set_widget_scaling(self.style["widget_scaling"] if "widget_scaling" in self.style else 1)
        customtkinter.set_window_scaling(self.style["window_scaling"] if "window_scaling" in self.style else 1)

        self._items = []

    def main_loop(self):
        self._window.mainloop()

    def add_widget(self, widget: any, options={}):
        widget = widget._ctk
        if "place" in options:
            widget.place(relx=options["place"]["relx"], rely=options["place"]["rely"], anchor=options["place"]["anchor"])
        else:
            widget.pack()

        self._items.append(widget)

    # slotter to get when used like this: window
    def __call__(self, *args, **kwargs):
        return self._window

