"""
Problem: divisible by five and eleven
Level:1
Date:26-02-26
Time Taken: 2 mins
"""

n = int(input("Enter the number: "))
if (n%5==0 and n%11==0):
    print("Number is not Divisible by 5 and 11")
else:
    print("Not Divisible")