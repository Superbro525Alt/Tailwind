import widget
import customtkinter

class Button(customtkinter.CTkButton):
    def __init__(self, style, properties, binds, master, **kwargs):
        self._ctk = customtkinter.CTkButton(master=master, **kwargs)
        self._widget = widget.Widget(style, properties, binds)

class Label(customtkinter.CTkLabel, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        customtkinter.CTkLabel.__init__(self, master, **kwargs)
        widget.Widget.__init__(self, style, properties, binds)

class Entry(customtkinter.CTkEntry, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        customtkinter.CTkEntry.__init__(self, master=master, **kwargs)
        widget.Widget.__init__(self, style, properties, binds)

class Frame(customtkinter.CTkFrame, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        customtkinter.CTkFrame.__init__(self, master=master, **kwargs)
        widget.Widget.__init__(self, style, properties, binds)

class Canvas(customtkinter.CTkCanvas, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        customtkinter.CTkCanvas.__init__(self, master=master, **kwargs)
        widget.Widget.__init__(self, style, properties, binds)

class Scrollbar(customtkinter.CTkScrollbar, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        customtkinter.CTkScrollbar.__init__(self, master=master, **kwargs)
        widget.Widget.__init__(self, style, properties, binds)

class ScrollView(customtkinter.CTkScrollableFrame, widget.Widget):
    def __init__(self, style, properties, binds, master, **kwargs):
        customtkinter.CTkScrollableFrame.__init__(self, master, **kwargs)
        widget.Widget.__init__(self, style, properties, binds)

