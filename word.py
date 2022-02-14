"""
score.py
Caleb Rasmussen
This file holds the implementation for the Word class.
"""

import pygame
import random

# RGB colors
BLACK = (0, 0, 0)


class Word:
    """
    A class that contains a randomly generated moving 
    word. 

    get_word()
    move_left()
    draw_text(scren, text, x, y)
    draw(screen)
    new_word()
    """

    # Init with random word, and a starting postion
    def __init__(self, word_list, start_x, start_y):
        self.word_list = word_list
        self.word = word_list[random.randint(0, len(self.word_list) - 1)]      # Generates random word

        self.start_x = start_x  # X and Y for reset
        self.start_y = start_y

        self.x = start_x    # Moving x and y
        self.y = start_y

        self.velocity = 2   # level 1, starting speed

        self.on_screen = True  # word is on screen

    # Returns current word as string
    def get_word(self):
        return self.word

    # Moves word left based on velocity
    def move_left(self):
        self.x -= self.velocity

    # Draws text to the screen
    def draw_text(self, screen, text, x, y):
        text_rect = text.get_rect()
        text_rect.center = (x, y) 
        screen.blit(text, text_rect)

    # Draws word to the screen
    def draw(self, screen):
        # If words is in bounds
        if self.x > -100:
            font = pygame.font.Font(None, 42)
            text = font.render(self.word, True, BLACK)
            self.draw_text(screen, text, self.x, self.y)
        else:
            self.on_screen = False      # word went off screen

    # Loads a new word and resets x and y
    def new_word(self):
        self.word = self.word_list[random.randint(0, len(self.word_list) - 1)]         # new random word from list
        
        self.x = self.start_x       # resets x and y to orginal init values
        self.y = self.start_y

        self.on_screen = True  # word is on screen