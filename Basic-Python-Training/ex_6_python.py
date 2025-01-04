#Topic : BASIC PYTHON
#Exercise Number : 6
##PROBLEM STATEMENT:
#   Read input string from user. Your task is to 
#   find out if the string  contains: alphanumeric characters, alphabetical characters, 
#   digits, lowercase and uppercase characters.
# Python Version : 3.7
"""
    Input Format
        A single line containing a string .
    Output Format
    In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    In the third line, print True if  has any digits. Otherwise, print False.
    In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    Sample Input
        qA2
    Sample Output
        True
        True
        True
        True
        True
"""
name=input()
print(name.isalnum())
for char in name:
    k=char.isalpha()
    if k is True:
        print("true")
        break
if k!=1:
    print("false")
for char in name:
    k=char.isdigit()
    if k is True:
        print("true")
        break
if k!=1:
    print("false")
for char in name:
    k=char.islower()
    if k is True:
        print("true")
        break
if k!=1:
    print("false")
for char in name:
    k=char.isupper()
    if k is True:
        print("true")
        break
if k!=1:
    print("false")
    
