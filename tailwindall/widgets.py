import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import os
import tkinter

from PIL import ImageTk

import tailwindall.widget as widget

import customtkinter

import PIL

import tailwindall.util as util


class Button():
    def __init__(self, window, command, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkButton(master=window(), command=command, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            self.window = window
        except tkinter.TclError:
            print("Failed to create button. Make sure you have a display.")
            self._ctk = None
            self._widget = None

    def hide(self):
        if self._ctk is not None:
            self._ctk.place_forget()

    def show(self):
        if self._ctk is not None:
            self.window.reinstate_widget(self)

class Dropdown:
    def __init__(self, window, options, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:

            self._ctk = customtkinter.CTkComboBox(window(), values=options, **kwargs)
            self._ctk.configure(state="readonly")
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            self.window = window

        except tkinter.TclError as e:
            print(f"Failed to create dropdown. Make sure you have a display. {e}")
            self._ctk = None
            self._widget = None

    def get_value(self):
        return self._ctk.get()

    def hide(self):
        if self._ctk is not None:
            self._ctk.place_forget()

    def show(self):
        if self._ctk is not None:
            self.window.reinstate_widget(self)

class Label():
    def __init__(self, window, text, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkLabel(window(), text=text, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            self.window = window

        except tkinter.TclError as e:
            print(f"Failed to create label. Make sure you have a display. {e}")
            self._ctk = None
            self._widget = None

    def hide(self):
        if self._ctk is not None:
            self._ctk.place_forget()

    def show(self):
        if self._ctk is not None:
            self.window.reinstate_widget(self)

    def set_text(self, text):
        self._ctk.configure(text=text)

class Entry():
    def __init__(self, window, text=None, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkEntry(master=window(), **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            if text is not None:
                self._ctk.configure(placeholder_text=text)

            self.window = window


        except tkinter.TclError:
            print("Failed to create entry. Make sure you have a display.")
            self._ctk = None
            self._widget = None

    def hide(self):
        if self._ctk is not None:
            self._ctk.place_forget()

    def show(self):
        if self._ctk is not None:
            self.window.reinstate_widget(self)

    def get_value(self):
        return self._ctk.get()

class Frame():
    def __init__(self, window, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkFrame(master=window(), **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            self.window = window

        except tkinter.TclError:
            print("Failed to create frame. Make sure you have a display.")
            self._ctk = None
            self._widget = None

    def hide(self):
        if self._ctk is not None:
            self._ctk.place_forget()

    def show(self):
        if self._ctk is not None:
            self.window.reinstate_widget(self)


class Canvas():
    def __init__(self, window, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkCanvas(master=window(), **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            self.window = window

        except tkinter.TclError:
            print("Failed to create canvas. Make sure you have a display.")
            self._ctk = None
            self._widget = None

    def hide(self):
        if self._ctk is not None:
            self._ctk.place_forget()

    def show(self):
        if self._ctk is not None:
            self.window.reinstate_widget(self)

class Scrollbar():
    def __init__(self, window, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkScrollbar(master=window(), **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            self.window = window

        except tkinter.TclError:
            print("Failed to create scrollbar. Make sure you have a display.")
            self._ctk = None
            self._widget = None

    def hide(self):
        if self._ctk is not None:
            self._ctk.place_forget()

    def show(self):
        if self._ctk is not None:
            self.window.reinstate_widget(self)

class ScrollView():
    def __init__(self, window, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkScrollableFrame(window(), **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            self.window = window

        except tkinter.TclError:
            print("Failed to create scrollview. Make sure you have a display.")
            self._ctk = None
            self._widget = None

    def hide(self):
        if self._ctk is not None:
            self._ctk.place_forget()

    def show(self):
        if self._ctk is not None:
            self.window.reinstate_widget(self)

class Image():
    def __init__(self, window, image, style: util.Style = util.Style.empty(), properties={}, binds={}, options={}, **kwargs):
        try:
            if "file" in options:
                if options["file"]:
                    img = PIL.Image.open(image)

                else:
                    # use image bytes
                    img = None
            else:
                # use image bytes
                img = None

            if img is not None:
                # scale the image
                if "scale" in options:
                    if util.Types.is_instance(options["scale"], util.ImageScale):
                        img = img.resize(options["scale"]())
                    else:
                        raise ValueError("Incorrect argument, scale option must be of type ImageScale")

                img = ImageTk.PhotoImage(img)
                self._holder = Label(window=window, image=img, properties={"image": img}, text="", **kwargs)
                self._ctk = self._holder._ctk
                self._widget = widget.Widget(style, properties, binds, self._ctk)

                window.add_garbage_collect_path(image)

                self.window = window

            else:
                self._holder = None
                self._ctk = None
                self._widget = None
                print("Failed to read image")

        except Exception as e:
            print(f"Failed to create image: {e}")
            print("Make sure you have a display")
            self._ctk = None
            self._widget = None

    def hide(self):
        if self._ctk is not None:
            self._ctk.place_forget()

    def show(self):
        if self._ctk is not None:
            self.window.reinstate_widget(self)

class Checkbox():
    def __init__(self, window, text, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkCheckBox(window(), text=text, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            self.window = window

        except tkinter.TclError:
            print("Failed to create checkbox. Make sure you have a display.")
            self._ctk = None
            self._widget = None

    def get_value(self):
        return self._ctk.get()

    def hide(self):
        if self._ctk is not None:
            self._ctk.place_forget()

    def show(self):
        if self._ctk is not None:
            self.window.reinstate_widget(self)

class FileSelect:
    def __init__(self, window, label, title, initial_dir, filetypes, text, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkButton(master=window(), text=text, command=lambda: self._getInput(title, initial_dir, filetypes), **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            self.path = None

            self.window = window

            self.label = label

        except tkinter.TclError:
            print("Failed to create file select. Make sure you have a display.")
            self._ctk = None
            self._widget = None

    def _getInput(self, title, initial_dir, filetypes):
        self.path = util.selectFile(title, initial_dir, filetypes)
        self.label._ctk.configure(text=self.path.split("/")[-1])

    def get_value(self):
        return self.path

class FolderSelect:
    def __init__(self, window, label, title, initial_dir, text, style: util.Style = util.Style.empty(), properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkButton(master=window(), text=text, command=lambda: self._getInput(title, initial_dir), **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

            self.window = window

            self.label = label

            self.path = None

        except tkinter.TclError:
            print("Failed to create file select. Make sure you have a display.")
            self._ctk = None
            self._widget = None

    def _getInput(self, title, initial_dir):
        folder = util.selectFolder(title, initial_dir)
        self.label._ctk.configure(text=folder.split("/")[-1])
        self.path = folder

    def get_value(self):
        return self.path