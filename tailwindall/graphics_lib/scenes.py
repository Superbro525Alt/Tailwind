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


class Scene(classes.BaseObject):
    def __init__(self, _objects: list[Union[objects.GameObject, objects.Rectangle, objects.Line]], init=None, onTick=None):
        self._onTick = onTick
        self._init = init

        self.objects = _objects

        if init is not None:
            init(self)
        if onTick is not None:
            onTick(self)

    def render(self, screen):

        for obj in self.objects:
            sprite = obj.render(screen)
            if sprite is not None:
                screen.blit(screen, sprite)

        if self._onTick is not None:
            self._onTick(self)

    def add_object(self, obj: Union[objects.GameObject, objects.Rectangle, objects.Line]):
        print(obj)
        self.objects.append(obj)
        if isinstance(self, CartesianPlane):
            # place object at the specified position even if it is (-1, 2)
            obj.position = (obj.position[0] + self.size.width / 2, obj.position[1] + self.size.height / 2)
            if obj.sprite is not None:
                obj.sprite.position = (obj.sprite.position[0] + self.size.width / 2, obj.sprite.position[1] + self.size.height / 2)
                print(obj.sprite.position)
class CartesianPlane(Scene):
    def __init__(self, gap, size, _objects: list[Union[objects.GameObject, objects.Rectangle, objects.Line]], init=None, onTick=None):
        super().__init__(_objects, init, onTick)

        self.gap = gap
        self.size = size

        for x in range(0, size.width, gap):
            self.objects.append(objects.Line((x, 0), (x, size.height), (255, 255, 255), 1))

        for y in range(0, size.height, gap):
            self.objects.append(objects.Line((0, y), (size.width, y), (255, 255, 255), 1))

        self.objects.append(objects.Line((0, size.height / 2), (size.width, size.height / 2), (255, 255, 255), 2))
        self.objects.append(objects.Line((size.width / 2, 0), (size.width / 2, size.height), (255, 255, 255), 2))