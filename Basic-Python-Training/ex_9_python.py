#Topic : BASIC PYTHON
#Exercise Number : 11
##PROBLEM STATEMENT:
#  Write a Python code to convert a given string to a tuple.
#  Do not include spaces or tabs in the tuple.
# NOTE : Tuple wil contain each character from "string_given".
# Python Version : 3.7
''' hello'''
S_G = 'Hello,this is your Program      . I am  Program'
S_G=S_G.replace(" ","")
R_1=tuple(S_G)
print(R_1)
