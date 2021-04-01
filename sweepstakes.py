from contestants import Contestant
import random
import user_interface
from sweepstakes_queue_manager import QueueManager
from sweepstakes_stack_manager import StackManager


class SweepStakes:
    def __init__(self):
        self.contestants = {}

    def register_contestant(self):

        first_name = user_interface.ask_first_name()
        last_name = user_interface.ask_last_name()
        email_address = user_interface.ask_email_address()
        registration_number = user_interface.ask_registration_info()
        contestant = Contestant(first_name, last_name, email_address, registration_number)
        self.contestants[contestant.registration_number] = contestant

    def pick_winner(self):
        contestant = random.choice(list(self.contestants.values()))
        return contestant

    def print_contestant_info(self, contestant):
        print(contestant.first_name, "You Win")
