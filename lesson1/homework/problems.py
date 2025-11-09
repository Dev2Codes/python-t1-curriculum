# Problem 1
# Create a variable for your lucky number and print it.
lucky_number:int = 67
print("My lucky number is {}".format(lucky_number))


# Problem 2
# Create a variable for the number of hours you sleep and print it.
hr_sleep:int = 8
print("The avg time I sleep is around {}".format(hr_sleep))


# Problem 3
# Create a variable for your favorite fruit and print it in a full sentence.
fav_fruit:str = "mango"
print("My favorite fruit is a {}".format(fav_fruit))


# Problem 4
# Create two variables: one for your city and one for your country.
# Print them on 2 separate lines.
city:str = "Redmond"
country:str = "United States of America"
# Could've been smaller if was: location:dict = {"city":"Redmond", "country":"United States of America"}
print("The city I live in is {}\nThe country I live in is the {}".format(city, country))


# Problem 5
# Create 3 variables: your pet's name, its age, and its type.
# Print them on the same line in a full sentence.

class Pet:
    def __init__(self, name:str, age:int, typev:str):
        self.name = name
        self.age = age
        self.type = typev
    
    def describe(self):
        print("The pet, {}, is a {}, who is {} years old".format(self.name, self.type, self.age))

pets = {Pet("Zebra", 10, "plush"), Pet("Rexy", 1, "plush")}

for pet in pets:
    pet.describe()