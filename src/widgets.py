import tkinter

import widget
import customtkinter

class Button(customtkinter.CTkButton):
    def __init__(self, style, properties, binds, master, **kwargs):
        try:
            self._ctk = customtkinter.CTkButton(master=master, **kwargs)
            self._widget = widget.Widget(style, properties, binds)
        except tkinter.TclError:
            print("Failed to create button. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Label(customtkinter.CTkLabel, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        try:
            customtkinter.CTkLabel.__init__(self, master, **kwargs)
            widget.Widget.__init__(self, style, properties, binds)
        except tkinter.TclError:
            print("Failed to create label. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Entry(customtkinter.CTkEntry, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        try:
            customtkinter.CTkEntry.__init__(self, master=master, **kwargs)
            widget.Widget.__init__(self, style, properties, binds)
        except tkinter.TclError:
            print("Failed to create entry. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Frame(customtkinter.CTkFrame, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        try:
            customtkinter.CTkFrame.__init__(self, master=master, **kwargs)
            widget.Widget.__init__(self, style, properties, binds)
        except tkinter.TclError:
            print("Failed to create frame. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Canvas(customtkinter.CTkCanvas, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        try:
            customtkinter.CTkCanvas.__init__(self, master=master, **kwargs)
            widget.Widget.__init__(self, style, properties, binds)
        except tkinter.TclError:
            print("Failed to create canvas. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class Scrollbar(customtkinter.CTkScrollbar, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        try:
            customtkinter.CTkScrollbar.__init__(self, master=master, **kwargs)
            widget.Widget.__init__(self, style, properties, binds)
        except tkinter.TclError:
            print("Failed to create scrollbar. Make sure you have a display.")
            self._ctk = None
            self._widget = None

class ScrollView(customtkinter.CTkScrollableFrame, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        try:
            customtkinter.CTkScrollableFrame.__init__(self, master, **kwargs)
            widget.Widget.__init__(self, style, properties, binds)
        except tkinter.TclError:
            print("Failed to create scrollview. Make sure you have a display.")
            self._ctk = None
            self._widget = None

