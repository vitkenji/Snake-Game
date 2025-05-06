import pygame as pg
import time
from entities.snake import Snake
from entities.apple import Apple
import random as r
import constants as c
from game_over import Game_Over

pg.init()
screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
clock = pg.time.Clock()
running = True
snake = Snake()
apple = Apple()
apple.initialize(snake)
font = pg.font.Font(c.font_path, 20)
restart = False

def restart_game():
    snake.restart()
    apple.restart()
    apple.initialize(snake)
    restart = False

while running:
    if (not (snake.check_wall_collision() or snake.check_snake_collision())) and not restart:
        screen.fill(c.BLACK)

        # printing snake's head first
        direction = snake.get_direction()
        ate_apple = snake.check_apple_collision(apple.position, direction)
        
        if ate_apple:
            snake.score += 1
            apple.initialize(snake)

        last_position = snake.head_position[:]
        snake.head_position[0] += direction[0]*25
        snake.head_position[1] += direction[1]*25
        pg.draw.rect(screen, c.SNAKE_COLOR, pg.Rect(snake.head_position[0], snake.head_position[1], c.SNAKE_TILE, c.SNAKE_TILE))

        # printing remaining parts of snake
        for i in range(len(snake.body)):
            aux = snake.body[i][:]
            snake.body[i] = last_position[:]
            last_position = aux[:]
            pg.draw.rect(screen, c.SNAKE_COLOR, pg.Rect(snake.body[i][0], snake.body[i][1], c.SNAKE_TILE, c.SNAKE_TILE))

        pg.draw.rect(screen, c.APPLE_COLOR, pg.Rect(apple.position[0], apple.position[1], c.SNAKE_TILE, c.SNAKE_TILE))
        
        score_text = font.render(f'Score: {snake.score}', True, c.WHITE)
        screen.blit(score_text, (10, 10))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pg.display.flip()
        clock.tick(8)
    else:
        gameover = Game_Over(snake.score)
        restart_btn = gameover.get_restart()
        gameover.print_game_over(screen)

        if restart_btn:
            restart_game()

pg.quit()

