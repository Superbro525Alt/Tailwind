import os, sys

import pygame

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import tailwindall.classes_lib.classes as classes
import events

class Sprite(classes.BaseObject):
    def __init__(self, image, position, size, sprite=None):
        self.image = image
        self.position = position
        self.size = size
        self.sprite = sprite

    def render(self, screen):
        if self.sprite is None:
            if isinstance(self.image, str):
                self.image = pygame.image.load(self.image)
            return pygame.sprite.Sprite(self.image, self.position, self.size)
        return self.sprite

class Rectangle(Sprite):
    def __init__(self, color, position, size):
        self.color = color
        super().__init__(None, position, size, None)

    def set_up(self, screen):
        super().__init__(None, self.position, self.size, pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])))
    def render(self, screen):
        super().__init__(None, self.position, self.size, pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])))
        return super().render(screen)

class Line(Sprite):
    def __init__(self, start_pos, end_pos, color, width):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.width = width
        super().__init__(None, None, None, None)

    def render(self, screen):
        super().__init__(None, None, None, pygame.draw.line(screen, self.color, self.start_pos, self.end_pos, self.width))
        return super().render(screen)

class GameObject(classes.BaseObject):
    def __init__(self, model: Sprite, init, events: list[events.Event]):
        self.events = events
        self.model = model
        self.init = init

    def check_events(self):
        for event in self.events:
            event.check()

    def render(self, screen):
        self.model.render(screen)