#Topic : BASIC PYTHON
#Exercise Number : 4
##PROBLEM STATEMENT:
#    Code reads two integers a and b from STDIN and Add logic to print five lines.
# Python Version : 3.7
"""
 First line prints the a+b then followed by a-b, a*b, a//b and a/b
   Example:
        a = 4
        b = 3
   Print:
        Addition : 7
        Subtraction : 1
        Multiplication : 12
        Floor Division : 1
        Division : 1.33
"""
a=int(input())
b=int(input())
print("Addition : ",a+b)
print("Subtraction : ",a-b)
print("Multiplication : ",a*b)
print("Floor Division : ",a//b)
print("Division : ",a/b)

#output:
#Addition : 7
#Subtraction : 1
#Multiplication : 12
#Floor Division : 1
#Division : 1.33
