# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
while True:
    number1:int = int(input("Enter a number: "))
    number2:int = int(input("Enter another number: "))
    try:
        print("Remainder: {}\nQuotient: {}".format(number1%number2, number1/number2))
        break
    except ZeroDivisionError:
        print("Hey, no 0s!")
        continue


# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
animal:str = input("<fav ~/animal>")
color:str = input("<fav ~/color>")

if (color.lower().startswith(("a", "e", "i", "o", "u"))):
    aword:str = "An"
else:
    aword:str = "A"

print("{} {} colored {} would be cool!".format(aword, color, animal))


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for x in range(11):
    if (x%2 == 0):
        print("{} is even".format(x))



# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
push_ups:int = int(input("How many push-ups can you do in, let's say: 10 seconds?: "))
match(push_ups):
    case push_ups if push_ups > 10:
        print("IT'S JOHN CENA!")
    case push_ups if push_ups > 4:
        print("Great!")
    case _:
        print("Weakling!")

print("You could do: {} push_ups in a week non-stop, don't know where\nyou'll use that but here it is!".format(push_ups*60480))


# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for x in range(7):
    print("{}\u00b2 = {}".format(x, x**x))
