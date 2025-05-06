import pygame as pg
import constants as c

class GraphicManager:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
    
    def clear_screen(self):
        self.screen.fill(c.BLACK)
    
    def draw_snake(self, head_position, body_segments):
    
    def draw_apple(self, position):
    
    def draw_score(self, score):

    def draw_game_over(self, texts: dict):
        self.clear_screen()
        for text, pos in texts.items():
            self.screen.blit(text, pos)

    def update_display(self):
        pg.display.flip()