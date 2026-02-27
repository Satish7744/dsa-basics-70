"""
Problem:Sum of N Natural Numbers
Level:2
Date:27-02-26
Time Taken: 3mins
"""

n = int(input("Enter the value: "))

if n<=0:
    print("Invalid")
else:
    total = 0
    for i in range(1, n+1):
        total += i
    print(total)