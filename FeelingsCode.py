import random
import tkinter


def get_name():
    """Gets the users name and returns it when called"""
    name = input('Enter your name: ')
    if name == "":
        print("Please enter your name, you cannot leave it blank!")
        print()
        get_name()

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
    print()
    print('''
    *********************
    *** Feelings Menu ***
    *********************
    ***               ***  
    ***   A: Happy    ***
    ***   B: Sad      ***
    ***   C: Angry    ***
    ***               ***
    *********************
    *** Feelings Menu ***
    *********************
    ''')

    quotes_sad = ['Things change. And friends leave. Life doesn\'t stop for anybody.',
                  'Breathing is hard. When you cry so much, it makes you realize that breathing is hard.',
                  'You cannot protect yourself from sadness without protecting yourself from happiness.']

    quotes_happy = ['Be healthy and take care of yourself, but be happy with the beautiful things that make you, you.',
                    'The biggest adventure you can ever take is to live the life of your dreams.',
                    'Beauty is everywhere. You only have to look to see it.']

    quotes_angry = ['Never go to bed mad. Stay up and fight.',
                    'Don’t waste your time in anger, regrets, worries, and grudges. Life is too short to be unhappy.',
                    'The best fighter is never angry.']

    persons_feeling = input('Enter the feeling that\'s closest to how you are feeling: ')

    if 'happy' in persons_feeling.lower() or persons_feeling.lower() == 'a':
        print()
        print(quotes_happy[random.randint(0, len(quotes_happy) - 1)])

    elif 'sad' in persons_feeling.lower() or persons_feeling.lower() == 'b':
        print()
        print(quotes_sad[random.randint(0, len(quotes_sad) - 1)])

    elif 'angry' in persons_feeling.lower() or persons_feeling.lower() == 'c':
        print()
        print(quotes_angry[random.randint(0, len(quotes_angry) - 1)])

    elif persons_feeling == "":
        print("Please enter a feeling, you cannot leave it empty!")
        main_loop(name)

    else:
        print("Sorry, the generator doesn't quite understand that!")
        main_loop(name)


def main():
    name_ = get_name()
    welcome_message(name_)
    main_loop(name_)


main()
