"""
Problem: one to n numbers
Level:2
Date:27-02-26
Time Taken: 2mins
"""

n = int(input("Enter the Value: "))

if n > 0:
    for i in range(1, n+1):
        print(i)
else:
    print("enter a positive number")

    