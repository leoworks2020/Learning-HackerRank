"""
HackerRank Challenge
-------------------------------------------------------------------
Task
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Function Description
Complete the swap_case function in the editor below.
swap_case has the following parameters:
- string s: the string to modify

Returns
- string: the modified string

Input Format
A single line containing a string s.

Constraints
0 <= len(s) <= 1000

Sample Input 0
HackerRank.com presents "Pythonist 2".

Sample Output 0
hACKERrANK.COM PRESENTS "pYTHONIST 2".
-------------------------------------------------------------------
Challenge Start Date:       2023-07-30
Challenge Completion Date:  2023-07-30
"""
def swap_case(s):
    swap_result = ""
    for w in range(len(s)):
        if s[w] == s[w].upper():
            swap_result = swap_result + s[w].lower()
        elif s[w] == s[w].lower():
            swap_result = swap_result + s[w].upper()
    return swap_result

s = input()
result = swap_case(s)
print(result)