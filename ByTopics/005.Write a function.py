"""
HackerRank Challenge
-------------------------------------------------------------------
An extra day is added to the calendar almost every four years as February 29,
and the day is called a leap day.
It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun.
A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

Task

Given a year, determine whether it is a leap year.
If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
It is only necessary to complete the is_leap function.

Input Format
Read year, the year to test.

Constraints
1900 <= year <= 10(**5)

Output Format
The function must return a Boolean value (True/False).
Output is handled by the provided code stub.

Sample Input 0
1990

Sample Output 0
False

Explanation 0
1990 is not a multiple of 4 hence it's not a leap year.
-------------------------------------------------------------------
Challenge Start Date:       2023-07-11
Challenge Completion Date:  2023-07-11
"""

def is_leap(year):
    leap = False

    # Write your logic here
    year_by_4 = year % 4
    year_by_100 = year % 100
    year_by_400 = year % 400
    # Check if year is divisible by 400
    if year_by_4 == 0:
        if year_by_100 == 0:
            if year_by_400 == 0:
                leap = True
        elif year_by_400 != 0 and year_by_100:
            leap = True
    return leap

print(f'Please input the year: ')
year = int(input())
result = is_leap(year)
print(f'Is this a leap year?: {result}')
