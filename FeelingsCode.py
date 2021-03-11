import random


def get_name():
    """Gets the users name and returns it when called"""
    name = input('Enter your name: ')

    return name


def welcome_message(name):
    """This runs the welcome message and explains what is happening"""
    name_ = name
    print("Hello, " + name_ + "! \nWelcome to the feelings generator!")
    print()
    print("Enter a feeling or the letter corresponding to how you are feeling to generate a quote based off of that "
          "feeling")


def main_loop(name):
    """This runs the main loop and handles feelings"""
    print('''
    *********************
    *** Feelings Menu ***
    *********************
    *** A: Happy      ***
    *** B: Sad        ***
    *** C: Angry      ***
    *********************
    ''')

    quotes_sad = ['Quote1_sad', 'Quote2_sad', 'Quote3_sad']
    quotes_happy = ['Quote1_happy', 'Quote2_happy', 'Quote3_happy']
    quotes_angry = ['Quote1_angry', 'Quote2_angry', 'Quote3_angry']

    persons_feeling = input('Enter the feeling that\'s closest to how you are feeling: ')

    if persons_feeling == 'sad'.lower() or 'a'.lower():
        print(quotes_sad[random.randint(0, len(quotes_sad) - 1)])


def main():
    user_name = get_name()
    welcome_message(user_name)
    main_loop(user_name)


main()