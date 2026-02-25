"""
Problem:Simple Interest
Level:1
Date:25-02-26
Time Taken:4 mins
"""

principal = int(input("enter the principle amount: "))
time = float(input("Enter the time of due(years): "))
rate = float(input("Enter the rate of interest: "))

simple_interest = (principal * time * rate) / 100
print("Simple Interest is: ",simple_interest)
