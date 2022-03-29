"""
    This class will hold the timer for the game.
    We will end an instance of the game once the timer has finished.
"""
import time
import pygame


class Timer():
    def __init__(self, duration) -> None:
        # time the clock should run
        self.duration = duration
        self.start_time = time.time()
        self.end_time = self.duration
        self.x = 900
        self.y = 436

    def get_curr_time(self):
        return time.time() - self.start_time

    def draw_time(self, screen, text, x, y):
        # draw the time on the screen
        wpm_rect = text.get_rect()
        wpm_rect.center = (x, y)
        screen.blit(text, wpm_rect)

    def config_text(self, screen):
        time_str = "Time: " + str(60 - round(self.get_curr_time()))
        font = pygame.font.Font(None, 52)
        text = font.render(time_str, True, (0, 0, 0))
        self.draw_time(screen, text, self.x, self.y)
