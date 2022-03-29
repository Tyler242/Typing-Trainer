import pygame
from score import Score
from word import Word
from timer import Timer
from wpm import WPM

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)


class Game:
    """
    Parent class for any gamemode
    """

    def __init__(self, filename):
        self.score = Score()
        self.time = Timer(60)
        self.wpm = WPM()
        self.user_text = ""
        self.level = 1
        self.level_cut = 50
        self.screen_end = False
        self.screen_words = []

        # Load a file of a words into a list, word_list
        with open(filename) as file:
            self.word_list = file.read().splitlines()

        # Returns the current score as an int
    def get_score(self):
        current_score = self.score.get_score()
        return current_score

    # Returns the current words per minute
    def get_wpm(self):
        return self.wpm.curr_wpm

    # Returns the state of the screen
    def end(self):
        return self.screen_end

        # Draws all main screen elements
    def draw(self, screen):
        self.score.draw(screen)            # score counter
        self.draw_level(screen)            # level counter
        self.wpm.config_text(screen)
        self.time.config_text(screen)
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

    # Levels up by increase speed
    def level_up(self):
        for word in self.screen_words:
            word.velocity += 1     # Increases speed

        self.level_cut += 50    # next level cut off
        self.level += 1         # next level
