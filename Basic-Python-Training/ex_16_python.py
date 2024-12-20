#Topic : BASIC PYTHON
#Exercise Number : 16
##PROBLEM STATEMENT:
#   Write a Python code to check wherther a given key
#   is exist in a dictionary without using in keyword or handling exceptions.
#   NOTE : Code must not contain the 'in' key word or any exception handling code.
# Python Version : 3.7
'''dictionary'''
input_dict={
    'name':'Reeya',
    'age':21,
    'Hometown':'Porbandar'
}
input_key=input()
if input_dict.get(input_key) is None:
    print("Not Present")
else:
    print("Present")
    
#output:
#Present
