import threading
import tkinter.messagebox as messagebox
from tkinter import Tk
import customtkinter
import platform
import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import tailwindall.window as window
import tailwindall.util as util
import tailwindall.widgets as widgets
import tailwindall.fonts as fonts

_fonts = fonts.init()


class InfoPopup:
    def __init__(self, title, message, header, message_font=None, title_font=None):
        self.title = title
        self.message = message
        self.header = header

        self.message_font = message_font if message_font is not None else ("FiraCode Nerd Font", 15)
        self.title_font = title_font if title_font is not None else ("FiraCode Nerd Font", 20)

    def display(self):
        if platform.system() == "Linux":
            threading.Thread(target=self._run_windows, daemon=True).start()
        elif platform.system() == "Windows":
            threading.Thread(target=self._run_windows, daemon=True).start()
    def _run_windows(self):
        try:
            win = window.Window(None, self.title, util.WindowProperties(True, util.resolution(2560, 1080), util.resolution(600, 500)))
            def kill_window(_window):
                _window.quit()
                del _window

            win.add_widget(widgets.Label(win, self.header, font=self.title_font), util.PlaceData(0.5, 0.2, anchor=util.CenterAnchor.get_anchor()))
            win.add_widget(widgets.Label(win, self.message, font=self.message_font), util.PlaceData(0.5, 0.5, anchor=util.CenterAnchor.get_anchor()))
            win.add_widget(widgets.Button(win, "Ok", lambda: kill_window(win)), util.PlaceData(0.5, 0.9, anchor=util.CenterAnchor.get_anchor()))
            win.main_loop()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while displaying the popup:\n {e}")
            print(e)
