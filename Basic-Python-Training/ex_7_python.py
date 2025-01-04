#Topic : BASIC PYTHON
#Exercise Number : 8
##PROBLEM STATEMENT:
#   Read input string from user which will contain first name and
#   last name of user i.e. sudha murthy.
#   Your task is to make sure that first name and last name of user must be captitalize.
# Python Version : 3.7
"""
Input: 
        sudha murthy
    Output:
        Sudha Murthy
"""
first_name=input("enter your first name: ")
last_name=input("enter your last name: ")
print(first_name.capitalize()+" "+last_name.capitalize())
