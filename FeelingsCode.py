import random


def get_name():
    """Gets the users name and returns it when called"""
    name = input('Enter your name: ')
    if name == "":
        print("Please enter your name, you cannot leave it blank!")
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

    quotes_sad = ['Quote1_sad', 'Quote2_sad', 'Quote3_sad']
    quotes_happy = ['Quote1_happy', 'Quote2_happy', 'Quote3_happy']
    quotes_angry = ['Quote1_angry', 'Quote2_angry', 'Quote3_angry']

    persons_feeling = input('Enter the feeling that\'s closest to how you are feeling: ')

    if 'happy' in persons_feeling.lower() or persons_feeling.lower() == 'a':
        print(quotes_happy[random.randint(0, len(quotes_happy) - 1)])
    elif 'sad' in persons_feeling.lower() or persons_feeling.lower() == 'b':
        print(quotes_sad[random.randint(0, len(quotes_sad) - 1)])
    elif 'angry' in persons_feeling.lower() or persons_feeling.lower() == 'c':
        print(quotes_angry[random.randint(0, len(quotes_angry) - 1)])
    elif persons_feeling == "":
        print("Please enter a feeling, you cannot leave it empty!")
        main_loop(name)
    else:
        print("Sorry, the generator doesn't quite understand that!")
        main_loop(name)


def main():
    user_name = get_name()
    welcome_message(user_name)
    main_loop(user_name)


main()