import pygame as pg
import random
import constants as c

class Snake:
    def __init__(self):
        self.length = 1
        self.head_position = [c.TILE_SIZE*random.randint(0, 31), c.TILE_SIZE*random.randint(0, 23)]
        self.last_direction = (1, 0)
        self.body = []
        
    def get_direction(self) -> tuple:
        keys = pg.key.get_pressed()
        
        if keys[pg.K_w] and self.last_direction != (0, 1):
            self.last_direction = (0, -1)
        
        elif keys[pg.K_a] and self.last_direction != (1, 0):
            self.last_direction = (-1, 0)
        
        elif keys[pg.K_s] and self.last_direction != (0, -1):
            self.last_direction = (0, 1)
        
        elif keys[pg.K_d] and self.last_direction != (-1, 0):
            self.last_direction = (1, 0)
        
        return self.last_direction
    
    def check_wall_collision(self):
        if self.head_position[0] < 0 or self.head_position[0] > c.WIDTH:
            return True
        elif self.head_position[1] < 0 or self.head_position[1] > c.HEIGHT:
            return True
        return False

    def check_snake_collision(self):
        for segment in self.body:
            if segment == self.head_position:
                return True
        return False

    def check_apple_collision(self, apple_position, direction):

        next_head_position = [self.head_position[0] + direction[0]*25, self.head_position[1] + direction[1]*25] 
        if next_head_position == apple_position:
            self.body.insert(0, self.head_position)
            self.head_position = apple_position
            return True

        return False
    
    def restart(self):
        self.length = 1
        self.head_position = [c.TILE_SIZE*random.randint(0, 31), c.TILE_SIZE*random.randint(0, 23)]
        self.last_direction = (1, 0)
        self.body = []
