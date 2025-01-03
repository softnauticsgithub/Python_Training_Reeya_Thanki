#Topic : BASIC PYTHON
#Exercise Number : 12
##PROBLEM STATEMENT:
#  Write a Python code to read an integer n from user and print
#  the following values for each integer from 1 to n:
#    Decimal
#    Octal
#    Hexadecimal (capitalized)
#    Binary
# Python Version : 3.7
"""
 Sample Input:
        4
    Sample Output:
        1     1     1     1
        2     2     2    10
        3     3     3    11
        4     4     4   100
"""
n=int(input())
for i in range(1,n+1):
    n_bin=bin(i)[2:]
    n_oct= oct(i)[2:]
    n_hex = hex(i)[2:].upper()
    print(f"{i}\t{n_oct}\t{n_hex}\t{n_bin}")
    
#output
#1     1     1     1
#2     2     2    10
#3     3     3    11
#4     4     4   100
