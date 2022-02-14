"""
score.py
Caleb Rasmussen
This file holds the implementation for the Score class.
"""

import pygame

# RGB colors
BLACK = (0, 0, 0)


class Score:
    """
    A class that contains the score of the game.

    init()
    get_score()
    add(num)
    reset()
    draw_text(scren, text, x, y)
    draw(screen)
    """
    # Init: sets default values
    def __init__(self):
        self.score = 0
        self.x = 900
        self.y = 25

    # Returns score as int
    def get_score(self):
        return self.score

    # Adds num to score total
    def add(self, num):
        self.score += num

    # Resets score
    def reset(self):
        self.score = 0

    # Draws text to the screen
    def draw_text(self, screen, text, x, y):
        text_rect = text.get_rect()
        text_rect.center = (x, y) 
        screen.blit(text, text_rect)

    # Draw score counter on the screen
    def draw(self, screen):
        score_str = "Score: " + str(self.score)
        font = pygame.font.Font(None, 52)       
        text = font.render(score_str, True, BLACK)
        self.draw_text(screen, text, self.x, self.y)         # top right corner