import os

WIDTH = 800
HEIGHT = 600
TILE_SIZE = 25
SNAKE_TILE = 23
SNAKE_COLOR = (240,240,240)
APPLE_COLOR = (240, 10, 10)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

base_dir = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(base_dir, 'assets', 'PressStart2P-Regular.ttf')
