"""
Problem:Electricity Bill
Level:1
Date:26-02-26
Time Taken: 4 mins
"""

units = int(input("Enter the number of units: "))

if units < 0:
    print("Invalid input")
elif units <= 100:
    bill = units * 5
elif units <=200:
    bill = units * 7
else:
    bill = units * 10
if units>0:
    print("Electricity Bill: ",bill)
    