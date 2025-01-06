#Topic : BASIC PYTHON
#Exercise Number : 15
##PROBLEM STATEMENT:
#   Write a Python code to check whether a given key already exists in a dictionary.
# Python Version : 3.7
'''Dictionary'''
input_dict={
    'name':'Reeya',
    'age':21,
    'Hometown':'Porbandar'
}
input_key=input()
if input_key in input_dict:
    print("Key is Already Exists ")
else:
    print("Key is not Present ")
    
#output:
#Key is Already Exists
    
