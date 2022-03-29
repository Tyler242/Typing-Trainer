import pygame
from end_screen import BLACK
from score import Score
from sentence import Sentence
from timer import Timer
from wpm import WPM
from game import Game
from pygame import mixer


class PoetryScreen(Game):

    def __init__(self, filename):
        super().__init__(filename)

        mixer.music.load('GameMusic.mp3')
        mixer.music.play()

        # Init 3 words and put into screen words list
        sentence = Sentence(self.word_list, 1000, 150)
        self.poetry_words = sentence.get_word().split()
        self.screen_words = [sentence]

        self.jeff_count = 0
        self.jeff_screen = False

    def run(self, screen):
        self.handle_logic()     # handles game logic
        self.draw_instructions(screen)
        self.draw(screen)       # draws elements to screen

    def handle_logic(self):
        if self.time.get_curr_time() >= self.time.end_time:
            self.screen_end = True

        # Level up
        if self.score.get_score() >= self.level_cut:
            self.level_up()

        # If word went off screen
        for word in self.screen_words:
            if word.on_screen == False:
                word.new_word()  # reset word
                self.poetry_words = word.get_word().split()

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

            # Return key is pressed
            elif event.key == pygame.K_RETURN:
                for word in self.screen_words:
                    word.new_word()
                    self.poetry_words = word.get_word().split()

                    if self.user_text == 'jeff':
                        self.user_text = ''
                        self.jeff_count += 1
                        if self.jeff_count == 4:
                            self.screen_end = True
                            self.jeff_screen = True

                self.user_text = ""

            elif event.key == pygame.K_SPACE:
                # compare the users most recent word, based on spaces
                # with the poetry queue
                if len(self.user_text) > 0:
                    self.user_text = self.user_text + ' '
                    recent_word = self.user_text.split()[-1]
                    if recent_word == self.poetry_words[0]:
                        del self.poetry_words[0]
                        self.wpm.correct_word(self.time.get_curr_time())
                        self.score.add(len(recent_word))
            else:
                self.user_text += event.unicode      # adds character to user_text

            for word in self.screen_words:
                word.show_completion(self.user_text)

    def draw_instructions(self, screen):
        font = pygame.font.Font(None, 40)
        instructions = 'Press enter for new sentence'
        text = font.render(instructions, True, BLACK)
        self.draw_text(screen, text, 500, 436)
