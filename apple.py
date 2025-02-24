import pygame as pg
import random
import constants as c
from snake import Snake

class Apple:
    def __init__(self):
        self.position = [c.TILE_SIZE*random.randint(0, 31), c.TILE_SIZE*random.randint(0, 23)]

    def initialize(self, snake):
        while self.position in snake.body or self.position == snake.head_position:
            self.position = [c.TILE_SIZE*random.randint(0, 31), c.TILE_SIZE*random.randint(0, 23)]