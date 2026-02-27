"""
Problem:Multiplication Table
Level:2
Date:27-02-26
Time Taken: 3mins
"""

table_number = int(input("Enter the table number: "))
limit = int(input("Enter the limit value: "))

for i in range(1, limit+1):
    print(table_number, "x", i ,"=",table_number * i)
    