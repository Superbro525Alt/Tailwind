import tkinter

import styles
import widget
import widgets

import customtkinter

import util

import os

class Window:
    def __init__(self, style, name, options={}):
        if "file" in options:
            self.style = styles.Styles.parse(style, True)
        else:
            self.style = styles.Styles.parse(style)

        if self.style == None:
            self.style = {"classes": {}, "ids": {}, "tags": {}}


        self.name = name

        self.error = False

        self._remove_on_exit = []

        self._on_exit_functions = [self.quit]




        try:
            self._window = customtkinter.CTk()
        except tkinter.TclError:
            print("Failed to create window. Make sure you have a display.")
            self.error = True

        if not self.error:
            self().protocol("WM_DELETE_WINDOW", util.exec_list(self._on_exit_functions))

            self._window.title(self.name)
            self._window.geometry("500x500" if "size" not in options else options["size"])
            self._window.resizable(False if "x-resizable" not in options else options["x-resizable"], False if "y-resizeable" not in options else options["y-resizable"])

            customtkinter.set_appearance_mode(self.style["appearance_mode"] if "appearance_mode" in self.style else "system")
            if "default_color_theme" in self.style: customtkinter.set_default_color_theme(self.style["default_color_theme"])
            customtkinter.set_widget_scaling(self.style["widget_scaling"] if "widget_scaling" in self.style else 1)
            customtkinter.set_window_scaling(self.style["window_scaling"] if "window_scaling" in self.style else 1)

            self._items = []

    def main_loop(self):
        if not self.error:
            self._window.mainloop()

    def add_widget(self, widget: any, options={}):
        if not self.error:
            widget_ctk = widget._ctk
            if "place" in options:
                widget_ctk.place(relx=options["place"]["relx"], rely=options["place"]["rely"], anchor=options["place"]["anchor"])
            else:
                widget_ctk.pack()

            self._items.append(widget)

    # slotter to get when used like this: window
    def __call__(self, *args, **kwargs):
        if not self.error:
            return self._window
        else:
            return None

    def quit(self):
        [os.remove(path) for path in self._remove_on_exit]

    def add_on_exit_function(self, func):
        self._on_exit_functions.append(func)

    def remove_on_exit_function(self, func):
        self._on_exit_functions.remove(func)

    def add_garbage_collect_path(self, path):
        self._remove_on_exit.append(path)

    def remove_garbage_collect_path(self, path):
        self._remove_on_exit.remove(path)