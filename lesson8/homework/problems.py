# Problem 1
# Write a function that returns the number 42 and print the result.
def function1() -> int:
    return 42

print("The meaning of the universe:", function1())



# Problem 2
# Write a function that returns "penguin" and print the result.
def function2() -> str:
    return "penguin"

print("Tux is a", function2())


# Problem 3
# Create a variable for a fruit, then print it.
# Modify it inside a function and print it again.
fruit: str = "mango" # python strings are immutable thus printing inside the func is required
print(fruit)

def function3() -> None:
    print(fruit.upper())


# Problem 4
# Write a function that takes two parameters: first_name and last_name.
# The function should return a string that combines the first and last names separated by a space.
def getname(first_name: str, last_name: str) -> str:
    return "{} {}".format(first_name, last_name)

# extra
print(getname("John", "Cena"))


# Problem 5
# Write a function called calculate_perimeter that takes two parameters: length and width.
# The function should return the perimeter of a rectangle (2 * (length + width)).

def squareperm(l, w) -> float | int:
    return 2 * (l + w)

#extra
print(squareperm(6, 7))
