"""
main.py
Caleb Rasmussen
This file holds the implementation for the main function
that serves as the engine for the program and runs the 
game classes and methods. 
"""

# Libraries and classes
import streamlit as st
from timer import Timer
from end_screen import EndScreen
from start_screen import StartScreen
from main_screen import MainScreen
import pygame
import os
from pygame.locals import *
from pygame import mixer


# MAIN
def main():

    # Initaialize pygame
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    mixer.music.load('jeff.mp3')
    mixer.music.play()


    # Set screen dimensions
    SCREEN_WIDTH = 1000
    SCREEN_HIEGHT = 461
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))

    # Load the background image
    background = pygame.image.load("desert.jpg")
    pygame.display.set_caption('Desert Typer')

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
                # timer.start_timer()

            elif screen_count == 1:         # End Screen
                score = current_screen.get_score()
                wpm = current_screen.get_wpm()
                current_screen = EndScreen(score, wpm)
                screen_count += 1

            elif screen_count == 2:
                # Restart
                if current_screen.get_restart() == True:
                    current_screen = MainScreen(filename)
                    screen_count -= 1

                # Quit
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
st.write(main())
