"""
    This file will contain the code 
    for tracking the users words per minute
"""
import pygame
# start a clock that will count the seconds from when the game starts.
# each time a word is entered correctly, calculate the words per minute and update it
# each time a word is entered incorrectly, calculate the words per minute with a penalty.


class Speed:

    def __init__(self):
        self.curr_wpm = 0
        self.x = 900
        self.y = 25

    def start_clock(self):
        self.start_time = pygame.time.get_ticks()
        self._compute_wpm()

    def correct_word(self):
        # calculate and update WPM if the user entered a word correctly
        print("correct word entered")
        self._compute_wpm()

    def incorrect_word(self):
        # calculate and update WPM if the user entered a word incorrectly
        print('word not on screen')
        self._compute_wpm()

    def _compute_wpm(self):
        # compute the words per minute
        elapsed_time = (self.start_time - pygame.time.get_ticks())
        print(elapsed_time)

    def draw_text(self, screen, text, x, y):
        # draw the WPM value on the screen
        wpm_rect = text.get_rect()
        wpm_rect.center(x, y)
        screen.blit(text, wpm_rect)

    def config_text(self, screen):
        wpm_str = "WPM: " + str(self.curr_wpm)
        font = pygame.font.Font(None, 52)
        text = font.render(wpm_str, True, (0, 0, 0))
        self.draw_text(screen, text, self.x, self.y)
