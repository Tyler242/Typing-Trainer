"""
    This class will hold the timer for the game.
    We will end an instance of the game once the timer has finished.
"""
import time


class Timer():
    def __init__(self, duration) -> None:
        # time the clock should run
        self.duration = duration
        self.start_time = time.time()
        self.end_time = self.duration

    def get_curr_time(self):
        return time.time() - self.start_time
