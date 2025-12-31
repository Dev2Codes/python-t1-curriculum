import numpy as np
# Problem 1
# Use a while loop to print the word "Python" 4 times.
print("#PROBLEM 1")
counter:int = 0
while counter != 4:
    print("Python!")
    counter+=1


# Problem 2
# Use a while loop to print the even numbers from 2 to 12 (inclusive).
print("\n#PROBLEM 2")
number:int = 2
while number < 13:
    print(number)
    number+=1


# Problem 3
# Ask the user to input a positive number.
# Use a while loop to count up from 0 to that number (inclusive), printing each number.
print("\n#PROBLEM 3")
inpu:int = int(input("enter an unsigned integer: "))
ccounter:int = 0
if inpu < 0:
    raise ValueError("inputed value was less than 0")
while ccounter < inpu + 1:
    print(ccounter)
    ccounter+=1


# Problem 4
# Ask the user to enter a starting number greater than 10.
# Use a while loop to count down by 5 each time until the number is less than 0.
print("\n#PROBLEM 4")
inpop:float = float(input("enter an unsigned number: ")) # value of 31.4 is still applicable
if inpop <= 10:
    raise ValueError("inputed value was not greater than 10")
while inpop > -1:
    inpop-=5
    print(inpop)


# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
print("\n#PROBLEM 5")
fav_animals:np.array = np.array(["Zebra", "Girrafe", "Elephant"])
counter:int = 0

while counter != fav_animals.size:
    cp:str = fav_animals[counter]
    if (cp.lower().startswith(("a", "e", "i", "o", "u"))):
        aword:str = "An"
    else:
        aword:str = "A"
    print("{} {} is awesome!".format(aword, cp))
    counter+=1
