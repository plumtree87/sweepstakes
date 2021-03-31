
def ask_first_name():
    fname = input("What is your first name?")
    return fname


def ask_last_name():
    lname = input("What is your last name?")
    return lname


def ask_email_address():
    email = input("What is your email address? ex. YourEmail@email.com ")
    return email


def ask_registration_info():
    while True:
        try:
            regis_num = int(input("Input your Birthday and then a 6 digit passcode only you would remember. Example July 6th 1987, passcode 177311, = 761987177311"))
            break
        except: ValueError
    return regis_num

