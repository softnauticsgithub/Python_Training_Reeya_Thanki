#Topic : BASIC PYTHON
#Exercise Number : 9
##PROBLEM STATEMENT:
#  Write a Python code to count repeated characters in a string
# Python Version : 3.7
"""
   Sample string: 
        'thequickbrownfoxjumpsoverthelazydog'
    Expected output :
        o 4
        e 3
        u 2
        h 2
        r 2
        t 2
"""
str_1=input()
str_2={}
for i in str_1:
    c=str_1.count(i)
    if i not in str_2.keys()
    	if c>1:
        	str_2[i]=c
for k,v in str_2.items():
    print(k,v)
