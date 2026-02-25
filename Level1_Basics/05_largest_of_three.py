"""
Problem:Largest of three numbers
Level:1
Date:24-02-26
Time Taken:3mins
"""

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
if (n1>n2 and n1>n3):
    print("n1 is largest number")
elif(n2>n1 and n2>n3):
    print("n2 is largest number")
else :
    print("n3 is largest number")