import random

sad_quotes = ['A million words would not bring you back, I know because I tried, neither would a million tears, '
              'I know because I cried.',
              'Things change. And friends leave. Life doesn\'t stop for anybody.',
              'Breathing is hard. When you cry so much, it makes you realize that breathing is hard.']
angry_quotes = ['I don\'t usually lose my temper, but if I get angry, it\'s true - I\'m scary.',
                'Sometimes, you have to get angry to get things done.',
                'For every minute you remain angry, you give up sixty seconds of peace of mind.']
tired_quotes = ['Losers quit when they’re tired. Winners quit when they’ve won.',
                'When I’d get tired and want to stop, I’d wonder what my next opponent was doing. I’d wonder if he '
                'was still working out. I’d tried to visualize him. When I could see him working, I’d start pushing '
                'myself. When I could see him in the shower, I’d push myself harder.',
                'My goal is to build a life that I don’t need a vacation from.']
happy_quotes = ['Be healthy and take care of yourself, but be happy with the beautiful things that make you, you.',
                'The biggest adventure you can ever take is to live the life of your dreams.',
                'Beauty is everywhere. You only have to look to see it.']
worried_quotes = ['Worry never robs tomorrow of its sorrow, it only saps today of its joy.',
                  'Worry often gives a small thing a big shadow.',
                  'People become attached to their burdens sometimes more than the burdens are attached to them.']
annoyed_quotes = ['I don\'t even want you to nod, that\'s how much you annoy me. Just freeze and shut up.',
                  'I like long walks, especialy when they are taken by people who annoy me.',
                  'If you can\'t annoy somebody, there is little point in writing.']


def get_name():
    """Awaits user input and sets the name value"""
    name = input("Enter your name: ")

    return name


def welcome_message(name):
    """This is called at the start and starts loop"""
    user_name = name
    print("Welcome to the quote generator, " + user_name)
    print("")
    print("The generator will give you a quote corresponding to how you're feeling.")


def main_loop(name):
    """This is the main loop where the users answer is handled"""

    """Different feeling types"""

    print('''
    *********************
    *** Feelings Menu ***
    *********************
    *** A: Sad        ***
    *** B: Angry      ***
    *** C: Tired      ***
    *** D: Happy      ***
    *** E: Worried    ***
    *** F: Annoyed    ***
    *********************
    ''')

    feeling = input("Enter a feeling: ")

    if feeling == "sad".lower() or "a".lower():
        random_number = random.randint(0, len(sad_quotes) - 1)

        print(sad_quotes[random_number])
    elif feeling == "angry".lower() or "b".lower():
        random_number = random.randint(0, len(angry_quotes) - 1)

        print(angry_quotes[random_number])
    elif feeling == "tired".lower() or "c".lower():
        random_number = random.randint(0, len(tired_quotes) - 1)

        print(tired_quotes[random_number])

    elif feeling == "happy".lower() or "d".lower():
        random_number = random.randint(0, len(happy_quotes) - 1)

        print(happy_quotes[random_number])

    elif feeling == "worried".lower() or "e".lower():
        random_number = random.randint(0, len(worried_quotes) - 1)

        print(worried_quotes[random_number])

    elif feeling == "annoyed".lower() or "f".lower():
        random_number = random.randint(0, len(annoyed_quotes) - 1)

        print(annoyed_quotes[random_number])
    else:
        print("Invalid answer, input one of the feelings above and a quote will follow.")
        print('Please try again!')
        main_loop(name)




def start():
    name = get_name()
    print("")
    welcome_message(name)

    main_loop(name)


start()
