import customtkinter
import styles

class Window:
    def __init__(self, style, name, options={}):
        if "file" in options:
            self.style = styles.Styles.parse(style, True)
        else:
            self.style = styles.Styles.parse(style)

        self.name = name

        self._window = customtkinter.CTk()
        self._window.title(self.name)
        self._window.geometry("500x500" if "size" not in options else options["size"])
        self._window.resizable(False if "x-resizable" not in options else options["x-resizable"], False if "y-resizeable" not in options else options["y-resizable"])

    def main_loop(self):
        self._window.mainloop()


