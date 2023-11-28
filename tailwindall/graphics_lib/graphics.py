import sys
import os

import tkinter as tk
from time import sleep

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import platform
import logging

logging.basicConfig(level=logging.DEBUG)

if platform.system() != "Windows":
    logging.warning("This module is only properly supported on windows. Proceed with caution.")

import random
import threading
from collections import namedtuple

import tailwindall.util as util
import pygame

import tailwindall.classes_lib.classes as classes
import tailwindall.graphics_lib.objects as objects
from tailwindall.graphics_lib.scenes import *
import tailwindall.popup as popup

import tailwindall.maths_lib.physics as physics

VERSION = "0.0.1"

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

    def show_popup(self, title, message, header, message_font=None, title_font=None):
        popup.InfoPopup(title, message, header, message_font, title_font).display()


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

        self.line_color = line_color
        self.center_color = center_color
        self.resolution = resolution

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
            # add text showing to corresponding cartesian plane point
            text = pygame.font.Font("./fonts/FreeSansBold.ttf", 20).render(
                f"{self.screen_to_plane(self.user_input_data['selected_point'])}", True, (0, 0, 0))
            pos = (self.get_mouse_position_on_plane()[0] - text.get_width() / 2,
                   self.get_mouse_position_on_plane()[1] - text.get_height() / 2)
            # move pos a bit up dynamically
            pos = (pos[0], pos[1] - text.get_height() / 1.5)

            self._screen.blit(text, pos)
            pygame.display.update()
            pygame.display.flip()

    def zoom(self, amount: int):
        # self.gap += amount

        # self.redraw_plane()
        pass

    def get_mouse_position_on_plane(self):
        mouse_pos = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        # snap to the grid
        gap = self.gap if self.gap != 0 else 50
        mouse_pos = (round(mouse_pos[0] / gap) * gap, round(mouse_pos[1] / gap) * gap)
        # invert the diagonals
        self.user_input_data["selected_point"] = (mouse_pos[0] - self.offset[0], self.offset[1] - mouse_pos[1])

        return mouse_pos

    def add_object(self,
                   obj: Union[objects.GameObject, objects.Rectangle, objects.Line, objects.Polygon, objects.Point]):
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

    def clear_objects(self, t, rep=20):
        threading.Thread(target=lambda: self._clear_objects(t, rep), daemon=True).start()

    def _clear_objects(self, t, rep=20):
        for j in range(rep):
            for i in self.get_scene().objects:
                if type(i) == t:
                    self.get_scene().objects.remove(i)
                    self.get_scene().render(self._screen)

    def screen_to_plane(self, pos: tuple[int, int]):
        gap = self.gap if self.gap != 0 else 50
        return (pos[0] / gap, pos[1] / gap)

    def redraw_plane(self):
        print("Redrawing plane...")
        self.clear_objects(objects.Line)
        print(self.gap)
        gap = self.gap if self.gap != 0 else 50
        print(gap)
        for i in range(0, self.resolution.width, gap):
            self.get_scene().add_object(objects.Line((i, 0), (i, self.resolution.height), self.line_color, 1))

        for i in range(0, self.resolution.height, gap):
            if not i == self.resolution.height / 2:
                self.get_scene().add_object(objects.Line((0, i), (self.resolution.width, i), self.line_color, 1))
            else:
                self.get_scene().add_object(objects.Line((0, i), (self.resolution.width, i), self.center_color, 1))

        self.get_scene().add_object(
            objects.Line((self.resolution.width / 2, 0), (self.resolution.width / 2, self.resolution.height),
                         self.center_color, 1))

class PlatformerWindow(PygameWindowStandalone):
    def __init__(self, name, resolution: util.resolution, background_color: util.string):
        super().__init__(name, [Scene([])], resolution, background_color)

        self.bounds = physics.Bounds(
            [[0, 0], [resolution.width, resolution.height]]
        )

        self._engine = physics.PhysicsEngine2D([], self.bounds)


        self._gravity = 0.5

        self._objects = []

        self._player = None

        self._player_speed = 5

        self._player_jumping = False

        self._player_jump_power = 100

        self.resolution = resolution

        self.set_player(objects.Rectangle("red", (0, 0), (50, 50), setup=True))



    def add_object(self, obj: Union[objects.GameObject, objects.Rectangle, objects.Line, objects.Polygon], gravity=True):
        self._objects.append(obj)

        if gravity:
            self._engine.add_object(obj)
        else:
            self._engine.add_object(obj, False)

        self.get_scene().add_object(obj, priority=0)

    def set_player(self, player: objects.Rectangle):
        self._player = player

        self.add_object(player)

    def set_player_speed(self, speed: int):
        self._player_speed = speed

    def set_player_jump_power(self, power: int):
        self._player_jump_power = power

    def set_gravity(self, gravity: int):
        self._gravity = gravity

    def main_loop(self):
        self._main_loop()

    def _main_loop(self):
        while self.main_loop_running:
            self._screen.fill(pygame.Color(self._background_color))
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self._player.falling = False

                        self.jump_player(self._player_jump_power)

                    if event.key == pygame.K_d:
                        self._player_speed = 5

                    if event.key == pygame.K_a:
                        self._player_speed = -5

            if not self.is_key_pressed("d") and not self.is_key_pressed("a"):
                self._player_speed = 0

            self._timer += self._clock.tick(60) / 1000

            if self._onTick is not None:
                self._onTick(self)

            self._scenes[self._current_scene].render(self._screen)

            pygame.display.update()
            pygame.display.flip()

            if self._player is not None:
                self._player.position = (self._player.position[0] + self._player_speed, self._player.position[1])

                if self._player.position[1] >= self.resolution.height - self._player.size[1]:
                    self._player.position = (self._player.position[0], self.resolution.height - self._player.size[1])

                    self._player.falling = False

                    self._player_jump_power = 25

                if self._player.position[0] <= 0:
                    self._player.position = (0, self._player.position[1])

                if self._player.position[0] >= self.resolution.width - self._player.size[0]:
                    self._player.position = (self.resolution.width - self._player.size[0], self._player.position[1])

            self._engine.update()

    def is_clicking(self, right=False):
        if right:
            return pygame.mouse.get_pressed()[2]
        else:
            return pygame.mouse.get_pressed()[0]

    def is_key_pressed(self, key: str):
        return pygame.key.get_pressed()[getattr(pygame, f"K_{key.lower()}")]

    def is_key_pressed_once(self, key: str):
        return self.is_key_pressed(key) and self._timer % 1 == 0

    def is_key_pressed_once_and_held(self, key: str):
        return self.is_key_pressed(key) and self._timer % 1 == 0 and self._timer % 10 == 0

    def is_key_pressed_and_held(self, key: str):
        return self.is_key_pressed(key) and self._timer % 10 == 0

    def move_player(self, x: int, y: int):
        self._player.position = (self._player.position[0] + x, self._player.position[1] + y)

    def jump_player(self, power: int):
        if not self._player.falling:
            self._player.falling = False

            # jump
            threading.Thread(target=self._jump_player, args=(power,), daemon=True).start()

    def _jump_player(self, power: int):
        if self._player.falling or self._player.jumping:
            return
        self._player_jumping = True
        self._player.falling = False
        self._player.jumping = True
        for i in range(power):
            self._player.position = (self._player.position[0], self._player.position[1] - 5)
            sleep(0.01)

        self._player.falling = True
        while self._player.falling:
            print("Falling...")
        self._player.jumping = False

    def set_player_jumping(self, jumping: bool):
        self._player_jumping = jumping

    def jump_player_once(self, power: int):
        if self.is_key_pressed_once("space"):
            self.jump_player(power)

