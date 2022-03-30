import pygame
from word import Word
from game import Game
from pygame import mixer


class Jeff(Game):

    def __init__(self, filename):
        super().__init__(filename)

        mixer.music.load('jeff.mp3')
        mixer.music.play()

        # Init 3 jeffs and put into screen words list
        jeff1 = Word(self.word_list, 1000, 150)
        jeff2 = Word(self.word_list, 1300, 225)
        jeff3 = Word(self.word_list, 1600, 300)
        jeff4 = Word(self.word_list, 1000, 300)
        jeff5 = Word(self.word_list, 1300, 300)
        self.screen_words = [jeff1, jeff2, jeff3, jeff4, jeff5]

        self.background = pygame.image.load('jeff.jpg')
        self.jeff_screen = False

        # Runs the program through methods
    def run(self, screen):
        self.handle_logic()
        screen.blit(self.background, (0, 0))   # handles game logic
        self.draw(screen)       # draws elements to screen

    # Handles game logic of lives, leveling up and word location
    def handle_logic(self):
        # If there no lives, end screen
        if self.time.get_curr_time() >= self.time.end_time:
            self.screen_end = True

        # Level up
        if self.score.get_score() >= self.level_cut:
            self.level_up()

        # If word went off screen
        for word in self.screen_words:
            if word.on_screen == False:
                word.new_word()  # reset word

    # Handles game events
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

            # Return is pressed
            elif event.key == pygame.K_RETURN:
                for word in self.screen_words:
                    if self.user_text == word.get_word():
                        # if word is correct
                        word.new_word()
                        self.wpm.correct_word(
                            self.time.get_curr_time())
                        self.score.add(len(word.get_word()))     # add to score

                self.user_text = ""     # reset user text

            else:
                self.user_text += event.unicode      # adds character to user_text

            for word in self.screen_words:
                word.show_completion(self.user_text)
