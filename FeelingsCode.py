import arcade
import random

name = ""
choice = ""


def Welcome():
    print("#########")
    print("Welcome!")
    print("#########")
    print("")


Welcome()


name = input("Enter your name: ")
print("Hi, " + name + "!")
print("")
print("A: I feel down")
print("B: I feel a worried")
print("C: I feel happy")
print("")
choice = input("Enter the letter that is nearest to how you are feeling: ")

choices = ['A', 'B', 'C']

choiceA = ['Quote1', 'Quote2', 'Quote3']
choiceB = ['Quote1', 'Quote2', 'Quote3']
choiceC = ['Quote1', 'Quote2', 'Quote3']

random_number = random.randint(0, 2)

if choice == "A", "a":
    print(choiceA[random_number])
elif choice == "B"