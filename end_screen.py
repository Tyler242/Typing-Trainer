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
    def __init__(self, score, wpm):
        self.score = score

        high_scores_file = open("high_scores.txt", "r")
        names = []
        high_scores = []
        
        for high_score in high_scores_file.readlines():
            name_score = high_score.split("=")
            names.append(name_score[0])
            high_scores.append(name_score[1])

        if len(high_scores) <= 5 or high_scores[5] < self.score:
            index = 0
            
            for high_score in high_scores:
                if int(high_score) > self.score:
                    index += 1
            
            names.insert(index,"Test_Name")
            high_scores.insert(index, self.score)

        high_scores_size = len(high_scores)

        if high_scores_size > 5:
            high_scores_size = 5

        high_scores_file = open("high_scores.txt", "w")

        for i in range(high_scores_size):
            high_scores_file.writelines(f"{names[i]}={high_scores[i]}")

        high_scores_file.close()
           

        self.wpm = wpm

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
            if 607 <= mouse[0] <= 687 and 378 <= mouse[1] <= 408:
                self.screen_end = True

            # Restart button
            elif 297 <= mouse[0] <= 417 and 378 <= mouse[1] <= 408:
                self.restart_game = True
                self.screen_end = True

    # Draws text to the screen
    def draw_text(self, screen, text, x, y):
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)

    # Draws end messages on screen
    def draw_end_message(self, screen):
        font = pygame.font.Font(None, 74)
        text = font.render("Good Job!", True, BLACK)
        self.draw_text(screen, text, 500, 55)      # top middle

    # Draws Final Score
    def draw_score(self, screen):
        score_str = "Final Score:" + str(self.score)
        font = pygame.font.Font(None, 50)
        text = font.render(score_str, True, BLACK)
        self.draw_text(screen, text, 500, 100)      # top middle

    def draw_highscores(self, screen):
        high_scores = open("high_scores.txt", "r")
    
        font = pygame.font.Font(None, 50)
        text = font.render("High Scores", True, BLACK)
        self.draw_text(screen, text, 500, 155)

        for i, score in enumerate(high_scores.readlines()):
            font = pygame.font.Font(None, 30)
            text = font.render(score[:-1], True, BLACK)
            self.draw_text(screen, text, 500, 205 + i * 35)
            pass # draw high scores

        pass

    def draw_wpm(self, screen):
        wpm_str = "Words Per Minute:" + str(self.wpm)
        font = pygame.font.Font(None, 50)
        text = font.render(wpm_str, True, BLACK)
        self.draw_text(screen, text, 500, 245)

    # Draws quit button and text
    def draw_quit_button(self, screen):
        font = pygame.font.Font(None, 42)
        text = font.render("Quit", True, WHITE)
        pygame.draw.rect(screen, BLACK, [607, 378, 80, 30])
        screen.blit(text, (615, 380))  


    # Draws restart button and text
    def draw_restart_button(self, screen):
        font = pygame.font.Font(None, 42)
        text = font.render("Restart", True, WHITE)
        pygame.draw.rect(screen, BLACK, [297, 378, 120, 30])
        screen.blit(text, (305, 380))  

    # Draws all main screen elements: final score and quit button

    def draw(self, screen):
        self.draw_end_message(screen)
        self.draw_score(screen)
        self.draw_highscores(screen)
        self.draw_wpm(screen)
        self.draw_quit_button(screen)
        self.draw_restart_button(screen)
