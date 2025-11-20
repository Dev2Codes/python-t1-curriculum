#custom
from colorama import Fore, Style
import sys


def common():
    print(Fore.RED + "invalid input supplied to inputf(): LEAVING_OVERRIDES: FATAL_ERROR: panic!(restart program)" + Style.RESET_ALL)
    sys.exit("exit code::-67")


def inputf(text:str, prompt:str = "prompt: ", format:str = "s", endl:str = ""):
    match format:
        case "f":
            print(prompt, text, end=endl)
            try:
                return float(input())
            except Exception as e:
                common()
        case "s":
            print(prompt, text, end=endl)
            return input()
        case "i":
            print(prompt, text, end=endl)
            try:
                return int(input())
            except Exception as e:
                common()
        case "li":
            print(prompt, text, end=endl)
            try:
                return list(input().split())
            except Exception as e:
                common()
        case "tu":
            print(prompt, text, end=endl)
            try:
                return tuple(input().split())
            except Exception as e:
                common()
        case "se":
            print(prompt, text, end=endl)
            try:
                return set(input().split())
            except Exception as e:
                common()
        case _:
            raise ValueError(Fore.RED + "invalid paramters supplied to inputf(): LEAVING_OVERRIDES")

# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."

#test scores are sometimes 9.5 or so
test_1:float = inputf("what did you get on last week's algebra test? (%): ", format="f")
test_2:float = inputf("what did you get on yesterday's English quiz? (%): ", format="f")

if (test_1 >= 50 and test_2 >= 50):
    print("great, you passed both")
elif (test_1 < 50 or test_2 < 50):
    print("you sold on at least one")



# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."

food:str = inputf("did you bring food? (Y/n default n):")
water:str = inputf("did you bring water? (Y/n default n):")
foodb:bool = (food == "Y")
waterb:bool = (water == "Y")

if (foodb == True and waterb == True):
    print("you're ready (hopefully)!")
elif (foodb == True or waterb == True):
    print("you'll last a day or two")
else:
    print("go home!")



# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."

number:int = inputf("enter a number:", format="i")
if (1 <= number <= 10):
    print("in range")
else:
    print("OutOfRangeError")

# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random

ai:int = random.randint(1, 10)
user:int = inputf("guess what number I have (1-10)?: ")

if (user == ai and user&2 == 0):
    print("kachow: even match!")
elif (user == ai or user == 5):
    print("kachicka: nice try!")
else:
    print("nope!")



# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
import re
numbers:tuple = inputf("enter an ordered pair of numbers (ie. (2, 3)): ")
numbers_int:list = re.findall(r'-?\d*\.?\d+', numbers)

for x in range(2):
    numbers_int[x] = int(numbers_int[x])

if ((numbers_int[0]%5 == 0 and numbers_int[1]%5 !=0) or (numbers_int[1]%5 == 0 and numbers_int[0]%5 !=0)):
    print("Interesting pair!")
else:
    print("plain pair!")
