"""
main_screen.py
Caleb Rasmussen
This file holds the implementation for the MainScreen()
class.
"""

import pygame
from word import Word
from score import Score

# RGB Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)


class MainScreen():
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
        self.score = Score()
        self.user_text = ""
        self.level = 1
        self.level_cut = 50
        self.lives = 5
        self.screen_end = False

        # Load a file of a words into a list, word_list
        with open(filename) as file:
            self.word_list = file.read().splitlines()

        # Init 3 words and put into screen words list
        word1 = Word(self.word_list, 1100, 150)
        word2 = Word(self.word_list, 1500, 225)
        word3 = Word(self.word_list, 1900, 300)
        self.screen_words = [word1, word2, word3]

    # Returns the current score as an int
    def get_score(self):
        current_score = self.score.get_score()
        return current_score

    # Returns the state of the screen
    def end(self):
        return self.screen_end

    # Runs the program through methods
    def run(self, screen):
        self.handle_logic()     # handles game logic 
        self.draw(screen)       # draws elements to screen

    # Handles game logic of lives, leveling up and word location
    def handle_logic(self):
        # If there no lives, end screen
        if self.lives <= 0:          
            self.screen_end = True

        # Level up
        if self.score.get_score() >= self.level_cut:         
            self.level_up()

        # If word went off screen
        for word in self.screen_words:
            if word.on_screen == False:     
                word.new_word()     # reset word 
                self.lives -= 1     # dock a lif

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
                        if self.user_text == word.get_word():        # if word is corrext
                            self.score.add(len(word.get_word()))     # add to score
                            word.new_word()                     # word reset
                self.user_text = ""     # reset user text

            else:
                self.user_text += event.unicode      # adds character to user_text
        
    # Draws all main screen elements
    def draw(self, screen):
        self.score.draw(screen)            # score counter     
        self.draw_level(screen)            # level counter
        self.draw_lives(screen)            # lives counter
        self.draw_input(screen)            # input box and text

        # Draws and moves words on scren
        for word in self.screen_words:
            word.draw(screen)
            word.move_left()

    # Draws text to the screen
    def draw_text(self, screen, text, x, y):
        text_rect = text.get_rect()
        text_rect.center = (x, y) 
        screen.blit(text, text_rect)

    # Draws text input box and text to the scren
    def draw_input(self, screen):
        # Draws input box
        input_rect = pygame.Rect(250, 365, 500, 32)
        pygame.draw.rect(screen, WHITE, input_rect) 
        
        # User text in input box
        font = pygame.font.Font(None, 32)
        text_surface = font.render(self.user_text, True, BLACK)  
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)
        
    # Draws level counter on the screen
    def draw_level(self, screen):
        font = pygame.font.Font(None, 52)     
        level_str = "Level: " + str(self.level)
        text = font.render(level_str, True, BLACK)
        self.draw_text(screen, text, 80, 25)        # top left corner

    # Draws the lives counter on the screen with colors
    def draw_lives(self, screen):
        color = BLACK

        # Draws "Lives: "
        font = pygame.font.Font(None, 52)       
        text = font.render("Lives: ", True, color)
        self.draw_text(screen, text, 80, 436)       # bottom left corner

        # Sets color of lives based on number of lives
        if self.lives >= 4:
            color = GREEN
        elif self.lives >= 2:
            color = ORANGE
        else:
            color = RED

        # Draws number of lives
        text = font.render(str(self.lives), True, color)
        self.draw_text(screen, text, 140, 436)       # bottom left corner next to lives

    # Levels up by increase speed
    def level_up(self):
        for word in self.screen_words:
            word.velocity += 1      # Increases speed

        self.level_cut += 50    # next level cut off
        self.level += 1         # next level
        self.lives = 5          # reset lives

