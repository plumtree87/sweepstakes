from contestants import Contestant
import random

class SweepStakes:
    def __init__(self):
        self.contestants = []
        self.registration_count = 1


    def register_contestant(self):

        first_name = input("What is your first name?")
        last_name = input("What is your last name?")
        email_address = input("What is your email address?")
        registration_number = input("Input the numbers of your driver's license ID Number. ONLY NUMBERS! No letters.")
        contestant = Contestant(first_name, last_name, email_address, registration_number)
        self.contestants.add(contestant)

    def pick_winner(self):
        num = random.randint(0, len(self.contestants))
        return self.contestants[num]

    def print_contestant_info(self, contestant):
        print(contestant["first_name"], contestant["last_name"], contestant["email_address"], contestant["registration_number"])