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
        self.restart_game = False
        
    # Runs program through other methods
    def run(self, screen):
        self.draw(screen)       # draws elements to screen
    
    # Returns the state of the screen, bool
    def end(self):
        return self.screen_end

    # Returns the state of the screen, bool
    def get_restart(self):
        return self.restart_game

    # Handles typing game events
    def handle_event(self, event):
        # Quits program on exit
        if event.type == pygame.QUIT:      
                pygame.quit()
                quit()

        # If mouse button is clicked, end screen
        if event.type == pygame.MOUSEBUTTONDOWN:	
            mouse = pygame.mouse.get_pos()

            # Quit Button
            if 607 <= mouse[0] <= 687 and 278 <= mouse[1] <= 308:
                self.screen_end = True

            # Restart button
            elif 297 <= mouse[0] <= 417 and 278 <= mouse[1] <= 308:
                self.restart_game = True
                self.screen_end = True
    
    # Draws text to the screen
    def draw_text(self, screen, text, x, y):
        text_rect = text.get_rect()
        text_rect.center = (x, y) 
        screen.blit(text, text_rect)

    #Draws end messages on screen
    def draw_end_message(self, screen):
        font = pygame.font.Font(None, 74)       
        text = font.render("Good Job!", True, BLACK)
        self.draw_text(screen, text, 500, 155)      # top middle

    # Draws Final Score 
    def draw_score(self, screen):   
        score_str = "Final Score:" + str(self.score)
        font = pygame.font.Font(None, 50)       
        text = font.render(score_str, True, BLACK)
        self.draw_text(screen, text, 500, 200)      # top middle

    # Draws quit button and text
    def draw_quit_button(self, screen):
        font = pygame.font.Font(None, 42)     
        text = font.render("Quit", True, WHITE)
        pygame.draw.rect(screen, BLACK, [607, 278, 80, 30])
        screen.blit(text, (615, 280))  

    # Draws restart button and text   
    def draw_restart_button(self, screen):
        font = pygame.font.Font(None, 42)     
        text = font.render("Restart", True, WHITE)
        pygame.draw.rect(screen, BLACK, [297, 278, 120, 30])
        screen.blit(text, (305, 280))  


    # Draws all main screen elements: final score and quit button
    def draw(self, screen):
        self.draw_end_message(screen)
        self.draw_score(screen)
        self.draw_quit_button(screen)
        self.draw_restart_button(screen)


