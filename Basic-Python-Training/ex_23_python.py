#Topic : BASIC PYTHON
#Exercise Number : 23
#PROBLEM STATEMENT:
# You are given a space separated list of integers.
# If all the integers are positive, then you need to check
# if any integer is a palindromic integer.
# Python Version : 3.7
"""
Input Format:
        The first line contains an integer N .N is the total number of
         integers in the list.
        The second line contains the space separated list of  integers.
    Output Format:
        Print True if all the conditions of the problem statement are satisfied.
         Otherwise, print False.
    Sample Input:
        5
        12 9 61 5 14 
    
    Sample Output:
        True
"""
def is_palindrom(num):
    ''' Here i attach palindromic function'''
    return str(num)==str(num)[::-1]

n=int(input())
user_input = input("Enter elements separated by space: ").split()
print(user_input)
PALINDROM_NUM=0
for i in user_input:
    PALINDROM_NUM=is_palindrom(i)
    if PALINDROM_NUM:
        print("True")
        break
else:
    print("False")
