"""
Problem:Factorial of a number
Level:2
Date:27-02-26
Time Taken: 3mins
"""
n = int(input("Enter the value: "))

if n < 0:
    print("Invalid")
else:
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)