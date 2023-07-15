"""
HackerRank Challenge
-------------------------------------------------------------------
Task
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123...n

Note that "..." represents the consecutive values in between.

Example
n = 5
Print the string 12345.

Input Format
The first line contains an integer, n.

Constraints
1 <= n <= 150

Output Format
Print the list of integers from 1 through n as a string, without spaces.

Sample Input 0
3

Sample Output 0
123
-------------------------------------------------------------------
Challenge Start Date:       2023-07-15
Challenge Completion Date:  2023-07-15
"""
def print_number(number):
    string = str
    string = ""
    for n in range(1,number+1):
        string += str(n)
    print(string)

number = int(input())
print_number(number)