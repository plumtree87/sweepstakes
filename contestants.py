

class Contestant:
    def __init__(self, first_name, last_name, email_address, registration_number):
        self.contestant = {

            "first_name": first_name,
            "last_name": last_name,
            "email_address": email_address,
            "registration_number": registration_number

        }

    def notify(self, picked_winner):
        print(picked_winner["first_name"], picked_winner["last_name"], "WINS!")
        #email the winner here if you can....
