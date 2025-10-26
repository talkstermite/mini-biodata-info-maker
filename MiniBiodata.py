# MINI BIODATA INFORMATION MAKER
# USING CONSOLE AND MADE BY TALKSTERMITE
# https://github.com/talkstermite

import colorama
from colorama import Fore, Style
colorama.init()

# PROGRAM TITLE
print(Fore.YELLOW + "========================================")
print("==== MINI BIODATA INFORMATION MAKER ====")
print("==== MADE BY TALKSTERMITE ==============")
print("========================================")
print(Fore.RESET)

# PROGRAM INPUTS
fullName = input("What is the person's full name?: ")
email = input("What is the person's email?: ")
gender = input("What is the person's gender? (M/F): ")
age = int(input("What is the person's real age?: "))
isStudent = (input("Is the person a student? (Y/N): "))
food = input("What is the person's favorite food?: ")

# IF STATEMENTS
if gender == "M" or gender == "m":
    gender = "Male"
elif gender == "F" or gender == "f":
    gender = "Female"
else:
    gender = "Unrecognized gender"

if isStudent == "Y" or isStudent == "y":
    stdnt = f"{fullName} is a student."
elif isStudent == "N" or isStudent == "n":
    stdnt = f"{fullName} is NOT a student."
else:
    stdnt = "Unspecified: is the person a student or not"

# PROGRAM OUTPUT
print()
print(Style.DIM + f"The person's name is {fullName}")
print(f"{fullName}'s email is {email}.")
print(f"{fullName}'s gender is {gender}.")
print(f"{fullName}'s age is {age} years old.")
print(stdnt)
print(f"{fullName}'s favorite food is {food}.")

print()
input(Style.RESET_ALL + "Press the enter key to exit...")