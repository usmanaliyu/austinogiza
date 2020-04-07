import random
import string
import pickle
import os
import sys
import sqlite3

user = []
first = input("What is your first name?: ")
last = input("What is your last name?: ")
email = input("Enter your email: ")
name = first + last
user.append(name)


def randomString():
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, 5))


password = (f"{first[0:2]}{last[-2:]}" + randomString()).lower()

answer = ""


if first and last != "":
    print("Your password is: " + str(password))

    answer = input("Are you satisfied with the password")
if answer == 'no':
    newpass = input("input desired password: ")
    print(newpass)
elif answer == "yes":
    print("Your password is: " + str(password))
if len(newpass) < 7:
    print('Enter a password more than 7 letters')
    newpass = input("input desired password: ")


pickle.dump(user, open("user.dat", "wb"))

user = pickle.load(open("user.dat", "rb"))
