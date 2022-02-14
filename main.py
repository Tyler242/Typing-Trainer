"""
main.py
Caleb Rasmussen
This file holds the implementation for the main function
that serves as the engine for the program and runs the 
game classes and methods. 
"""

# Libraries and classes
import pygame
from main_screen import MainScreen
from start_screen import StartScreen
from end_screen import EndScreen


# MAIN
def main():

    # Initaialize pygame
    pygame.init() 
    clock = pygame.time.Clock()

    # Set screen dimensions
    SCREEN_WIDTH = 1000
    SCREEN_HIEGHT = 461
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))

    # Load the background image
    background = pygame.image.load("jungle.jpg")
    pygame.display.set_caption('Jungle Typer')

    # Loop variables
    filename = "words.txt"
    screen_count = 0
    current_screen = StartScreen()


    # Runs the program
    while True:

        # Draws Background and current screen
        screen.blit(background, (0, 0))
        current_screen.run(screen)

        # Changes screens if necessary
        if current_screen.end() == True:
            if screen_count == 0:           # main
                current_screen = MainScreen(filename)
                screen_count += 1

            elif screen_count == 1:         # end
                score = current_screen.get_score()
                current_screen = EndScreen(score)
                screen_count += 1

            # End program if there are no more screen
            else:
                pygame.quit()
                quit()

        # Sends program events to current screen
        for event in pygame.event.get():
            current_screen.handle_event(event)

        # Update program    
        clock.tick(60)
        pygame.display.update()


# Start program
main()