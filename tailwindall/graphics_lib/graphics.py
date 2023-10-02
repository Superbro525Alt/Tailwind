import platform
import random
import threading
from collections import namedtuple
from typing import overload, Union, Final

from _distutils_hack import override

import tailwindall.util as util
import pygame

import sys
import os

import tkinter as tk

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import tailwindall.classes_lib.classes as classes
import tailwindall.graphics_lib.objects as objects
from tailwindall.graphics_lib.scenes import *


class PygameWindow:
    def __init__(self, window, name, onTick, init, resolution: util.resolution, background_color: util.string):

        self.window = window()
        self._window = window

        self._name = name

        pygame.init()

        self.screen = pygame.display.set_mode((resolution.width, resolution.height))

        pygame.display.set_caption(name)

        self.screen.fill(pygame.Color(background_color))
        self.clock = pygame.time.Clock()

        self.timer = 0

        self.onTick = onTick

        self.init = init

        self.init(self)

        # self.embed()

    def embed(self):
        os.environ['SDL_WINDOWID'] = str(self.window.winfo_id())
        if platform.system == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'

    def run(self):
        # Pygame loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.timer += self.clock.tick(60) / 1000

            pygame.display.update()

            self.onTick(self)

            if self._window.destroyed:
                running = False
            else:
                self.window.update()

        if not self._window.destroyed:
            util.exec_list(self._window._on_exit_functions, self.window.destroy())
        pygame.quit()


class PygameWindowStandalone(classes.BaseObject):
    def __init__(self, name, scenes: list[Scene], resolution: util.resolution, background_color: util.string):
        self._name = name
        self._scenes = scenes
        self._resolution = resolution
        self._background_color = background_color

        self._current_scene = 0

        self._screen = pygame.display.set_mode((resolution.width, resolution.height))

        pygame.display.set_caption(name)

        self._screen.fill(pygame.Color(background_color))

        self._clock = pygame.time.Clock()

        self._timer = 0

        self._onTick = self._scenes[self._current_scene]._onTick
        self._sceneInit = self._scenes[self._current_scene]._init

        self.change_scene(0)

        self.loopThread = threading.Thread(target=self._main_loop, daemon=True)

        self.main_loop_running = True

    def change_scene(self, scene: int):
        self._current_scene = scene

        self._onTick = self._scenes[self._current_scene]._onTick
        self._sceneInit = self._scenes[self._current_scene]._init

        if self._sceneInit is not None:
            self._sceneInit(self)

    def main_loop(self):
        self._main_loop()

    def stop_main_loop(self):
        self.main_loop_running = False
        self.loopThread.join()
        self.main_loop_running = True

    def _main_loop(self):
        while self.main_loop_running:
            self._screen.fill(pygame.Color(self._background_color))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._timer += self._clock.tick(60) / 1000

            if self._onTick is not None:
                self._onTick(self)

            self._scenes[self._current_scene].render(self._screen)

            pygame.display.update()
            pygame.display.flip()

    def get_scene(self):
        return self._scenes[self._current_scene]


class Size(classes.BaseObject):
    def __init__(self, width, height):
        self.width, self.height = width, height


