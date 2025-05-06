import pygame as pg
import random
import constants as c
from managers.input_manager import InputManager 

class Snake:
    def __init__(self):
        self.length = 1
        self.head_position = [
            c.TILE_SIZE * random.randint(0, 31),
            c.TILE_SIZE * random.randint(0, 23)
        ]
        self.body = []
        self.score = 0
        self.input_manager = InputManager()

    def get_direction(self) -> tuple:
        self.input_manager.update_direction()
        return self.input_manager.get_direction()

    def check_wall_collision(self):
        if self.head_position[0] < 0 or self.head_position[0] >= c.WIDTH:
            return True
        elif self.head_position[1] < 0 or self.head_position[1] >= c.HEIGHT:
            return True
        return False

    def check_snake_collision(self):
        return self.head_position in self.body

    def check_apple_collision(self, apple_position, direction):
        next_head_position = [
            self.head_position[0] + direction[0] * c.TILE_SIZE,
            self.head_position[1] + direction[1] * c.TILE_SIZE
        ]
        if next_head_position == apple_position:
            self.body.insert(0, list(self.head_position))
            self.head_position = list(apple_position)
            return True
        return False

    def restart(self):
        self.__init__()
