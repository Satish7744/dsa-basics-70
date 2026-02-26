"""
Problem: Vowel or Consonant
Level:1
Date:26-02-26
Time Taken: 3 mins
"""

letter = input("Enter the letter: ")

if (len(letter)!=1):
    print("Enter a letter")
elif letter.lower() in ('a','e','i','o','u'):
    print("Vowel")
elif letter.isalpha():
    print("Consonant")
else:
    print("Not an Alphabet")