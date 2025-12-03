import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
os: list = ["gentoo", "archlinux", "debian"]
print(os[len(os)-1])
os.reverse()
print(os)

# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subj: list = ["math", "science", "English", "history"]
print("The second subject is {}!".format(subj[1]))
subj.sort()
print(subj)


# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
errno: list = ["418", "404", "100", "500", "403"]
print(len(errno))
try:
    print(errno.index("403"))
except:
    print("An erro occured, sorry! :(")



# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
langs: list = ["C", "B"]
print(random.choice(langs))
langs.append("A")
print(langs)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
pwd: list = ["2#@$@#$232", "23423$$$$", "y2i34@#$@#$", "2347823rERFER#$", "o237$#$@#!@#!@#!@#267"]
print(pwd[round(len(pwd)/2)])
print(pwd.pop(0))
print(pwd)