class CartesianPlane(PygameWindowStandalone):
    def __init__(self, name, resolution: util.resolution, background_color: util.string, line_color: util.string,
                 center_color: util.string, gap: int = 50):
        super().__init__(name, [Scene([])], resolution, background_color)

        for i in range(0, resolution.width, gap):
            self.get_scene().add_object(objects.Line((i, 0), (i, resolution.height), line_color, 1))

        for i in range(0, resolution.height, gap):
            if not i == resolution.height / 2:
                self.get_scene().add_object(objects.Line((0, i), (resolution.width, i), line_color, 1))
            else:
                self.get_scene().add_object(objects.Line((0, i), (resolution.width, i), center_color, 1))

        self.get_scene().add_object(
            objects.Line((resolution.width / 2, 0), (resolution.width / 2, resolution.height), center_color, 1))

        self.rect = self._screen.get_rect()

        self.offset = list(self.rect.center)

        self.gap = gap

        self.user_input_data = {"selected_point": (0, 0)}
        self.events = []

    def main_loop(self, ontick=None):
        self._main_loop(ontick)

    def _main_loop(self, ontick=None):
        while self.main_loop_running:
            self._screen.fill(pygame.Color(self._background_color))
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._timer += self._clock.tick(60) / 1000

            if self._onTick is not None:
                self._onTick(self)
            if ontick is not None:
                ontick(self)

            self._scenes[self._current_scene].render(self._screen)

            pygame.draw.circle(self._screen, pygame.Color("green"), self.get_mouse_position_on_plane(), 5)

            pygame.display.update()
            pygame.display.flip()

    def get_mouse_position_on_plane(self):
        mouse_pos = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        # snap to the grid
        mouse_pos = (round(mouse_pos[0] / self.gap) * self.gap, round(mouse_pos[1] / self.gap) * self.gap)
        # invert the diagonals
        self.user_input_data["selected_point"] = (mouse_pos[0] - self.offset[0], self.offset[1] - mouse_pos[1])

        return mouse_pos

    def add_object(self, obj: Union[objects.GameObject, objects.Rectangle, objects.Line, objects.Polygon]):
        if not type(obj) == objects.Polygon and not type(obj) == objects.Point:
            obj.position = (obj.position[0] + self._resolution.width / 2, obj.position[1] + self._resolution.height / 2)
            obj.position = (obj.position[0] - obj.size[0] / 2, obj.position[1] - obj.size[1] / 2)
        if type(obj) == objects.Polygon:
            points = namedtuple("points", ["zero", "one", "two", "three"])
            old_points = points(obj.points[0], obj.points[1], obj.points[2], obj.points[3])
            for i in range(len(obj.points)):
                # obj.points[i] = (obj.points[i][0] + self._resolution.width / 2, obj.points[i][1] + self._resolution.height / 2)
                # convert list of catesian points to pygame points
                obj.points[i] = (round(obj.points[i][0] + self.offset[0]), round(self.offset[1] - obj.points[i][1]))

        if type(obj) == objects.Point:
            obj.position = (round(obj.position[0] + self.offset[0]), round(self.offset[1] - obj.position[1]))

        self.get_scene().add_object(obj, priority=0)

    def is_clicking(self, right=False):
        if right:
            return pygame.mouse.get_pressed()[2]
        else:
            return pygame.mouse.get_pressed()[0]

    def clear_points(self):
        for i in self.get_scene().objects:
            if type(i) == objects.Point:
                self.get_scene().objects.remove(i)
                self.get_scene().render(self._screen)
        for i in self.get_scene().objects:
            if type(i) == objects.Point:
                self.get_scene().objects.remove(i)
                self.get_scene().render(self._screen)
        for i in self.get_scene().objects:
            if type(i) == objects.Point:
                self.get_scene().objects.remove(i)
                self.get_scene().render(self._screen)

    def clear_polygons(self):
        for i in self.get_scene().objects:
            if type(i) == objects.Polygon:
                self.get_scene().objects.remove(i)
                self.get_scene().render(self._screen)
        for i in self.get_scene().objects:
            if type(i) == objects.Polygon:
                self.get_scene().objects.remove(i)
                self.get_scene().render(self._screen)
        for i in self.get_scene().objects:
            if type(i) == objects.Polygon:
                self.get_scene().objects.remove(i)
                self.get_scene().render(self._screen)


class Colors:
    @classmethod
    def random(cls):
        return cls.random_rgb()

    @classmethod
    def random_rgb(cls):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


if __name__ == '__main__':
    import tailwindall.maths_lib.shapes as shapes

    rules = classes.Rules({
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11): "Square",
        (1, 2, 3, 5, 6, 7, 8, 9, 10): "Rhombus",
        (1, 2, 4, 7, 8, 9, 10, 11): "Rectangle",
        (1, 2, 7, 8): "Parallelogram",
        (5, 6, 7, 9): "Kite",
        (1): "Trapezium"
    })

    win = CartesianPlane("Math CAT Investigation", util.resolution(1000, 500), "white", "black", "red")

    points_selected = []


    def get_point_select(window):
        for event in window.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(window.user_input_data["selected_point"])
                    window.add_object(objects.Point("red", window.user_input_data["selected_point"], 5))
                    points_selected.append(window.user_input_data["selected_point"])

                    if len(points_selected) == 4:
                        window.add_object(objects.Polygon(
                            shapes.get_shape_from_points(points=points_selected, rules=rules, clockwise=False),
                            Colors.random_rgb(), (0, 0), show_points=True, points_color="red", points_radius=5,
                            show_angles=True, show_side_lengths=True, show_name=True, gap=50))
                        points_selected.clear()
                        window.clear_points()

                elif event.button == 2:
                    points_selected.clear()
                    window.clear_polygons()
                    window.clear_points()


    win.main_loop(ontick=get_point_select)
