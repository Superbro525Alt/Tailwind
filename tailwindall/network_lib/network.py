import threading

class Request:
    def __init__(self, operation, data, extra=None):
        self.operation = operation.lower()
        self.data = data
        self.extra = extra

        self.req: str = ""

        if self.extra is None:
            self.req = f"{self.operation}|{self.data}"
        else:
            self.req = f"{self.operation}|{self.data}|{self.extra}"

    def __str__(self):
        return self.req