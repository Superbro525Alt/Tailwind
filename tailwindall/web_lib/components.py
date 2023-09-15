class Button:
    def __init__(self, text, onclick):
        self.text = text
        self.onclick = onclick

    def __str__(self):
        return f"<button onclick='{self.onclick}'>{self.text}</button>"