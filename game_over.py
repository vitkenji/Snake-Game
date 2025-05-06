import pygame as pg
import constants as c

class Game_Over:
    def __init__(self, score):
        self.score = score
        self.font = pg.font.Font(c.font_path, 30)
        self.font_2 = pg.font.Font(c.font_path, 20)
        self.game_over_text = self.font.render(f'GAME OVER', True, c.WHITE)
        self.restart_text = self.font_2.render('Press R to restart', True, c.WHITE)
        self.quit_text = self.font_2.render('Press Q to quit', True, c.WHITE)
        self.score_text = score_text = self.font.render(f'Score: {self.score}', True, c.WHITE)

    def print_game_over(self, screen):
        screen.fill(c.BLACK)
        screen.blit(self.game_over_text, (260, 200))
        screen.blit(self.score_text, (260, 300))
        screen.blit(self.restart_text, (260, 400))
        screen.blit(self.quit_text, (260, 450))        
        pg.display.flip()
    
    def get_restart(self) -> bool:
        gkeys = pg.key.get_pressed()
        
        for event in pg.event.get():
            if gkeys[pg.K_r]:
                return True
            elif gkeys[pg.K_q]:
                pg.quit()

        return False