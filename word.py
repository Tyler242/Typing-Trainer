"""
score.py
Caleb Rasmussen
This file holds the implementation for the Word class.
"""

from letter import Letter

import pygame
import random

# RGB colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)


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
        # Generates random word
        self.word = word_list[random.randint(0, len(self.word_list) - 1)]

        self.start_x = start_x  # X and Y for reset
        self.start_y = start_y

        self.x = start_x    # Moving x and y
        self.y = start_y

        self.velocity = .3   # level 1, starting speed

        self.letters = []

        current_x = start_x

        for char in self.word:

            font = pygame.font.Font(None, 42)
            text = font.render(char, True, BLACK)
            char_width = text.get_width()

            letter = Letter(char, current_x + (char_width / 2), start_y)
            self.letters.append(letter)
            current_x += letter.get_width()

        self.on_screen = True  # word is on screen

    # Returns current word as string
    def get_word(self):
        return self.word

    # Moves word left based on velocity
    def move_left(self):
        self.x -= self.velocity
        for letter in self.letters:
            letter.move_left(self.velocity)

    # Draws text to the screen
    def draw_text(self, screen, text, x, y):
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)

    # Draws word to the screen
    def draw(self, screen):
        # If words is in bounds
        if self.x > 0:
            for letter in self.letters:
                letter.draw(screen)
        else:
            self.on_screen = False      # word went off screen

    # Loads a new word and resets x and y
    def new_word(self):
        # new random word from list
        self.word = self.word_list[random.randint(0, len(self.word_list) - 1)]

        self.letters = []

        self.x = self.start_x       # resets x and y to orginal init values
        self.y = self.start_y

        current_x = self.x

        for char in self.word:
            font = pygame.font.Font(None, 42)
            text = font.render(char, True, BLACK)
            char_width = text.get_width()

            letter = Letter(char, current_x + (char_width / 2), self.start_y)
            self.letters.append(letter)
            current_x += letter.get_width()

        self.on_screen = True  # word is on screen

    def show_completion(self, text):
        if text in self.word and len(text) <= len(self.word):
            for char in enumerate(text):
                if char[1] == self.letters[char[0]].char:
                    self.letters[char[0]].color = RED
        else:
            for letter in self.letters:
                letter.color = BLACK
