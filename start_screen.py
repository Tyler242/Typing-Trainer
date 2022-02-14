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

        # If mouse button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.screen_end = True
            # TODO: add button cordinates 

    # Draws text to the screen
    def draw_text(self, screen, text, x, y):
        text_rect = text.get_rect()
        text_rect.center = (x, y) 
        screen.blit(text, text_rect)

    # Draws all screen elements: welcome message, and start button
    def draw(self, screen):
        # Draws welcome message
        font = pygame.font.Font(None, 56)     
        welcome_text = font.render("Welcome to Jungle Typer!", True, BLACK)
        self.draw_text(screen, welcome_text, 500, 155)        # top middle

        # Button and text
        font = pygame.font.Font(None, 42)     
        button_text = font.render("  Start Game  ", True, WHITE)
        button = button_text.get_rect()
        button.center = (500, 307) # bottom middle
        pygame.draw.rect(screen, BLACK, button, 100) 
        screen.blit(button_text, button)   

