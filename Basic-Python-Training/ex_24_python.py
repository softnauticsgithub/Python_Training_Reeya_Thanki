#Topic : BASIC PYTHON
#Exercise Number : 24
##PROBLEM STATEMENT:
#Write a Python code to find all pairs from a array
#whose division is equal to given integer number.
# Python Version : 3.7
"""
  List: [[9,3], [20,5], [42, 6, 4.5], [4, 5, 0.58] [78,0], [2,3], [4,6], [0, 0], 0, 16, None]
    NOTE: Individual numbers, "None" value must be taken care of during the code. 
    Only two number's division must match with given input. 
    In case of more than two values in the list. Please take last two values from the list
    Sample Input: 0
    Sample Output: 1. [2,3]
                   2. [4,6]
"""
List= [[9, 3], [20, 5], [42, 6, 4.5], [4, 5, 0.58],[78, 0], [2, 3], [4, 6], [0, 0], 0, 16, None]
number=int(input())
list2=[]
for i in List:
    if type(i) is list:
        j=i
        den=j[-1]
        num=j[-2]
        # print(den)
        if den != 0 and num // den == number:
            list2.append(i)
print(list2)
