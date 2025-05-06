import pygame as pg

class InputManager:
    def __init__(self):
        self.direction = (1,0)
    
    def update_direction(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w] and self.last_direction != (0, 1):
            self.last_direction = (0, -1)
        
        elif keys[pg.K_a] and self.last_direction != (1, 0):
            self.last_direction = (-1, 0)
        
        elif keys[pg.K_s] and self.last_direction != (0, -1):
            self.last_direction = (0, 1)
        
        elif keys[pg.K_d] and self.last_direction != (-1, 0):
            self.last_direction = (1, 0)
    
    def get_direction(self):
        return self.direction