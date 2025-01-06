#Topic : BASIC PYTHON
#Exercise Number : 21
##PROBLEM STATEMENT:
#   Write a Python code to remove repetitive items from a list using for loop.
# Python Version : 3.7
'''Remove repetitive'''
list1=[1,1,2,3,4,4,4,5,5,6]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

#output:
#[1,2,3,4,5,6]
