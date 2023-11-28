import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(parent_dir)))
sys.path.append(parent_dir)

import tailwindall.graphics_lib.objects as objects

class PhysicsEngine2D:
    def __init__(self, objects: list[objects.Sprite] = []):
        self.objects = objects

        self.gravity = 9.8

    def set_gravity(self, gravity):
        self.gravity = gravity

    def add_object(self, obj):
        self.objects.append(obj)

    def __add__(self, other):
        if isinstance(other, objects.Sprite):
            self.objects.append(other)

    def update(self):
        for obj in self.objects:
            print(obj.jumping)
            if obj.falling and not obj.jumping:
                obj.position = [obj.position[0], obj.position[1] + self.gravity]
                # if object in another object:
                for obj2 in self.objects:
                    if obj2 != obj:
                        if obj2.position[0] <= obj.position[0] <= obj2.position[0] + obj2.size[0] and obj2.position[1] <= obj.position[1] <= obj2.position[1] + obj2.size[1]:
                            obj.position = [obj.position[0], obj2.position[1] - obj.size[1]]
                            obj.falling = False
                            break
                        else:
                            obj.falling = True
