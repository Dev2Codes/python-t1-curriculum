# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
print("Alex appears {} time(s)!".format(names.count("Alex")))



# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
if (animals.count("elephant") == 0):
    print("No 'elephant' in the list")
else:
    print("There is 'elephant' in the list")



# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
print("{} kids got a perfect score!".format(scores.count(100)))



# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
try:
    print("'blue' at index {}".format(colors.index("blue")))
except Exception:
    print("'blue' isn't in the list")



# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]

for temperature in temperatures:
    if temperature < 0:
        print("{} was below 0 degress C".format(temperature))
    """
    # uncomment this for extra functionality
    else:
        print("{} was above 0 degress C".format(temperature))
    """
