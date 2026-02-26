"""
Problem:ASCII Value
Level:1
Date:26-02-26
Time Taken: 2 mins
"""

character = input("Enter the character: ")
if(len(character)!=1):
    print("Enter a single character")
elif not character.isprintable():
    print("Invalid Input")
else:
    print("ASCII Value is: ",ord(character))