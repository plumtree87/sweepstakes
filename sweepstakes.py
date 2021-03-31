from contestants import Contestant
import random
import user_interface

class SweepStakes:
    def __init__(self):
        self.contestants = []
        self.registration_count = 1


    def register_contestant(self):

        first_name = user_interface.ask_first_name()
        last_name = user_interface.ask_last_name()
        email_address = user_interface.ask_email_address()
        registration_number = user_interface.ask_registration_info()
        contestant = Contestant(first_name, last_name, email_address, registration_number)
        self.contestants.append(contestant)
        print(self.contestants)

    def pick_winner(self):
        num = random.randint(0, len(self.contestants))
        return self.contestants[num]

    def print_contestant_info(self, contestant):
        print(contestant["first_name"], contestant["last_name"], contestant["email_address"], contestant["registration_number"])