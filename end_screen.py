"""
end_screen.py
Caleb Rasmussen
This file holds the implementation for the EndScreen()
class.
"""

import pygame

# RGB Colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class EndScreen():
    """
    A class that contains the end screen for the Jungle Typer
    game. The end screen prints the final score and has a
    quit button.

    init()
    run(screen)
    end()
    handle_event(event)
    draw_text(scren, text, x, y)
    draw(screen)
    """

    # Init: sets default values
    def __init__(self, score):
        self.score = score
        self.screen_end = False
        
    # Runs program through other methods
    def run(self, screen):
        self.draw(screen)       # draws elements to screen
    
    # Returns the state of the screen, bool
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
            self.screen_end = True
    
    # Draws text to the screen
    def draw_text(self, screen, text, x, y):
        text_rect = text.get_rect()
        text_rect.center = (x, y) 
        screen.blit(text, text_rect)

    # Draws all main screen elements: final score and quit button
    def draw(self, screen):
        # Draws Final Score   
        score_str = "Final Score:" + str(self.score)
        font = pygame.font.Font(None, 56)       
        text = font.render(score_str, True, BLACK)
        self.draw_text(screen, text, 500, 155)      # top middle

        # Draws quit button and text
        font = pygame.font.Font(None, 42)     
        button_text = font.render("  Quit  ", True, WHITE)
        button = button_text.get_rect()
        button.center = (500, 307)          # bottom middle
        pygame.draw.rect(screen, BLACK, button, 0)
        screen.blit(button_text, button)   

