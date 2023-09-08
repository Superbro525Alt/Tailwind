import tkinter

import styles
import widget
import widgets

import customtkinter

import util

import os

import graphics_lib.graphics as graphics

class Window:
    def __init__(self, style, name, options: util.WindowProperties= util.WindowProperties.empty(), embed: bool = False):
        if options.css_file:
            self.style = styles.Styles.parse(style, True)
        else:
            self.style = styles.Styles.parse(style)

        if self.style == None:
            self.style = util.Style.empty()


        self.name = name

        self.error = False

        self._remove_on_exit = []

        self._on_exit_functions = [self.quit]

        self.options = options

        self.destroyed = False



        try:
            self._window = customtkinter.CTk()

            if embed:
                self._embeded = graphics.PygameEmbeded(self,
                                                 self.options.size if self.options.size is not None else util.resolution(
                                                     500, 500), "white")
            else:
                self._embeded = None
        except tkinter.TclError:
            print("Failed to create window. Make sure you have a display.")
            self.error = True

        if not self.error:
            self().protocol("WM_DELETE_WINDOW", lambda: util.exec_list(self._on_exit_functions, self().destroy))

            self._window.title(self.name)
            self._window.geometry("500x500" if options.size is None else options.size)
            self._window.resizable(False if options.resizable.x is None else options.resizable.x, False if options.resizable.y is None else options.resizable.y)

            customtkinter.set_appearance_mode(self.options.appearance_mode if self.options.appearance_mode is not None else "system")
            if self.options.default_color_theme is not None: customtkinter.set_default_color_theme(self.options.default_color_theme)
            customtkinter.set_widget_scaling(self.options.widget_scaling if self.options.widget_scaling is not None else 1)
            customtkinter.set_window_scaling(self.options.window_scaling if self.options.window_scaling is not None else 1)

            self._items = []

    def get_style(self):
        return self.style

    def main_loop(self):
        try:
            if not self.error:
                if self._embeded is not None:
                    self._embeded.run()
                else:
                    self._window.mainloop()
        except KeyboardInterrupt:
            self.quit()

    def add_widget(self, widget: any, placeData: util.PlaceData = None):
        if not self.error:
            if widget._widget._style == util.Style.empty():
                widget._widget._style = self.style
                widget._widget.reload_styles()
            widget_ctk = widget._ctk


            if placeData is not None:
                if util.Types.is_instance(placeData, util.PlaceData):
                    widget_ctk.place(relx=placeData.relx, rely=placeData.rely, anchor=placeData.anchor)
                else:
                    raise ValueError("Incorrect argument, placeData must be of type util.PlaceData")
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

        self.destroyed = True

    def add_on_exit_function(self, func):
        self._on_exit_functions.append(func)

    def remove_on_exit_function(self, func):
        self._on_exit_functions.remove(func)

    def add_garbage_collect_path(self, path):
        self._remove_on_exit.append(path)

    def remove_garbage_collect_path(self, path):
        self._remove_on_exit.remove(path)