"""
main_screen.py
Caleb Rasmussen
This file holds the implementation for the MainScreen()
class.
"""

import pygame
from word import Word
from score import Score
from timer import Timer
from wpm import WPM
from game import Game
from pygame import mixer


import os.path
from os import path

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)


class MainScreen(Game):
    """
    A class that contains the main screen of the Jungle Typer
    game. It handles the moving words, input box, levels, scoring,
    and lives counter.

    init()
    get_score()
    end()
    run(screen)
    handle_logic()
    handle_event(event)
    draw(screen)
    draw_text(screen, text, x, y)
    draw_input(screen)
    draw_level(screen)
    draw_lives(screen)
    level_up()
    """

    # Init: sets default values
    def __init__(self, filename):
        super().__init__(filename)

        mixer.music.load('GameMusic.mp3')
        mixer.music.play()

        # Init 3 words and put into screen words list
        word1 = Word(self.word_list, 1000, 150)
        word2 = Word(self.word_list, 1300, 225)
        word3 = Word(self.word_list, 1600, 300)
        self.screen_words = [word1, word2, word3]

        self.jeff_count = 0
        self.jeff_screen = False

    # Runs the program through methods
    def run(self, screen):
        self.handle_logic()     # handles game logic
        self.draw(screen)       # draws elements to screen

    # Handles game logic of lives, leveling up and word location
    def handle_logic(self):
        # If there no lives, end screen
        if self.time.get_curr_time() >= self.time.end_time:
            self.screen_end = True

        # Level up
        if self.score.get_score() >= self.level_cut:
            self.level_up()

        # If word went off screen
        for word in self.screen_words:
            if word.on_screen == False:
                word.new_word()  # reset word

    # Handles game events
    def handle_event(self, event):
        # Quits program on exit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # If key is pressed
        if event.type == pygame.KEYDOWN:

            # Backspace is pressed
            if event.key == pygame.K_BACKSPACE:
                if len(self.user_text) > 0:
                    self.user_text = self.user_text[:-1]

            # Return is pressed
            elif event.key == pygame.K_RETURN:
                for word in self.screen_words:
                    if self.user_text == word.get_word():
                        # if word is correct
                        word.new_word()
                        self.wpm.correct_word(
                            self.time.get_curr_time())
                        self.score.add(len(word.get_word()))     # add to score

                    elif self.user_text == 'jeff':
                        self.user_text = ''
                        self.jeff_count += 1
                        if self.jeff_count == 3:
                            self.screen_end = True
                            self.jeff_screen = True

                self.user_text = ""     # reset user text

            else:
                self.user_text += event.unicode      # adds character to user_text

            for word in self.screen_words:
                word.show_completion(self.user_text)
