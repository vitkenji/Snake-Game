import pygame as pg
import time
from snake import Snake
from apple import Apple
import random as r
import constants as c

pg.init()
screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
clock = pg.time.Clock()
running = True
snake = Snake()
apple = Apple()
apple.initialize(snake)
score = 0
font = pg.font.Font('PressStart2P-Regular.ttf', 20)
restart = False

def restart_game():
    score = 0
    snake = Snake()
    apple = Apple()
    apple.initialize(snake)
    restart = False

def game_over():
    global restart
    screen.fill((0,0,0))
    game_over_text = font.render(f'GAME OVER', True, c.WHITE)
    score_text = score_text = font.render(f'Score: {score}', True, c.WHITE)
    screen.blit(game_over_text, (400, 300))
    screen.blit(score_text, (400, 400))
    
    pg.display.flip()

    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    restart_game()
                    waiting = False 


while running:
    if (not (snake.check_wall_collision() or snake.check_snake_collision())) and not restart:
        screen.fill((0,0,0))

        score_text = font.render(f'Score: {score}', True, c.WHITE)
        screen.blit(score_text, (10, 10))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # printing snake's head first
        direction = snake.get_direction()
        ate_apple = snake.check_apple_collision(apple.position, direction)
        
        if ate_apple:
            score += 1
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
        
        pg.display.flip()
        clock.tick(8)
    else:
        game_over()

pg.quit()

