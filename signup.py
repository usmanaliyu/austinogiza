import random
import string
import pickle
import os
import sys
import sqlite3


def connect():
    conn = sqlite3.connect('database.db')
    conn.commit()
    conn.close()


def table():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY, first_name VARCHAR(100), last_name VARCHAR(100), user VARCHAR(100), email VARCHAR(50), password VARCHAR(100) )')
    conn.close()
    conn.close()

def adduser(first_name, last_name, email, password, user):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO user VALUES(Null, ?, ?, ?, ?, ?)",(first_name, last_name, user,email, password))
    conn.commit()
    conn.close()

def allusers():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row

connect()
table()
print( 'Avalable users:')
print(allusers())



first = input("What is your first name?: ")
last = input("What is your last name?: ")
email = input("Enter your email: ")
user_name = first + last




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
    while len(newpass) < 7:
        print('Enter a password more than 7 letters')
        newpass = input("input desired password: ")

    print(newpass)

    adduser(first_name=first, last_name=last, user=user_name, email=email, password=newpass)

elif answer == "yes":
    print("Your password is: " + str(password))
    adduser(first_name=first, last_name=last, user=user_name, email= email, password=password)

 
