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


        if self._onTick is not None:
            self._onTick(self)

    def add_object(self, obj: Union[objects.GameObject, objects.Rectangle, objects.Line], priority: int = None):
        if priority is not None:
            self.objects.insert(priority, obj)
        else:
            self.objects.append(obj)

