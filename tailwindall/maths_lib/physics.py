import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(parent_dir)))
sys.path.append(parent_dir)

import tailwindall.graphics_lib.objects as objects

from tailwindall.classes_lib.classes import BaseObject

class Bounds(BaseObject):
    def __init__(self, bounds: list[list[int]]):
        super().__init__()

        self.bounds = bounds

    def add_bounds(self, bounds):
        self.bounds.append(bounds)

    def remove_bounds(self, bounds):
        self.bounds.remove(bounds)

    def is_in_bounds(self, position):
        """
        :param position:
        :return:

        Get if position inside self.bounds

        self.bounds is a square described by a list of 2 points, the first being the top left corner, the second being the bottom right corner
        """
        if self.bounds == []:
            return True

        if self.bounds[0][0] <= position[0] <= self.bounds[1][0] and self.bounds[0][1] <= position[1] <= self.bounds[1][1]:
            return True

        return False


    def is_out_of_bounds(self, position):
        return not self.is_in_bounds(position)

    @classmethod
    def none(cls):
        return cls([])

class PhysicsEngine2D(BaseObject):
    def __init__(self, objects: list[objects.Sprite] = [], bounds: Bounds = Bounds.none()):
        super().__init__()
        print(bounds)
        self.objects = objects

        self.bounds = bounds

        self.gravity = 9.8

    def set_gravity(self, gravity):
        self.gravity = gravity

    def add_object(self, obj, gravity=True):
        self.objects.append(obj)

        if gravity:
            obj.use_gravity = True
        else:
            obj.use_gravity = False

    def __add__(self, other):
        if isinstance(other, objects.Sprite):
            self.objects.append(other)

    def update(self):
        for obj in self.objects:
            print(obj)
            if obj.falling:
                if obj.use_gravity:
                    obj.position = [obj.position[0], obj.position[1] + self.gravity]
                # if object in another object:
                for obj2 in self.objects:
                    if obj2 != obj:
                        if obj2.position[0] <= obj.position[0] <= obj2.position[0] + obj2.size[0] and obj2.position[1] <= obj.position[1] <= obj2.position[1] + obj2.size[1] and obj2.falling:
                            obj.position = [obj.position[0], obj2.position[1] - obj.size[1]]
                            obj.falling = False
                        else:
                            obj.falling = True

                print(self.bounds.is_out_of_bounds(obj.position))
                if self.bounds.is_out_of_bounds(obj.position):
                    obj.position = [obj.position[0], obj.position[1] - self.gravity]
                    obj.falling = False

                    # move object to edge of bounds
                    if obj.position[0] < self.bounds.bounds[0][0]:
                        obj.position = [self.bounds.bounds[0][0], obj.position[1]]
                        obj.falling = True

                    elif obj.position[0] > self.bounds.bounds[1][0]:
                        obj.position = [self.bounds.bounds[1][0], obj.position[1]]
                        obj.falling = True

                    elif obj.position[1] < self.bounds.bounds[0][1]:
                        obj.position = [obj.position[0], self.bounds.bounds[0][1]]
                        obj.falling = True

                    elif obj.position[1] > self.bounds.bounds[1][1]:
                        obj.position = [obj.position[0], self.bounds.bounds[1][1]]
                        obj.falling = True



