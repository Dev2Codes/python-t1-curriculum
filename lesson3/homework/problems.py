# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
inpu:int = int(input("enter an int value: "))
if (inpu%2 == 0):
    print("that would be even")
else:
    print("that would be odd")


# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
"""
# A+ code
day:str = input("what day is it today?: ").lower()
com:str = "that would be a weekday, but:"
match day:
    case "saturday" | "sunday":
        print("Hooray! It's the weekend!")
    case "monday":
        print(com, "BOO!")
    case "tuesday":
        print(com,"at least it's not Monday!")
    case "wednesday":
        print(com, "mid-week!")
    case "thursday":
        print(com, "ALMOST...")
    case "Friday":
        print(com, "Houston, we have landed!")
    case _:
        print("Where do you live? {} isn't a day!".format(day))
"""
# B- code
day:str = input("what day is it today?: ").lower()
if (day == "saturday" or day == "sunday"):
    print("The good old weekend")
else:
    print("a tipical weekday (sigh)")


# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
import random

while True:
    ai:int = random.randint(1, 10)
    try:
        user:int = int(input("(1-10) which number am I thinking of?: "))
    except ValueError:
        print("CHECK YOUR KEYBOARD DRIVER, as you clearly don't know numbers!")
        continue
    if (ai == user):
        print("CORRECT!")
        break
    else:
        print("Womp Womp! Correct answer was: {}".format(ai))




# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
inpu:int = int(input("enter an int value: "))
if (inpu%2 == 0 and inpu > 10):
    print("Big even number")
else:
    print("DoesNotMeetCriteriaError")



# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
a:int = int(input("enter a number (a): "))
b:int = int(input("enter a number (b): "))
if (a == b):
    print("those numbers are both equal (a=b)")
elif (a > b):
    print("the first number was greater (a>b)")
else:
    print("the second number was greater (b>a)")
