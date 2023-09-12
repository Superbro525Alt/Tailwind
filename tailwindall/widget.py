import customtkinter
import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import tailwindall.util as util

class Widget:
    def __init__(self, style, properties, binds, _ctk: customtkinter.CTkBaseClass, className=None, id=None):
        if util.Types.is_instance(style, util.Style):
            self._style = style
            self._properties = properties
            self._binds = binds

            self._ctk = _ctk

            self.type = util.Types.widget_type(self._ctk)

            self.className = className
            self.id = id


            self.reload_styles()
            self.reload_properties()
            self.reload_binds()
        else:
            raise ValueError("Incorrect argument, style must be of type util.Style")

    def reload_styles(self):
        if self.type in self._style.classes:
            for style in list(self._style.tags[self.type].keys()):
                try:
                    exec(f"self._ctk.configure({style}={self._style.tags[style]})")
                except Exception as e:
                    print(f"Failed to configure style {style} to {self._style.tags[style]}: {e}")

                try:
                    exec(f"self._ctk.{style} = {self._style.tags[style]}")
                except Exception as e:
                    print(f"Failed to set style {style} to {self._style.tags[style]}: {e}")

        if self.id is not None:
            if self.id in self._style.ids:
                for style in list(self._style.ids[self.id].keys()):
                    try:
                        exec(f"self._ctk.configure({style}={self._style.ids[style]})")
                    except Exception as e:
                        print(f"Failed to configure style {style} to {self._style.ids[style]}: {e}")

                    try:
                        exec(f"self._ctk.{style} = {self._style.ids[style]}")
                    except Exception as e:
                        print(f"Failed to set style {style} to {self._style.ids[style]}: {e}")

        if self.className is not None:
            if self.className in self._style.classes:
                for style in list(self._style.classes[self.className].keys()):
                    try:
                        exec(f"self._ctk.configure({style}={self._style.classes[style]})")
                    except Exception as e:
                        print(f"Failed to configure style {style} to {self._style.classes[style]}: {e}")

                    try:
                        exec(f"self._ctk.{style} = {self._style.classes[style]}")
                    except Exception as e:
                        print(f"Failed to set style {style} to {self._style.classes[style]}: {e}")
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


