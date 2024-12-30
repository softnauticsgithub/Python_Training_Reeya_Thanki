#Topic : BASIC PYTHON
#Exercise Number : 2
##PROBLEM STATEMENT:
#   Read a given string, change the character at a given index and then print the modified string.
# Python Version : 3.7
"""
    - Input Format
        The first line contains a string, .
        The next line contains an integer , denoting the index location
         and a character separated by a space.
    - Output Format
        Using any of the methods explained above, replace the character at index with character .
    - Sample Input
        abracadabra
        5 k
    - Sample Output
        abrackdabra
"""
try:
	name=input("Enter one String:")
	index,ch=input("Please give input seprated by a space!!").split(" ")
except Exception as e:
	print(e)
index=int(index)
x=list(name)
x[index]=ch
RES="".join(x)
print(RES)

