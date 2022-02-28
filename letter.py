import random
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

class Letter:
    def __init__(self, char, start_x, start_y):
        self.char = char

        self.x = start_x
        self.y = start_y

        r = random.randint(80, 255)
        g = random.randint(80, 255)
        b = random.randint(80, 255)
        self.color = BLACK #(r, g, b)

    def get_width(self):
        font = pygame.font.Font(None, 42)
        text = font.render(self.char, True, self.color)
        char_width = text.get_width()

        return char_width

    def draw(self, screen):
        self.x -= 3
        font = pygame.font.Font(None, 42)
        text = font.render(self.char, True, self.color)
        text_rect = text.get_rect()
        text_rect.center = (self.x, self.y)
        screen.blit(text, text_rect)

    def move_left(self, velocity):
        self.x -= velocity