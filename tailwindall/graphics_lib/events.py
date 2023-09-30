import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import tailwindall.classes_lib.classes as classes

class Event(classes.BaseObject):
    """
    An event that can be triggered by a GameObject

    :param name: The name of the event
    :param event: The event (a function)
    :param on: What starts the event (a function)

    :return: An event object
    """
    def __init__(self, name, event, on):
        self.name = name
        self.event = event
        self.on = on

    def check(self):
        res = self.on()
        if res:
            self.event()