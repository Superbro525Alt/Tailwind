import os, sys
from typing import Union

import pygame

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import tailwindall.classes_lib.classes as classes
import tailwindall.maths_lib.shapes as shapes
import tailwindall.graphics_lib.events as events

pygame.font.init()

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

    def _calculate_sprite(self, screen):
        super().__init__(None, self.position, self.size, pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1]))

    def render(self, screen):
        super().__init__(None, self.position, self.size, pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1]))
        pygame.draw.rect(screen, self.color, self.sprite)
        return None

class Polygon(Sprite):
    def __init__(self, shape: Union[list[tuple[int, int]], shapes.Shape], color, position, show_points=False, points_color=None, points_radius=5, show_angles=False, show_side_lengths=False, show_name=False, gap=50):
        self.show_points = show_points
        self.points_color = points_color
        if type(shape) == list:
            self.points = shape
            self.shape = None
        else:
            self.points = shape.points
            self.shape = shape

        self.gap = gap
        self.color = color
        self.points_radius = points_radius
        self.show_angles = show_angles
        self.show_side_lengths = show_side_lengths
        self.show_name = show_name

        super().__init__(None, position, None, None)

    def render(self, screen):
        super().__init__(None, None, None, pygame.draw.polygon(screen, self.color, self.points))
        if self.show_points:
            for point in self.points:
                pygame.draw.circle(screen, self.points_color, point, self.points_radius)

        if self.shape is not None:
            # init font
            pygame.font.init()
            if self.show_angles:
                for i in range(len(self.shape.angles)):
                    text = pygame.font.Font("./fonts/FreeSansBold.ttf", 20).render(f"{str(int(self.shape.angles[i]))}°", True, (0, 0, 0))
                    screen.blit(text, (self.shape.points[i][0], self.shape.points[i][1]))

            if self.show_side_lengths:
                for i in range(len(self.shape.sides)):
                    text = pygame.font.Font("./fonts/FreeSansBold.ttf", 20).render(f"{str(int(self.shape.sides[i]))}", True, (0, 0, 0))
                    if not i == len(self.shape.sides) - 1:
                        screen.blit(text, ((self.shape.points[i][0] + self.shape.points[i + 1][0]) / 2, (self.shape.points[i][1] + self.shape.points[i + 1][1]) / 2))
                    else:
                        screen.blit(text, ((self.shape.points[i][0] + self.shape.points[0][0]) / 2, (self.shape.points[i][1] + self.shape.points[0][1]) / 2))

            if self.show_name:
                text = pygame.font.Font("./fonts/FreeSansBold.ttf", 20).render(f"{self.shape.name}", True, (0, 0, 0))
                center_of_shape = (sum([i[0] for i in self.shape.points]) / len(self.shape.points), sum([i[1] for i in self.shape.points]) / len(self.shape.points))
                center_of_shape = (center_of_shape[0] - text.get_width() / 2, center_of_shape[1] - text.get_height() / 2)
                height_of_shape = max([i[1] for i in self.shape.points]) - min([i[1] for i in self.shape.points])
                center_of_shape = (center_of_shape[0], center_of_shape[1] - height_of_shape / 1.5)
                screen.blit(text, (center_of_shape[0], center_of_shape[1]))
        return None

class Point(Sprite):
    def __init__(self, color, position, radius, pos_on_plane=None):
        self.color = color
        self.radius = radius
        self.pos_on_plane = pos_on_plane
        super().__init__(None, position, None, None)

    def _calculate_sprite(self, screen):
        super().__init__(None, self.position, self.size, pygame.draw.circle(screen, self.color, self.position, self.radius))

    def render(self, screen):
        super().__init__(None, self.position, self.size, pygame.draw.circle(screen, self.color, self.position, self.radius))
        if self.pos_on_plane is not None:
            text = pygame.font.Font("./fonts/FreeSansBold.ttf", 20).render(f"{self.pos_on_plane}", True, (0, 0, 0))
            pos = (self.position[0] - text.get_width() / 2, self.position[1] - text.get_height() / 2)
            pos = (pos[0], pos[1] - text.get_height() / 1.5)
            screen.blit(text, pos)
        return super().render(screen)

class Line(Sprite):
    def __init__(self, start_pos, end_pos, color, width):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.width = width
        super().__init__(None, None, None, None)

    def _calculate_sprite(self, screen):
        super().__init__(None, self.position, self.size, pygame.draw.rect(screen, self.color,
                                                                          pygame.Rect(self.position[0],
                                                                                      self.position[1], self.size[0],
                                                                                      self.size[1])))

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
