"""
start_screen.py
Caleb Rasmussen
This file holds the implementation for the StartScreen()
class.
"""

import pygame

# RGB Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class StartScreen():
    """
    A class that contains the start scren of the Jungle
    Typer game. The screen consists of a welcome message
    and a start button

    init()
    run(screen)
    end()
    handle_event(event)
    draw_text(screen, text, x y)
    draw(screen)
    """

    # Init: sets default values
    def __init__(self):
        self.screen_end = False
        self.game_mode = ""

    # Runs the program through other methods
    def run(self, screen):
        self.draw(screen)       # draws elements to screen

    # Returns the state of the screen
    def end(self):
        return self.screen_end

    # Handles typing game events
    def handle_event(self, event):
        # Quits program on exit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # If mouse button is clicked, end screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            # Words button
            if 240 <= mouse[0] <= 440 and 278 <= mouse[1] <= 308:
                self.game_mode = "words"
                self.screen_end = True

            # Poerty button
            elif 540 <= mouse[0] <= 740 and 278 <= mouse[1] <= 308:
                self.game_mode = "poetry"  # TODO: change to poerty
                self.screen_end = True

    # Draws text to the screen
    def draw_text(self, screen, text, x, y):
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)

    # Draws all screen elements: welcome message, and start button
    def draw(self, screen):
        # Draws welcome message
        font = pygame.font.Font(None, 56)
        welcome_text = font.render(
            "Welcome to the Fastest Fingers in the West!", True, BLACK)
        self.draw_text(screen, welcome_text, 500, 155)        # top middle

        # Game mode message
        font = pygame.font.Font(None, 36)
        text = font.render("Please select a game mode below:", True, BLACK)
        self.draw_text(screen, text, 500, 200)

    # Draws single words mode button on screen

    def draw_words_button(self, screen):
        font = pygame.font.Font(None, 42)
        text = font.render("Single Words", True, WHITE)
        screen.blit(text, (255, 280))

    # Draws poerty lines mode button on screen
    def draw_poerty_button(self, screen):
        font = pygame.font.Font(None, 42)
        text = font.render("Poerty Lines", True, WHITE)
        screen.blit(text, (555, 280))

    # Draws all main screen elements: final score and quit button
    def draw(self, screen):
        self.draw_welcome_message(screen)
        self.draw_words_button(screen)
        self.draw_poerty_button(screen)
