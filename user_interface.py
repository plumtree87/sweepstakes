
def ask_first_name():
    fname = input("What is contestants first name?")
    return fname


def ask_last_name():
    lname = input("What is contestants last name?")
    return lname


def ask_email_address():
    email = input("What is their email address? ex. YourEmail@email.com ")
    return email


def ask_registration_info():
    while True:
        try:
            regis_num = int(input("Input their Birthday and then a 6 digit passcode only they would remember. Example July 6th 1987, passcode 177311, = 761987177311"))
            break
        except: ValueError
    return regis_num

def ask_firm_type_of_data_structure():
    answer = "Gibberish"
    while answer != "a" or answer != "b":
        if answer == "a":
            return True
        if answer == "b":
            return False
        else:
            answer = input("Would you like to use a (a)queue manager or (b)stack manager  ")


def add_more_contestants():
    answer = "Supercalafregalisticsexpialadotious!"
    while answer != "y" or answer != "n":
        if answer == "y":
            return True
        if answer == "n":
            return False
        else:
            answer = input("Would you like to add another contestant? (y/n) ")


def create_new_sweepstake():
        answer = "Gibberish"
        while answer != "y" or answer != "n":
            if answer == "y":
                return True
            if answer == "n":
                return False
            else:
                answer = input("Create a sweepstake? (y/n) ")