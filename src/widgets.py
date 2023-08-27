import tkinter

from PIL import ImageTk

import widget

import customtkinter

import PIL

import util

class Button(customtkinter.CTkButton):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkButton(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create button. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Label(customtkinter.CTkLabel):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkLabel(master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError as e:
            print(f"Failed to create label. Make sure you have a display. {e}")
            self._ctk = None
            self._widget = None

class Entry(customtkinter.CTkEntry):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkEntry(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create entry. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Frame(customtkinter.CTkFrame):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkFrame(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create frame. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Canvas(customtkinter.CTkCanvas):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkCanvas(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create canvas. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Scrollbar(customtkinter.CTkScrollbar):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkScrollbar(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create scrollbar. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class ScrollView(customtkinter.CTkScrollableFrame):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkScrollableFrame(master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create scrollview. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Image():
    def __init__(self, master, image, style={}, properties={}, binds={}, options={}, **kwargs):
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
                    if util.is_type(options["scale"], util.ImageScale):
                        img = img.resize(options["scale"]())
                    else:
                        raise ValueError("Incorrect argument, scale option must be of type ImageScale")

                img = ImageTk.PhotoImage(img)
                self._holder = Label(master=master, image=img, properties={"image": img}, **kwargs)
                self._ctk = self._holder._ctk
                self._widget = widget.Widget(style, properties, binds, self._ctk)

            else:
                self._holder = None
                self._ctk = None
                self._widget = None
                print("Failed to read image")

        except Exception as e:
            print(f"Failed to create image: {e}")
            self._ctk = None
            self._widget = None