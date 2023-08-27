import customtkinter
import util

class Widget(customtkinter.CTkBaseClass):
    def __init__(self, style, properties, binds, _ctk):
        self._style = style
        self._properties = properties
        self._binds = binds

        self._ctk = _ctk

        self.reload_styles()
        self.reload_properties()
        self.reload_binds()

    def reload_styles(self):
        for style in list(self._style.keys()):
            try:
                exec(f"self._ctk.configure({style}={self._style[style]})")
            except Exception as e:
                print(f"Failed to configure style {style} to {self._style[style]}: {e}")

            try:
                exec(f"self._ctk.{style} = {self._style[style]}")
            except Exception as e:
                print(f"Failed to set style {style} to {self._style[style]}: {e}")
    def reload_properties(self):
        for _property in list(self._properties.keys()):
            try:
                exec(f"self._ctk.configure({_property}={self._properties[_property]})")
            except Exception as e:
                try:
                    exec(f'self._ctk.configure({_property}="{self._properties[_property]}")')
                except Exception as j:
                    print(f"Failed to configure property {_property} to {self._properties[_property]}: {j}")

            try:
                exec(f"self._ctk.{_property} = {self._properties[_property]}")
            except Exception as e:
                try:
                    exec(f'self._ctk.{_property} = "{self._properties[_property]}"')
                except Exception as j:
                    print(f"Failed to set property {_property} to {self._properties[_property]}: {j}")

    def reload_binds(self):
        for bind in list(self._binds.keys()):
            self._ctk.bind(f"<{bind}>", self._binds[bind])


