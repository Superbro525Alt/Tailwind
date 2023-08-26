import customtkinter
import util

class Widget(customtkinter.CTkBaseClass):
    def __init__(self, style, properties, binds):
        self._style = style
        self._properties = properties
        self.binds = binds

        self.reload_styles()
        self.reload_properties()
        self.reload_binds()

    def reload_styles(self):
        for style in list(self._style.keys()):
            try:
                exec(f"self.configure({style}={self._style[style]})")
            except:
                print(f"Failed to configure style {style} to {self._style[style]}")

            try:
                exec(f"self.{style} = {self._style[style]}")
            except:
                print(f"Failed to set style {style} to {self._style[style]}")
    def reload_properties(self):
        for _property in list(self._properties.keys()):
            try:
                exec(f"self.config({_property}={self._properties[_property]})")
            except:
                print(f"Failed to configure style {_property} to {self._properties[_property]}")

            try:
                exec(f"self.{_property} = {self._properties[_property]}")
            except:
                print(f"Failed to set style {_property} to {self._properties[_property]}")

    def reload_binds(self):
        for bind in list(self.binds.keys()):
            self.bind(f"<{bind}>", self.binds[bind])


