"""
Problem:Leap Year
Level:1
Date: 25-02-26
Time Taken: 4 mins
"""
year = int(input("Enter the year: "))
if (year%400==0 ):
    print("Leap year")
elif (year%100==0):
    print("Not a Leap Year")
elif(year%4==0):
    print("Not a Leap Year")
else:
    print("Not a Leap Year")
