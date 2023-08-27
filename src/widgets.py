import tkinter

import widget
import customtkinter

class Button(customtkinter.CTkButton):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkButton(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create button. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Label(customtkinter.CTkLabel, widget.Widget):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkLabel(master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create label. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Entry(customtkinter.CTkEntry, widget.Widget):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkEntry(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create entry. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Frame(customtkinter.CTkFrame, widget.Widget):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkFrame(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create frame. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Canvas(customtkinter.CTkCanvas, widget.Widget):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkCanvas(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create canvas. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Scrollbar(customtkinter.CTkScrollbar, widget.Widget):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkScrollbar(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create scrollbar. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class ScrollView(customtkinter.CTkScrollableFrame, widget.Widget):
    def __init__(self, master, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = customtkinter.CTkScrollableFrame(master, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)
        except tkinter.TclError:
            print("Failed to create scrollview. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Image(Frame, widget.Widget):
    def __init__(self, master, image, style={}, properties={}, binds={}, **kwargs):
        try:
            self._ctk = Label(master=master, image=image, **kwargs)
            self._widget = widget.Widget(style, properties, binds, self._ctk)

        except tkinter.TclError:
            print("Failed to create image. Make sure you have a display.")
            self._ctk = None
            self._widget = None