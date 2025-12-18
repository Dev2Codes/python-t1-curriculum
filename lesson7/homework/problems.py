# Problem 1
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]

sum_value:int = 0
for number in numbers:
    if number > 25:
        sum_value+=number
print("The sum of only numbers above 25 is: ", sum_value)



# Problem 2
# Find and print the sum of all the numbers less than -10 in the list.
numbers = [-5, -20, -11, 0, 4, -15]

sum_value:int = 0
for number in numbers:
    if number < -10:
        sum_value+=number
print("The sum of only numbers below -10 is: ", sum_value)



# Problem 3
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]

biggest:int = 0
for number in numbers:
    if number > biggest and number < 100:
        biggest = number
print("The biggest number under 100 is: ", biggest)



# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]
print("The largest number is: ", max(numbers))



# Problem 5
# Find and print the total sum of all the numbers in the list.
numbers = [1, 3, 5, 7, 9]
print("The sum is: ", sum(numbers))