class Colors:
    @classmethod
    def random(cls):
        return cls.random_rgb()

    @classmethod
    def random_rgb(cls):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

class Tests:
    @classmethod
    def all(cls):
        try:
            cls.color_test()
            cls.cartesian_plane_test()
            cls.window_standalone_test()

            logging.info("All tests passed.")
            return True
        except Exception as e:
            logging.error(f"Test failed: {e}")
            return False

    @classmethod
    def color_test(cls):
        logging.info("Testing colors...")
        for i in range(10):
            logging.info(Colors.random_rgb())
        logging.info("Colors test passed.")

    @classmethod
    def cartesian_plane_test(cls):
        logging.info("Testing cartesian plane...")
        win = CartesianPlane("Test", util.resolution(1000, 1000), "white", "black", "red")
        def stop():
            sleep(5)
            win.main_loop_running = False

        threading.Thread(target=stop, daemon=True).start()

        win.main_loop()

        logging.info("Cartesian plane test passed.")

    @classmethod
    def window_standalone_test(cls):
        logging.info("Testing window standalone...")
        win = PygameWindowStandalone("Test", [Scene([])], util.resolution(1000, 1000), "white")
        def stop():
            sleep(5)
            win.main_loop_running = False

        threading.Thread(target=stop, daemon=True).start()

        win.main_loop()

        logging.info("Window standalone test passed.")



print(f"Loaded tailwindall.graphics_lib.graphics v{VERSION}")
if __name__ == '__main__':
    import tailwindall.maths_lib.shapes as shapes

    rules = classes.Rules({
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11): "Square",
        (1, 2, 3, 5, 6, 7, 8, 9, 10): "Rhombus",
        (1, 2, 4, 7, 8, 11): "Rectangle",
        (1, 2, 7, 8): "Parallelogram",
        (5, 6, 7, 9): "Kite",
        (1, 11): "Trapezium",
    }, {
        1: "One pair of parallel sides",
        2: "Two pairs of parallel sides",
        3: "All sides are equal",
        4: "All angles are 90°",
        5: "Two pairs of equal adjacent sides",
        6: "Diagonals are perpendicular",
        7: "One diagonal bisects the other",
        8: "Both diagonals bisect each other",
        9: "One diagonal bisects the angle it passes through",
        10: "Both diagonals bisect the angles they pass through",
        11: "Diagonals are equal in length"
    })

    win = CartesianPlane("Math CAT Investigation", util.resolution(2000, 1000), "white", "black", "red")

    points_selected = []


    def get_point_select(window: CartesianPlane):
        for event in window.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    window.add_object(objects.Point("red", window.user_input_data["selected_point"], 5,
                                                    window.screen_to_plane(window.user_input_data["selected_point"])))
                    points_selected.append(window.user_input_data["selected_point"])

                    if len(points_selected) == 4:
                        shape = shapes.get_shape_from_points(points_selected, rules, clockwise=False)
                        window.add_object(objects.Polygon(
                            shape,
                            Colors.random_rgb(), (0, 0), show_points=True, points_color="red", points_radius=5,
                            show_angles=True, show_side_lengths=True, show_name=True, gap=50))

                        t = threading.Thread(target=lambda: window.show_popup(
                            f"Proofs - {shape.name if shape.name is not None else 'None'}", shape.data()[0],
                            shape.data()[1]))
                        t.setDaemon(True)

                        t.start()

                        points_selected.clear()
                        window.clear_objects(objects.Point)
                elif event.button == 2:
                    points_selected.clear()
                    window.clear_objects(objects.Polygon)
                    window.clear_objects(objects.Point)
                if event.button == 4:
                    window.zoom(50)
                elif event.button == 5:
                    window.zoom(-50)


    win.main_loop(ontick=get_point_select)
