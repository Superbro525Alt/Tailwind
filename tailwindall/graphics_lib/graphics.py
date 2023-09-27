import platform
import threading
from typing import overload, Union

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

    def get_scene(self):
        return self._scenes[self._current_scene]

class Size(classes.BaseObject):
    def __init__(self, width, height):
        self.width, self.height = width, height


if __name__ == '__main__':
    win = PygameWindowStandalone("Test", [CartesianPlane(50, Size(500, 500), [])],
                                 util.resolution(500, 500), "black")

    win.get_scene().add_object(objects.Rectangle((255, 0, 0), (-1, 0), (50, 50)))

    win.main_loop()


